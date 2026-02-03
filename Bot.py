import telebot
from yt_dlp import YoutubeDL
import os
from flask import Flask
from threading import Thread

# --- CONFIGURATION ---
API_TOKEN = '8289181991:AAFVOIY9NTd_BCXBzLDGu6rB9BfNnBEGit0'
CHANNEL_ID = '@onlineDeals25'
# Aapka Monetag Direct Link fit kar diya hai
MONETAG_LINK = "https://otieu.com/4/10562007" 

bot = telebot.TeleBot(API_TOKEN)
app = Flask('')

@app.route('/')
def home(): 
    return "TechVerse Bot is Online & Earning!"

def check_sub(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except: 
        return False

@bot.message_handler(commands=['start'])
def start(message):
    if check_sub(message.from_user.id):
        bot.reply_to(message, "🚀 TechVerse Bot Active!\n\n🔹 Insta Reel: Direct Video milegi.\n🔹 YouTube: Fast Download link milega.")
    else:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Join Channel 📢", url="https://t.me/onlineDeals25"))
        bot.send_message(message.chat.id, "⚠️ Bhai, pehle channel join karo tabhi bot chalega!", reply_markup=markup)

@bot.message_handler
