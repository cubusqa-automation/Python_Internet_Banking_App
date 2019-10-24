FROM python:3.8
MAINTAINER Vijay.J <vijayjeyaram@gmail.com>
COPY . /Internet_Banking_4.0
ADD requirements.txt /Mobile_Internet_Banking/requirements.txt
RUN pip install -r /Mobile_Internet_Banking/requirements.txt
WORKDIR /Mobile_Internet_Banking/authentication
ENTRYPOINT ["pytest"]
CMD ["-v"]
