import telebot
from yt_dlp import YoutubeDL
import os

# Aapka Token yahan setup hai
API_TOKEN = '8289181991:AAFVOIY9NTd_BCXBzLDGu6rB9BfNnBEGit0'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔥 TechVerse Downloader Active! \n\nInsta Reel ya YT link bhejo, main download kar dunga.")

@bot.message_handler(func=lambda m: True)
def download_video(message):
    url = message.text
    if "instagram.com" in url or "youtube.com" in url or "youtu.be" in url:
        bot.send_message(message.chat.id, "⏳ Fetching video... please wait.")
        try:
            # Render/VPS ke liye temporary settings
            ydl_opts = {
                'format': 'best',
                'outtmpl': '/tmp/video.mp4', # Render par /tmp folder use karna safe hai
                'quiet': True
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            with open('/tmp/video.mp4', 'rb') as video:
                bot.send_video(message.chat.id, video, caption="✅ Downloaded by TechVerse Bot")
            
            os.remove('/tmp/video.mp4')
        except Exception as e:
            bot.reply_to(message, "❌ Error: Video download nahi ho payi.")
    else:
        bot.reply_to(message, "⚠️ Bhai, sirf Instagram ya YouTube link bhejo!")

bot.polling()
