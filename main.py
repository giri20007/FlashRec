from pyrogram import Client, filters
import subprocess

API_ID = "25527509"
API_HASH = "2f2fc130d5091f2d09bd303dd2019f6f"
BOT_TOKEN = "7973940134:AAGu1QoWXyvMvjR7AZiZe9rJfhZVbD80TMA"

flashrec = Client(
    name="flashrec",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workdir="/tmp"  # Use writable dir
)

@flashrec.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("Hi! Send me a YouTube link and I'll try to download it.")

@flashrec.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text("Send any YouTube video link and I will try to download it using yt-dlp.")

@flashrec.on_message(filters.text & ~filters.command(["start", "help"]))
async def download_video(client, message):
    url = message.text.strip()
    if "youtube.com" in url or "youtu.be" in url:
        await message.reply_text("Downloading...")
        try:
            output_file = "video.mp4"
            subprocess.run(["yt-dlp", "-o", output_file, url], check=True)
            await client.send_video(message.chat.id, video=output_file)
        except Exception as e:
            await message.reply_text(f"Download failed: {e}")
    else:
        await message.reply_text("Invalid link. Please send a valid YouTube URL.")

print("YT-DLP Bot is running...")
flashrec.run()
