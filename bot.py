from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Замени токен на свой
TOKEN = "8196991937:AAGbHFaC5WspH06hmYWWHlFdPO4dQ1INPkY"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Девачкиииии будем делать проект ")

# Запуск бота
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
