import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PORT = int(os.getenv("PORT", "8080"))


# -------------------------
# HTTP SERVER
# -------------------------

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Telegram Bot is running!")

    def log_message(self, format, *args):
        return


def run_server():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"🌐 HTTP server running on port {PORT}")
    server.serve_forever()


# -------------------------
# TELEGRAM BOT
# -------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello!\n\n"
        "🤖 Bot is running on Render.\n"
        f"🌐 Port: {PORT}\n\n"
        "Commands:\n"
        "/start - Start bot\n"
        "/ping - Check status"
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! Bot is working.")


# -------------------------
# MAIN
# -------------------------

def main():

    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set")

    # Start HTTP server in background
    threading.Thread(
        target=run_server,
        daemon=True
    ).start()

    # Telegram application
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))

    print("🤖 Telegram bot started...")

    app.run_polling()


if __name__ == "__main__":
    main()
