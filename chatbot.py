import os
import requests
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수 가져오기
access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
user_id = os.getenv('USER_ID')

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}'
}

message = '안녕하세요! 이것은 테스트 메시지입니다.'

data = {
    "to": user_id,
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
    print('메시지가 성공적으로 전송되었습니다!')
else:
    print(f"메시지 전송 실패. 상태 코드: {response.status_code}")
    print(response.text)
