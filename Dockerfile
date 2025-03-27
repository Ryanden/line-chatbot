# Python 이미지 기반
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 환경 변수 로드
ENV PYTHONUNBUFFERED=1

# Flask 서버 실행 (Gunicorn 사용)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "simple_server:app"]
