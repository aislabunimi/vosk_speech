FROM alphacep/kaldi-vosk-server:latest

ENV MODEL_VERSION 0.4
RUN mkdir /opt/vosk-model-it \
   && cd /opt/vosk-model-it \
   && wget -q https://alphacephei.com/vosk/models/vosk-model-small-it-${MODEL_VERSION}.zip \
   && unzip vosk-model-small-it-${MODEL_VERSION}.zip \
   && mv vosk-model-small-it-${MODEL_VERSION} model \
   && rm vosk-model-small-it-${MODEL_VERSION}.zip

EXPOSE 2700
WORKDIR /opt/vosk-server/websocket
ENV VOSK_SAMPLE_RATE 16000
CMD [ "python3", "./asr_server.py", "/opt/vosk-model-it/model" ]
