print("📦 Скрипт запущен. Ожидаю сообщения...")

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    print(f"✉️ Пересылаю из {event.chat_id} в {target_channel}")
    await client.send_message(target_channel, event.message)


from telethon import TelegramClient, events

# Твои данные:
api_id = 25739501
api_hash = '22651d330b804549e1f995004a075f5e'

# Каналы
source_channel = [-1001620974581, -1001743256029, -1002553100753, -1002124285588, -1002196286683]  # ID закрытого канала-источника
target_channel = 'avtoprosmotry222'  # Юзернейм канала-приемника

# Создаём клиент
client = TelegramClient('session_forwarder', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    await client.send_message(target_channel, event.message)

client.start()
client.run_until_disconnected()
