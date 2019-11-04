FROM python:3.7
MAINTAINER Vijay.J <vijayjeyaram@gmail.com>
COPY . /Demo_Internet_Banking
ADD requirements.txt /Demo_Internet_Banking/requirements.txt
RUN pip install -r /Demo_Internet_Banking/requirements.txt
WORKDIR /Demo_Internet_Banking/authentication
ENTRYPOINT ["pytest"]
CMD ["-v"]
