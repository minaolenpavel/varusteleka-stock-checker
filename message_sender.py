import asyncio
from telegram import Bot

async def send_telegram_message(bot_token, chat_id, message, pic_path=None):
    bot = Bot(token=bot_token)
    if pic_path:
        #importance of the async function, the picture gets sent which can take some time
        #it will perform the picture sending, without blocking the whole program
        await bot.send_photo(chat_id=chat_id, photo=open(pic_path, 'rb'), caption=message)
    else:
        await bot.send_message(chat_id=chat_id, text=message)


