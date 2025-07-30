from pyrogram import Client, filters

API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

app = Client("flashrec", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.text & filters.private)
def reply_hi(client, message):
    if message.text.lower() == "hi":
        message.reply("Hello!")

app.run()
