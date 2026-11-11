import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    text = (
        "🌌 STAR MARKET\n\n"
        "Добро пожаловать в магазин звёзд!\n\n"
        "✨ Здесь можно приобрести собственную звезду,\n"
        "🌙 заказать кусочек галактики,\n"
        "💖 или найти кое-что особенное.\n\n"
        "Специальное предложение уже подготовлено!\n\n"
        "🔎 Посмотри, что есть в наличии..."
    )

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            "🔎 Посмотреть наличие",
            callback_data="check"
        )
    )

    bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):
    bot.answer_callback_query(call.id)

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            "Кажется, догадываюсь ❤️",
            callback_data="guess"
        )
    )

    bot.send_message(
        call.message.chat.id,
        "🔍 Проверка наличия завершена...\n\n"
        "💫 Обнаружен особенный человек!\n\n"
        "❤️ Я тебя люблю, Соня.\n\n"
        "(Угадай кто?)",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: call.data == "guess")
def guess(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "❤️ Твой Сеня ❤️")


if __name__ == "__main__":
    print("STAR MARKET запущен!")
    bot.infinity_polling()
