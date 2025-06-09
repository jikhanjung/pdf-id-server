FROM python:3.13-slim

WORKDIR /app

# 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 모델 및 코드 복사
COPY ./app ./app
COPY ./models /app/models

# FastAPI 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

#docker login
#docker build -t pdf-id-server .
#docker tag pdf-id-server honestjung/pdf-id-server:latest
#docker tag pdf-id-server honestjung/pdf-id-server:v0.0.2
#docker push honestjung/pdf-id-server:latest
#docker push honestjung/pdf-id-server:v0.0.2
#docker run --restart=always --name pdf-id-server -p 8052:8000 honestjung/pdf-id-server:latest
