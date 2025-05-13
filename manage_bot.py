import os
import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    setup_handlers(application)
    print("Bot is running...")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())