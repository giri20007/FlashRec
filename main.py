import os
from pyrogram import Client, filters
from yt_dlp import YoutubeDL

# 🔒 Replace with your actual credentials
API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

# Initialize bot
app = Client("ytbot", api_id=, api_hash=, bot_=)

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

