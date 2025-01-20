import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Токен бота
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Функция для начала общения с ботом (команда /start)
def start(update: Update, context) -> None:
    update.message.reply_text('Привет! Отправь ссылку на рилс из Instagram.')

# Функция для обработки текстовых сообщений
def handle_message(update: Update, context) -> None:
    chat_id = update.message.chat_id
    message_text = update.message.text

    # Ответ пользователю
    update.message.reply_text(f'Ты написал: {message_text}')

# Функция для установки webhook
def set_webhook():
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook?url=https://instagram-reels-bot.vercel.app/"
    response = requests.get(url)
    if response.status_code == 200:
        print("Webhook successfully set!")
    else:
        print("Failed to set webhook.")

# Основная функция, запускающая бота
def main():
    # Настроим бота
    updater = Updater(TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    # Команда /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Обработка текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Установим webhook для Telegram
    set_webhook()

    # Запустим бота
    updater.start_polling()

    # Ожидаем завершения работы
    updater.idle()

if __name__ == '__main__':
    main()
