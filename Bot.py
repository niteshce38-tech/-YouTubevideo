import telebot
from yt_dlp import YoutubeDL
import os
from flask import Flask
from threading import Thread

# --- CONFIGURATION ---
API_TOKEN = '8289181991:AAFVOIY9NTd_BCXBzLDGu6rB9BfNnBEGit0'
CHANNEL_ID = '@onlineDeals25'
MONETAG_LINK = "https://otieu.com/4/10562007" 

bot = telebot.TeleBot(API_TOKEN)
app = Flask('')

@app.route('/')
def home(): return "TechVerse Bot is Online!"

def check_sub(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def start(message):
    if check_sub(message.from_user.id):
        bot.reply_to(message, "🚀 TechVerse Bot Active!\n\n🔹 Insta Link: Direct Video milegi.\n🔹 YouTube: Earning Link + Download.")
    else:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Join Channel 📢", url="https://t.me/onlineDeals25"))
        bot.send_message(message.chat.id, "⚠️ Pehle channel join karein!", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_download(message):
    if not check_sub(message.from_user.id):
        bot.reply_to(message, "❌ Pehle @onlineDeals25 join karo!")
        return

    url = message.text
    # --- INSTAGRAM DIRECT DOWNLOAD ---
    if "instagram.com" in url:
        sent_msg = bot.reply_to(message, "⏳ Insta Reel download ho rahi hai... Wait karein.")
        video_path = f"/tmp/{message.chat.id}.mp4"
        
        try:
            # Code ko force kar rahe hain ki sirf Insta download kare
            ydl_opts = {
                'format': 'best',
                'outtmpl': video_path,
                'quiet': True,
                'no_warnings': True,
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            with open(video_path, 'rb') as video:
                bot.send_video(message.chat.id, video, caption="✅ Insta Reel Downloaded!\n\n📢 Join: @onlineDeals25")
            
            if os.path.exists(video_path):
                os.remove(video_path)
        except Exception as e:
            bot.reply_to(message, "❌ Insta Direct Download fail hua. Shayad account private hai.")
        
        bot.delete_message(message.chat.id, sent_msg.message_id)

    # --- YOUTUBE REDIRECT (SAVEFROM + MONETAG) ---
    elif "youtube.com" in url or "youtu.be" in url:
        markup = telebot.types.InlineKeyboardMarkup()
        btn_earn = telebot.types.InlineKeyboardButton("📥 Download HD (Server 1)", url=MONETAG_LINK)
        btn_dl = telebot.types.InlineKeyboardButton("🚀 Download Video (Server 2)", url=f"https://en.savefrom.net/1-youtube-video-downloader-360v/?url={url}")
        markup.add(btn_earn)
        markup.add(btn_dl)
        bot.send_message(message.chat.id, "✅ YouTube Video Ready!\n\nNiche buttons use karein:", reply_markup=markup)
    
    else:
        bot.reply_to(message, "⚠️ Sahi link bhejiye!")

def run(): app.run(host='0.0.0.0', port=8080)
if __name__ == "__main__":
    Thread(target=run).start()
    bot.polling(none_stop=True)
