import telebot
from yt_dlp import YoutubeDL
import os

API_TOKEN = '8289181991:AAFVOIY9NTd_BCXBzLDGu6rB9BfNnBEGit0'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔥 TechVerse Downloader Active!\n\nInsta/YT link bhejo.")

@bot.message_handler(func=lambda m: True)
def download_video(message):
    url = message.text
    if "http" in url:
        sent_msg = bot.reply_to(message, "⏳ YouTube Video process ho rahi hai (360p)...")
        video_path = f"/tmp/{message.chat.id}.mp4"
        
        try:
            ydl_opts = {
                # YouTube ke liye format 18 (360p) sabse stable hota hai
                'format': '18/best[ext=mp4]', 
                'outtmpl': video_path,
                'quiet': True,
                'no_warnings': True,
                # Isse YouTube ko lagega ki normal mobile se request hai
                'user_agent': 'Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
            }
            
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            with open(video_path, 'rb') as video:
                bot.send_video(message.chat.id, video, caption="✅ TechVerse: YouTube Download Successful")
            
            if os.path.exists(video_path):
                os.remove(video_path)
            bot.delete_message(message.chat.id, sent_msg.message_id)

        except Exception as e:
            bot.reply_to(message, "❌ YouTube Error: High quality video Render support nahi kar raha. Try small video.")
    else:
        bot.reply_to(message, "⚠️ Sahi link bhejein.")

bot.polling()
