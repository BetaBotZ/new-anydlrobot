from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import psutil
import time
bot_start_time = time.time()


@Client.on_message(filters.command(["server"]), group=-2)
async def start(client, message):
    bot_uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - bot_start_time)) 
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("JOIN", url="https://t.me/agprojects")],
        [InlineKeyboardButton(
            "Group", url="https://t.me/agprojectschat")]
    ])
    welcomed = f"<b>--Server Details--</b>\n<b>CPU:</b> {psutil.cpu_percent()}%\n<b>RAM:</b> {psutil.virtual_memory().percent}%\n<b>DISK:</b> {psutil.disk_usage('/').percent}%\n\n <b><i>Bot Uptime :</i></b> {bot_uptime}"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
