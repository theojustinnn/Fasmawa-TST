FROM python:3.9.4
WORKDIR /fasilitasplanner3
COPY requirements.txt /fasilitasplanner3/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /fasilitasplanner3
EXPOSE 8000

CMD ["uvicorn","main:app","--host=0.0.0.0","--reload"]
