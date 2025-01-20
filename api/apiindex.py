import os
import json
import requests

def handler(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        chat_id = data['message']['chat']['id']
        text = data['message']['text']
        user_name = data['message']['from']['first_name']

        welcome_message = f"Привет, {user_name}! Ты отправил: {text}"

        TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': welcome_message
        }

        requests.post(url, data=payload)

        return {
            "statusCode": 200,
            "body": json.dumps({"status": "success"})
        }

    return {
        "statusCode": 404,
        "body": "Not Found"
    }
