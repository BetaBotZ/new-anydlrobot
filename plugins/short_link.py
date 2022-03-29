''''from os import environ
# Moved Back to asyncio-dev branch of pyrogram
from pyrogram import Client, filters, inlineKeyboardButton, inlineKeyboardMarkup
import pyshorteners

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('TG_BOT_TOKEN')
API_KEY = environ.get('API_KEY')

bot = Client('Shortlink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)




@bot.on_message(filters.regex(r'https?://[^\s]+') & Filters.private)
async def link_handler(bot, update):
    link = update.matches[0].group(0)
    if API_KEY:
      try:
        s = pyshorteners.Shortener() 
        shortened_url = s.dagd.short(link)
        button = [[inlineKeyboardButton("Link 🔗", url=shortened_url)]]
        markup = inlineKeyboardMarkup(button)
        await update.reply_text(text=f'Here is your shortlink \n`{shortened_url}`', reply_markup=markup, quote=True)
        
      except Exception as e:
        await update.reply(f'Error: {e}', quote=True)
    else:
      try:
        s = pyshorteners.Shortener() 
        shortened_url = s.dagd.short(link)
        button = [[inlineKeyboardButton("Link 🔗", url=shortened_url)]]
        markup = inlineKeyboardMarkup(button)
        await update.reply_text(text=f'Here is your shortlink \n`{shortened_url}`', reply_markup=markup, quote=True)
        
      except Exception as e:
        await update.reply(f'Error: {e}', quote=True)

      

bot.run()
'''
