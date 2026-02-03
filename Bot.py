import telebot
from flask import Flask
from threading import Thread

API_TOKEN = '8289181991:AAFVOIY9NTd_BCXBzLDGu6rB9BfNnBEGit0'
CHANNEL_ID = '@onlineDeals25'
bot = telebot.TeleBot(API_TOKEN)

app = Flask('')
@app.route('/')
def home(): return "Bot is Alive!"

def check_sub(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def start(message):
    if check_sub(message.from_user.id):
        bot.reply_to(message, "🚀 TechVerse Active!\n\nYouTube ya Insta link bhejo, main aapko high-speed download link bana kar dunga.")
    else:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Join Channel 📢", url="https://t.me/onlineDeals25"))
        bot.send_message(message.chat.id, "⚠️ Bhai, pehle hamare channel ko join karein!", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_links(message):
    if not check_sub(message.from_user.id):
        bot.reply_to(message, "❌ Pehle channel join karo bhai!")
        return

    url = message.text
    if "youtube.com" in url or "youtu.be" in url or "instagram.com" in url:
        # Jugaad: External Downloader Link (Yahan aap Monetag link bhi add kar sakte hain)
        download_url = f"https://en.savefrom.net/1-youtube-video-downloader-360v/?url={url}"
        
        markup = telebot.types.InlineKeyboardMarkup()
        # Yahan aap apna Monetag Direct Link bhi dal sakte hain
        btn = telebot.types.InlineKeyboardButton("📥 Download Video (All Quality)", url=download_url)
        markup.add(btn)
        
        bot.send_message(message.chat.id, "✅ Aapka Download Link Taiyar Hai!\n\nNiche button par click karke video save karein:", reply_markup=markup)
    else:
        bot.reply_to(message, "⚠️ Sirf YouTube ya Insta link bhejiye!")

def run(): app.run(host='0.0.0.0', port=8080)
if __name__ == "__main__":
    Thread(target=run).start()
    bot.polling(none_stop=True)
    
