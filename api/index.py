import os
from flask import Flask, request, jsonify
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

app = Flask(__name__)

# Получаем токен из переменной окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

# Создаём диспетчер для обработки команд и сообщений
dispatcher = Dispatcher(bot, None, workers=0)

# Обработчик команды /start
def start(update, context):
    update.message.reply_text("Привет! Я бот, работающий через вебхук на Vercel.")

# Обработчик текстовых сообщений
def echo(update, context):
    update.message.reply_text(f"Вы сказали: {update.message.text}")

# Регистрируем обработчики
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Маршрут для обработки вебхуков
@app.route("/", methods=["POST"])
def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
        return "OK", 200

# Маршрут для проверки состояния сервера
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Server is running"}), 200
