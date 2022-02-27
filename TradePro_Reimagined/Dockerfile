FROM python:3.7.4-slim

COPY . /app
WORKDIR /app 

RUN python3 -m venv /opt/tradepro_venv

RUN pip install pip --upgrade
RUN /opt/tradepro_venv/pip install -r requirements.txt
RUN chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]
