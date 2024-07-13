import message_sender
import scrapper
import secret
from telegram import Bot
import asyncio

def Main():
    tst_pouch = scrapper.get_stock("https://www.varusteleka.com/en/product/sarma-tst-general-purpose-pouch-zip-s/61190", "M05 Snow Camo")
    ct_10 = scrapper.get_stock("https://www.varusteleka.com/en/product/sarma-tst-cp10-mini-combat-pack-w-flat-shoulder-straps/75035", "M05 Snow Camo")
    ct_15 = scrapper.get_stock("https://www.varusteleka.com/en/product/sarma-tst-cp15-combat-pack-w-flat-shoulder-straps/75036", "M05 Snow Camo")
    items = (tst_pouch, ct_10, ct_15)
    #telegram bot needs to be runned with asynchronous functions
    async def send_messages():
        for item in items:
            message = f'{item["name"]}, {item["stock"]}'
            #will execute the message sending without blocking the whole program
            await message_sender.send_telegram_message(secret.bot_token, secret.chat_id, message, item["image"])
    asyncio.run(send_messages())



if __name__ == "__main__":
    Main()