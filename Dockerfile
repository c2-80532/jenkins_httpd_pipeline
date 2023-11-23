FROM python
WORKDIR /src
COPY server.py .
RUN pip3 install flask
EXPOSE 9000
CMD python3 server.py
