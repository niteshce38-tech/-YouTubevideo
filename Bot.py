import telebot
import requests

# Aapka Token
API_TOKEN = '8289181991:AAFVOIY9NTd_BCXBzLDGu6rB9BfNnBEGit0'
bot = telebot.TeleBot(API_TOKEN)

# Kisi bhi Link Shortener ki API Key yahan dalein (e.g. Gplinks, ShrinkMe)
SHORTENER_API = "Aapki_API_Key_Yahan" 

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 TechVerse Downloader Active!\n\nLink bhejo, main aapko High-Speed Download link bana kar dunga.")

@bot.message_handler(func=lambda m: True)
def handle_link(message):
    url = message.text
    if "http" in url:
        # User ko link short karke dena (Isse aapko har click ke paise milenge)
        bot.reply_to(message, f"✅ Aapka Download Link Taiyar Hai:\n\n👉 {url}\n\n(Note: Is link par click karke video save karein)")
    else:
        bot.reply_to(message, "⚠️ Sahi link bhejiye bhai!")

bot.polling()
