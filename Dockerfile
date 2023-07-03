FROM python:3.10-alpine3.17

COPY run.py /run.py

ENTRYPOINT [ "/run.py" ]