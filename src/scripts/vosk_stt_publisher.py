#!/usr/bin/env python

from __future__ import print_function

import rospy


import time
from threading import Thread, Event
import websocket
import pyaudio 
try:
	import thread
except ImportError:
	import _thread as thread
import time
import json 

import rospy
from std_msgs.msg import String

# global variable as "correct" handling of threading seems to break the management of websockets...
response = []
error = []
listen = True
vosk_thread = []

def on_message(ws, message):
	global response
	response.append(json.loads(message))

def on_error(ws, error):
	rospy.loginfo("Cannot access the VOSK DOCKER container")
	error.append(json.loads(error))
	

def on_close(ws):
	print("### closed ###")

def on_open(ws):
	# stick to this parameter or it will "fail" in a weird way (no error, but also no answers)
	RATE = 16000
	CHUNK = 8000
	BUFF_SIZE = 4000
	timeout = 5
	steps = RATE/CHUNK*timeout
	p = pyaudio.PyAudio()
	st = p.open(format=pyaudio.paInt16,channels = 1,rate = RATE,input = True, frames_per_buffer = CHUNK)		
	def run(*args):
		while listen: 
			data = st.read(BUFF_SIZE)			
			ws.send(data, opcode=websocket.ABNF.OPCODE_BINARY)
		print("thread terminating...")
	thread.start_new_thread(run, ())


def startListening() :
	global response
	global error
	websocket.enableTrace(False)
	ws = websocket.WebSocketApp("ws://localhost:2700",
							  on_message = on_message,
							  on_error = on_error,
							  on_close = on_close)
	ws.on_open = on_open
	ws.keep_running = False 
	ws.run_forever()

	
	return response


def vosk_talker():
	global response
	global vosk_thread
	pub_partial = rospy.Publisher('vosk/partial_speech', String, queue_size=10)
	pub_speech = rospy.Publisher('vosk/speech', String, queue_size=10)
	pub_fullresults = rospy.Publisher('vosk/confidence', String, queue_size=10)
	rospy.init_node('vosk_STT', anonymous=True)
	vosk_thread =thread.start_new_thread(startListening, ())
	rate = rospy.Rate(5) # 5hz
	while not rospy.is_shutdown():
		if response :
			popstr = response.pop()
			if 'partial' in popstr.keys() :
				pub_partial.publish(popstr["partial"])
			rate.sleep()
			if 'result' in popstr.keys() :
				pub_speech.publish(str(popstr['text']))
				pub_fullresults.publish(str(popstr['result']))
			if len(response) > 10:
				rospy.loginfo("Queue on VOSK response is getting bigger, filtering out older results")
				response = []
		else :
			pass

def shutdown():
	global vosk_thread
	rospy.loginfo("killing vosk listener node")
	listen = False
	

if __name__ == '__main__':
	try:
		vosk_talker()
		rospy.on_shutdown(shutdown)
	except rospy.ROSInterruptException:
	    pass
