from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from bot.downloader import *
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Link yuboring – men videoni yoki audioni yuklab beraman.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = update.message.text.strip().lower()

    path = None
    if "youtube.com" in link or "youtu.be" in link:
        path = download_youtube(link)
        send_type = "video"
    elif "tiktok.com" in link:
        path = download_tiktok(link)
        send_type = "video"
    elif "instagram.com" in link:
        path = download_instagram(link)
        send_type = "video"
    elif "facebook.com" in link or "fb.watch" in link:
        path = download_facebook(link)
        send_type = "video"
    elif "twitter.com" in link or "x.com" in link:
        path = download_twitter(link)
        send_type = "video"
    elif "soundcloud.com" in link:
        path = download_soundcloud(link)
        send_type = "audio"
    else:
        await update.message.reply_text("Bu link qo‘llab-quvvatlanmaydi.")
        return

    if isinstance(path, str) and os.path.exists(path):
        with open(path, 'rb') as file:
            if send_type == "video":
                await update.message.reply_video(file)
            elif send_type == "audio":
                await update.message.reply_audio(file)
        os.remove(path)
    else:
        await update.message.reply_text("Yuklab olishda xatolik yuz berdi.")

def setup_handlers(application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))