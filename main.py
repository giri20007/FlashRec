from pyrogram import Client, filters

API_ID = "25527509"
API_HASH = "2f2fc130d5091f2d09bd303dd2019f6f"
BOT_TOKEN = "7973940134:AAGu1QoWXyvMvjR7AZiZe9rJfhZVbD80TMA"

@flashrec = Client(
    name="flashrec",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
 )


print("Bot flah started")

@flashrec.run()
