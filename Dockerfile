FROM python:3.2
LABEL maintainer="ravi.cs20@iiitmk.ac.in"

WORKDIR /root

RUN git clone --depth=1 https://github.com/ravi-prakash1907/CaterApp.git && \
	cd /root/CaterApp && \
	pip3 install . -r requirements.txt && \
    cd caterapp

CMD /bin/bash