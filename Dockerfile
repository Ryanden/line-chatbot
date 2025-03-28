# 1. 공식 Python 3.9 이미지 사용
FROM python:3.9

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 현재 폴더의 모든 파일을 컨테이너로 복사
COPY . .

# 4. pip 최신 버전으로 업데이트 후 패키지 설치
RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r requirements.txt

# 5. 컨테이너 실행 시 gunicorn으로 Flask 서버 실행
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "simple_server:app"]