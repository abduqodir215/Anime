import os
import logging
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8878421158:AAFQnkOu8qzBqTj5uGcHReDxQbHG5KZqw8k"
CHANNEL_ID = -1003960126207 

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "👋 Salom! Anime botga xush kelibsiz.\n\n"
        "Anime qidirish uchun quyidagi formatda yuboring:\n"
        "`/search [Anime nomi] [Fasl]`\n\n"
        "Masalan: `/search Naruto 1`", 
        parse_mode="Markdown"
    )

@dp.message(Command("search"))
async def search_anime(message: types.Message):
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.answer("⚠️ Format noto'g'ri. Namuna: `/search Naruto 1`")
        return
    
    anime_name = args[1]
    season = args[2]
    
    await message.answer(
        f"🔎 **{anime_name}** animesining **{season}-fasli** bo'yicha qidiruv boshlandi...\n"
        f"Kanal ID: {CHANNEL_ID}",
        parse_mode="Markdown"
    )

async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
        
