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
 3. Install the container by using the Dockerfile provided in the repo. [Here](https://docs.docker.com/get-started/02_our_app/) you can find some documentation about that. **Note that** the Dockerfile is configured to use a VOSK model trained in **Italian language** to recognize it. If you need another language or you want to change the model, please edit the Dockerfile. 
To do so do the following:
```
docker build -f /path/to/a/Dockerfile .

```
 4. Start the Container
