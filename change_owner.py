from telethon import TelegramClient, errors
from telethon.tl import functions
api_id = 9411854
api_hash = '499c76606cefdeadd4b1ece84a5a9932'
client = TelegramClient('my_account', api_id, api_hash)


async def main():
    chat_link = input('Введите ссылку на чат:')
    try:
        res = await client(functions.messages.ImportChatInviteRequest(hash=chat_link))
        chat_id = res.updates[1].channel_id
    except errors.UserAlreadyParticipantError:
        res = await client(functions.messages.CheckChatInviteRequest(chat_link))
        chat_id = res.chat.id
    print(chat_id)
    new_owner = None
    async for member in client.iter_participants(entity=chat_id):
        if not member.bot:
            new_owner = member.id
            break
    pwd = await client(functions.account.GetPasswordRequest())
    print(pwd)
    result = await client(functions.channels.EditCreatorRequest(
        channel=chat_id,
        user_id=new_owner,
        password=pwd

    ))
    print(result)
with client:
    client.loop.run_until_complete(main())