import asyncio
from telegram import Bot

async def send_telegram_message(bot_token, chat_id, message):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)
    print("Message sent!")

# Your bot token and chat ID
bot_token = 'secret'
chat_id = '1secret'

# The message you want to send
message = "Hello from Python via Telegram!"

# Run the async function
asyncio.run(send_telegram_message(bot_token, chat_id, message))
