## 실행법

pipenv shell

## requirements 가 있을경우
pipenv install

## simple_server.py
유저 아이디 습득

## chatbot.py
유저에게 간단한 메세지 테스트

## tunnel test
플라스크 기동하고 python simple_server.py

npm install -g localtunnel
lt --port 5000

아래에 나오는 url에 
{url}/callback 으로 서버를 열어둠

라인공식어카운트 메세지 셋팅에서 webhook 설정 ON반드시하기, 자동응답은 꺼야됨