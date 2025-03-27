from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

# Webhook을 처리할 엔드포인트
@app.route('/webhook', methods=['POST'])  # POST 요청만 처리
def webhook():
    data = request.json  # 요청의 JSON 데이터 추출
    print(f"Received data: {data}")
    return "OK", 200  # HTTP 200 응답

@app.route('/callback', methods=['POST'])
def callback():
    body = request.get_json()
    
    # 메시지가 왔을 때 userId 확인
    if 'events' in body:
        for event in body['events']:
            if event['type'] == 'message':  # 사용자가 메시지를 보냈을 때
                user_id = event['source']['userId']
                print(f"📌 새로운 사용자 ID: {user_id}")
    
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
