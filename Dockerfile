FROM python:3.9.4
WORKDIR /fasilitasplanner
COPY requirements.txt /fasilitasplanner/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /fasilitasplanner
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8080","--reload"]

