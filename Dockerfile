# Python 이미지 사용
FROM python:3.9

WORKDIR /app

# pipenv 설치
RUN pip install --no-cache-dir pipenv

# 프로젝트 복사
COPY . .

# pipenv 환경 설정 & 패키지 설치
RUN pipenv install --deploy --ignore-pipfile

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1

# Flask 앱 실행
CMD ["pipenv", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "simple_server:app"]
