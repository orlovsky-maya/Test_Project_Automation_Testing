FROM python:3.10-alpine
RUN apk add --update curl jq
COPY requirements.txt .
WORKDIR /test_project/
RUN pip install -r /requirements.txt
CMD ./run_pytest_docker.sh