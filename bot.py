import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    await message.reply("Привет! Я бот, развернутый на Railway.")

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
