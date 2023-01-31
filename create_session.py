from telethon import TelegramClient
api_id = 9411854
api_hash = '499c76606cefdeadd4b1ece84a5a9932'
session_name = input('Введите имя для файла сессии')
client = TelegramClient(session_name, api_id, api_hash)


async def main():
    print(await client.get_me())
    print('Сессия успешно создана.')
with client:
    print(1)
    client.loop.run_until_complete(main())