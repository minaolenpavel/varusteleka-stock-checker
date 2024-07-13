import asyncio
from telegram import Bot
import secret

async def send_telegram_message(bot_token, chat_id, message, pic_path=None):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)
    if pic_path:
        await bot.send_photo(chat_id=chat_id, photo=open(pic_path, 'rb'))
