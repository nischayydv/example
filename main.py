import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello!\n\n"
        "Bot is running on Render successfully.\n\n"
        "Commands:\n"
        "/start - Start bot\n"
        "/ping - Check bot status"
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! Bot is working.")


def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))

    print("🤖 Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
