# adapted from https://github.com/opsani/servo-ec2asg-newrelic/blob/master/Dockerfile
FROM python:3.6-slim

WORKDIR /servo

# Install dependencies (use latest pip packages)
# hadolint ignore=DL3013
RUN apt-get update && apt-get install -y --no-install-recommends apache2-utils curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install requests PyYAML python-dateutil boto3
    

# Change /usr/bin/python3 => /usr/local/bin/python3, since the first is older,
# so that import of boto3 works
RUN rm -f /usr/bin/python3 && \
	ln -s /usr/local/bin/python3 /usr/bin/python3

RUN mkdir encoders/ measure.d/

# Install servo:  ec2win adjust (which uses the servo base adjust.py) and
# aws cloudwatch measure (which uses the servo base measure.py) and
# dotnet encoder (which users encoders/base.py)
ADD https://raw.githubusercontent.com/opsani/servo/master/servo \
    https://raw.githubusercontent.com/opsani/servo/master/adjust.py \
    https://raw.githubusercontent.com/opsani/servo/master/measure.py \
    https://raw.githubusercontent.com/kumulustech/servo-ec2win/master/adjust \
    https://raw.githubusercontent.com/kumulustech/servo-agg/master/measure \
    https://raw.githubusercontent.com/opsani/servo-agg/master/util.py \
    /servo/

ADD https://raw.githubusercontent.com/opsani/servo/master/encoders/base.py \ 
    https://raw.githubusercontent.com/kumulustech/encoder-dotnet/master/encoders/dotnet.py \
    /servo/encoders/ 

ADD https://raw.githubusercontent.com/opsani/servo-ab/master/measure \
    /servo/measure.d/01ab

ADD https://raw.githubusercontent.com/kumulustech/servo-cloudwatch/master/measure \
    /servo/measure.d/02cloudwatch

RUN chmod a+rwx /servo/adjust /servo/measure /servo/servo /servo/measure.d/01ab /servo/measure.d/02cloudwatch
RUN chmod a+rw /servo/measure.py /servo/adjust.py encoders/base.py encoders/dotnet.py

# TODO: remove when testing complete
RUN sed -i 's/30,         # warmup time in seconds/0,         # warmup time in seconds/' measure.d/01ab
RUN sed -i 's/180,         # time limit in seconds/900,         # time limit in seconds/' measure.d/01ab

ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "python3", "servo" ]
