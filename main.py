import os
from pyrogram import Client, filters
from yt_dlp import YoutubeDL

# 🔒 Replace with your actual credentials
API_ID = 25527509
API_HASH = "2f2fc130d5091f2d09bd303dd2019f6f"
BOT_TOKEN = "7973940134:AAEFpYblpqCjYYd0oOLvDoEj8P3Dl_DpDus"

# Initialize bot
app = Client("ytbot", api_id=25527509, api_hash=2f2fc130d5091f2d09bd303dd2019f6f, bot_token7973940134:AAEFpYblpqCjYYd0oOLvDoEj8P3Dl_DpDus=)

# yt-dlp options
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'merge_output_format': 'mp4',
    'quiet': True,
    'noplaylist': True
}

# Start command
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("🎬 Send me a video link (YouTube, TikTok, etc.) to download.")

# Handle video link
@app.on_message(filters.text & ~filters.command(["start"]))
def download(client, message):
    url = message.text.strip()
    status = message.reply("📥 Downloading... Please wait.")
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        if os.path.exists(filename):
            status.edit("📤 Uploading to Telegram...")
            message.reply_video(filename, caption=info.get("title", "Here is your video 🎞️"))
            os.remove(filename)
            status.delete()
        else:
            status.edit("❌ Download failed.")
    except Exception as e:
        status.edit(f"❌ Error: {str(e)}")

app.run()

