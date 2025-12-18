from pyrogram import Client, filters
import yt_dlp
import os

API_ID = 36657002
API_HASH = "99e33aed3f9757c797436bf284e47fb6"
BOT_TOKEN = "5938139554:AAGHqW4h-0NKPAWaS00X2JhwmhHnl52KeHs"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("أهلاً بك! أرسل رابط تيك توك وسأقوم بالتحميل فوراً.")

@app.on_message(filters.text & filters.private)
async def download_video(client, message):
    url = message.text
    if "tiktok.com" in url:
        status = await message.reply("⏳ جاري التحميل...")
        file_name = f"video_{message.chat.id}.mp4"
        ydl_opts = {'format': 'best', 'outtmpl': file_name, 'quiet': True}
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            await message.reply_video(file_name, caption="تم التحميل بواسطة بوتك الخاص ✅")
            if os.path.exists(file_name): os.remove(file_name)
            await status.delete()
        except Exception as e:
            await status.edit(f"❌ خطأ: {str(e)}")
    else:
        await message.reply("الرابط غير صحيح.")

app.run()

