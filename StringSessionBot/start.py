from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup

                
@Client.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
        await cmd.reply_photo(
		photo="https://telegra.ph/file/2c08b9817d7585736d89a.jpg", caption=Data.START, 		        
		reply_markup=InlineKeyboardMarkup(Data.buttons)
        )
