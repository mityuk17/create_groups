import asyncio
import logging
from telethon import TelegramClient
from telethon.tl import functions

bot = '@NeverNowhere_bot'
api_id = 9411854
api_hash = '499c76606cefdeadd4b1ece84a5a9932'
client = TelegramClient('my_account', api_id, api_hash)
logging.basicConfig(level=logging.INFO)


async def main():
    await client.connect()
    result = await client(functions.channels.CreateChannelRequest(
        title='chat1',
        megagroup = True,
        about='quiz'
    ))
    chat = (result.updates[1].channel_id)
    print(chat,bot)
    await client.edit_admin(entity=chat, user=bot, is_admin=True)
    link = (await client(functions.messages.ExportChatInviteRequest(peer=chat))).link
    print(link)
    result = await client(functions.channels.InviteToChannelRequest(channel=chat, users = [bot]))
    print(result)
    result = await client(functions.channels.TogglePreHistoryHiddenRequest(channel=chat, enabled=True))
    #result = await client(functions.channels.LeaveChannelRequest(channel=chat))
    await client.disconnect()


with client:
    client.loop.run_until_complete(main())