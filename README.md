# vosk_speech
ROS node for speech to text using VOSK on a docker container

Works with [ROS](http://wiki.ros.org/) and python 2.7.
Tested with ROS melodic.

This package provides real-time and offline speech-to-text using [VOSK](https://alphacephei.com/vosk/).

You should install VOSK in its [websocket server version](https://alphacephei.com/vosk/install) using docker. 
A configuration file for installing the docker container is provided.




## Dependencies

### Main dependencies
```
docker
ROS
```

### Python dependencies
```python
python 2.7+
websockets
rospy
threading
pyaudio
 ```
