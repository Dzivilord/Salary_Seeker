FROM python:3.11-slim-bullseye

WORKDIR /Deployment

COPY Deployment/requirements.txt requirements.txt

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
       build-essential gcc g++ python3-dev \
       curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY Deployment/ /Deployment/

COPY start.sh /Deployment/start.sh
RUN chmod +x /Deployment/start.sh

CMD ["./start.sh"]
EXPOSE 8000
EXPOSE 8501
