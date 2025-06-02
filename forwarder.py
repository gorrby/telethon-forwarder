from telethon import TelegramClient, events
from telegram import Bot
import asyncio

# --- ТВОИ ДАННЫЕ ---
api_id = 25739501
api_hash = '22651d330b804549e1f995004a075f5e'
session_name = 'session_forwarder'
source_channels = [
    -1001620974581,
    -1001743256029,
    -1002553100753,
    -1002124285588,
    -1002196286683
]
bot_token = '7836673052:AAG10jqD6nDfa98zqDLXUm177iU8L5z95DU'
target_channel = '@avtoprosmotry222'

# --- КЛИЕНТЫ ---
client = TelegramClient(session_name, api_id, api_hash)
bot = Bot(token=bot_token)

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    text = event.message.text or '[не текст]'
    try:
        await bot.send_message(chat_id=target_channel, text=text)
        print(f"✅ Переслано из {event.chat_id} в {target_channel}")
    except Exception as e:
        print(f"⚠️ Ошибка: {e}")

async def main():
    await client.start()
    print("🔁 Скрипт работает. Слушаю каналы...")
    await client.run_until_disconnected()

asyncio.run(main())