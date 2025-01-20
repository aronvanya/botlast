from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "Server is running"}

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print(data)  # Для отладки, можно удалить позже
    return {"ok": True}

if __name__ == "__main__":
    app.run()
