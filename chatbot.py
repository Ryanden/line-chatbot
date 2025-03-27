import os
import requests
import schedule
import time
import logging
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수 가져오기
ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
USER_ID = os.getenv('USER_ID')

# 로그 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# 메시지 전송 함수
def send_line_message():
    # 일시정지 여부 확인
    if os.path.exists("pause.txt"):
        logging.info("⏸ 메시지 전송이 일시정지됨.")
        return
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }

    message = '굿모닝! ☀️ 매일 오전 10시에 자동으로 보내는 메시지입니다. 😊'

    data = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

    url = 'https://api.line.me/v2/bot/message/push'
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        logging.info("✅ 메시지가 성공적으로 전송되었습니다!")
        return True  # 메시지가 성공적으로 전송되었음을 표시
    else:
        logging.error(f"❌ 메시지 전송 실패. 상태 코드: {response.status_code}")
        logging.error(f"응답 내용: {response.text}")
        return False  # 메시지 전송 실패

# 매일 오전 10시 실행
schedule.every().day.at("10:00").do(send_line_message)

if __name__ == "__main__":
    logging.info("⏳ 스케줄러 실행 중... 매일 오전 10시에 메시지를 전송합니다.")
    
    start_time = time.time()  # 시작 시간 기록
    
    while True:
        schedule.run_pending()
        
        # 2분(120초)이 지나면 종료
        if time.time() - start_time > 120:  # 120초 = 2분
            logging.info("⏰ 2분 동안 메시지를 받지 않았습니다. 프로그램을 종료합니다.")
            break  # 2분 지나면 종료
        
        time.sleep(60)  # 1분마다 실행 체크
