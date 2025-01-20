from flask import Flask, request
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        update = request.get_json()
        # Здесь обработка сообщений бота
        return {"status": "ok"}, 200
    else:
        return {"status": "Unsupported Media Type"}, 415
