FROM amazon/aws-lambda-python:latest

LABEL maintainer="fenris"
# Installs python, removes cache file to make things smaller
RUN dnf update -y && \
    dnf install -y python3 python3-devel python3-pip gcc && \
    dnf clean all

# Copies requirements.txt file into the container
COPY requirements.txt ./
# Installs dependencies found in your requirements.txt file
RUN pip install -r requirements.txt

# Be sure to copy over the function itself!
# Goes last to take advantage of Docker caching.
COPY example_docker_lambda.py ./

# Points to the handler function of your lambda function
CMD ["example_docker_lambda.handler"]