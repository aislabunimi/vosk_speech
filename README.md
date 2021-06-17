# vosk_speech
ROS node for speech to text using VOSK on a docker container

Works with [ROS](http://wiki.ros.org/) and python 2.7.
Tested with ROS melodic.

This package provides real-time and offline speech-to-text using [VOSK](https://alphacephei.com/vosk/).

You should install VOSK in its [websocket server version](https://alphacephei.com/vosk/install) using docker. 
A configuration file for installing the docker container is provided.

## Description

This package provide a speech to text module that is aimed to be fast and working locally on the robot, to bypass network delays that could jeopardize human robot ineteraction. IT relies on a relatively lightweight speech to text library, VOSK, which supports multiple languages. The payoff is in the fact that accuracy of the recognized speech could be lower wrt other alternatives (e.g., Google Cloud Services).
The advantage is that you can have a speech to text module always active on the robot, and have faster results.

**Note THAT**

This is a first draft of the module that works as a publisher.
In the following months (hopefully) expect
1. this code to be refined and improved 
2. The possibility to ask the Vosk SST service to act as a [ROS Action Server](http://wiki.ros.org/actionlib) and not as a ROS topic.

If you want to contribute, feel free to do so!

## Usage

1. Start the docker container
2. Start
```
vosk_sst_publiser.py
```
3. You should see three topics being published. All three of them publish String messages. The topics are.
`vosk/speech` publishes sentences as they are recognized in their entirety. If you are intereted in full sentences, use this topic.
`vosk/partial_speech` publishes partial partial results from speech in real time as they are translated into text. If you need more accuracy, use the `vosk/speech` results. If want to get a prompter results (e.g., getting a "no" or "yes" utterance and you are not interested in the full sentence, use this topic.
`vosk/confidence` publishes, for each word published in a `vosk/speech` channel the confidence for each world.


## Dependencies

### Main dependencies
```
docker
ROS
```

### Python dependencies

You need python 2.7. It may work on python3 but no tests have been done.
Besides that, you need the following libraries (to be installed either with pip or from apt)
```python
websockets
rospy
threading
pyaudio
 ```
 
 ### Docker container setup
 1. Install docker
 2. (opt) Installa a management tool for docker containers (e.g., [dockstation](https://dockstation.io/))
 3. Install the container by using the Dockerfile provided in the repo. [Here](https://docs.docker.com/get-started/02_our_app/) you can find some documentation about that. 
 
 **Note that** the Dockerfile is configured to use a VOSK model trained in **Italian language** to recognize it. If you need another language or you want to change the model, please edit the Dockerfile. 
To do so do the following:
```
docker build -f /path/to/a/Dockerfile .

```
 4. Start the Container
