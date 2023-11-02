FROM python:3.13.0a1-alpine3.18
RUN apk add --update curl jq
COPY requirements.txt .
WORKDIR /test_project/
RUN pip install -r /requirements.txt
CMD ./run_pytest.sh