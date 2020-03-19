FROM python:3.7
ADD . /analysis
WORKDIR /analysis
RUN pip install -r requirements.txt
