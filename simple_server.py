
from flask import Flask, request, jsonify, render_template
import os
import requests
import logging
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수 가져오기
ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
USER_ID = os.getenv('USER_ID')

# 로그 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)

# 메시지 전송 함수
def send_line_message():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }

    message = '📢 버튼을 눌러 전송된 메시지입니다!'

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
        return True
    else:
        logging.error(f"❌ 메시지 전송 실패. 상태 코드: {response.status_code}")
        logging.error(f"응답 내용: {response.text}")
        return False

# 홈 페이지: 버튼이 있는 HTML 페이지 렌더링
@app.route('/')
def home():
    return render_template('index.html')

# 버튼을 누르면 메시지 전송
@app.route('/send_message', methods=['POST'])
def send_message():
    success = send_line_message()
    if success:
        return jsonify({"status": "success", "message": "메시지가 전송되었습니다."})
    else:
        return jsonify({"status": "error", "message": "메시지 전송 실패."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
