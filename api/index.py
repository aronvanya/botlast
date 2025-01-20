import os
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from flask import Flask, request, jsonify

app = Flask(__name__)

# Получаем токен из переменной окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

# Создаём диспетчер
dispatcher = Dispatcher(bot, None, workers=0)

# Обработчик команды /start
def start(update, context):
    update.message.reply_text("Привет! Я бот на Vercel. Отправьте мне сообщение.")

# Обработчик всех текстовых сообщений
def echo(update, context):
    update.message.reply_text(f"Вы сказали: {update.message.text}")

# Регистрируем обработчики
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Обработка вебхука
@app.route("/", methods=["POST"])
def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
        return "OK", 200

# Проверка, если сервер работает
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Server is running"}), 200
