from Data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from StringSessionBot.generate import generate_session, ERROR_MESSAGE, withoutapigenerate


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user["mention"]
    query = callback_query.data.lower()
    if query.startswith("generate"):
        if query == "generate":
            await callback_query.message.reply(
            """Welcome to Merissa Pyrogram and Telethon String Session Generator.


You can procees with bot's api values if you want , else you can proceed with your api values

Bot has over 100+ API ID and HASH Saved , You can use them. 


Press Button Below to Start Generating Session!""",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Pyrogram", callback_data="pyrogram"),
                InlineKeyboardButton("Telethon", callback_data="telethon")],
               [InlineKeyboardButton("Using Bot's Apiid And Hash", callback_data="cbgenerate")
            ]])
        )
    elif query in ["pyrogram", "telethon"]:
        await callback_query.answer()
        try:
            if query == "pyrogram":
                await generate_session(bot, callback_query.message)
            else:
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
    elif query in ["cbpyrogram", "cbtelethon"]:
        await callback_query.answer()
        try:
            if query == "cbpyrogram":
                await withoutapigenerate(bot, callback_query.message)
            else:
                await withoutapigenerate(bot, callback_query.message, telethon=True)
        except Exception as e:
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
    elif query == "cbgenerate":
        await callback_query.message.reply(
            """Press Button Below to Start Generating Session!""",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Pyrogram Music-Bot", callback_data="cbpyrogram")],
                [InlineKeyboardButton("Telethon User-Bot", callback_data="cbtelethon")
            ]])
        )
