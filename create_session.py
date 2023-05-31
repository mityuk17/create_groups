from telethon import TelegramClient
api_id = 0
api_hash = ''
session_name = input('Введите имя для файла сессии')
client = TelegramClient(session_name, api_id, api_hash)


async def main():
    print(await client.get_me())
    print('Сессия успешно создана.')
with client:
    client.loop.run_until_complete(main())
