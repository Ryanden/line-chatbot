# Python 3.9 이미지 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# pipenv 설치
RUN pip install --no-cache-dir pipenv

# 프로젝트 복사
COPY . .

# pipenv 환경 설정 & 패키지 설치
RUN pipenv install --deploy --ignore-pipfile

RUN pipenv run pip install gunicorn  # gunicorn 설치 추가

# Gunicorn을 이용해 Flask 앱 실행
CMD ["pipenv", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:${PORT}", "simple_server:app"]