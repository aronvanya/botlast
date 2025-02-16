from flask import Flask, request
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        update = request.get_json()
        print(update)  # Логирование обновлений для проверки
        return {"status": "ok"}, 200
    else:
        return {"status": "Unsupported Media Type"}, 415

if __name__ == '__main__':
    app.run(debug=True)
