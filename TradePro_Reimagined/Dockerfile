FROM python:3.7.4-slim

COPY . /app
WORKDIR /app 

RUN python3 -m venv /opt/tradepro_venv

RUN /opt/tradepro_venv/bin/pip3 install pip --upgrade && \
/opt/tradepro_venv/bin/pip3 install -r requirements.txt && \
chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]