FROM python:3.6

EXPOSE 8000
WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

# CMD ["./run_app.sh"]
CMD ["python", "server.py"]
