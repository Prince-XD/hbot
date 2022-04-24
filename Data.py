from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey Welcome to @PrincexStringGenBot
───────────────────────
**You can use me to Generate Pyrogram and Telethon String Session. Use below buttons to Learn More** !
───────────────────────
**Powered By**:~ **@PrincexBots**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Generate Session", callback_data="generate")],
        [InlineKeyboardButton(text="Back", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Generate Session", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Generate Session", callback_data="generate")],
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ],
        [InlineKeyboardButton("Updates", url="https://t.me/PrincexNetwork"),
         InlineKeyboardButton("Support", url="https://t.me/PrincexSupport"),
        ],
    ]

    # Help Message
    HELP = """
✗ **Available Commands** 
────────────────────────
/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
✗ **About This Bot** 
────────────────────────
A Telegram Bot to Generate Pyrogram and Telethon String Session Made by [Prince](https://t.me/Princebots)
────────────────────────
✗ Source Code : [Click Here](https://t.me/princexbots)

✗ Framework : [Pyrogram](docs.pyrogram.org)

✗ Language : [Python](www.python.org)

✗ Developer : [Prince](https://t.me/Princexbots)
    """
