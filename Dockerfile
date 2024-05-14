FROM python:3.9-slim

RUN pip install requests

COPY swagger-server-handler.py .

CMD ["python", "swagger-server-handler.py"]