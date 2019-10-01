FROM python:3.7
MAINTAINER Vijay.J <vijayjeyaram@gmail.com>
COPY . /Internet_Banking_4.0
ADD requirements.txt /Internet_Banking_4.0/requirements.txt
RUN pip install -r /Internet_Banking_4.0/requirements.txt
WORKDIR /Internet_Banking_4.0/authentication
ENTRYPOINT ["pytest"]
CMD ["-v"]
