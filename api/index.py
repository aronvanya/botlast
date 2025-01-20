import os
import json
import requests

def handler(request):
    if request.method == 'POST':
        try:
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

            response = requests.post(url, data=payload)

            # Проверка успешности запроса к Telegram
            if response.status_code != 200:
                return {
                    "statusCode": 500,
                    "body": f"Error sending message: {response.text}"
                }

            return {
                "statusCode": 200,
                "body": json.dumps({"status": "success"})
            }

        except Exception as e:
            return {
                "statusCode": 500,
                "body": f"Error: {str(e)}"
            }

    return {
        "statusCode": 404,
        "body": "Not Found"
    }
