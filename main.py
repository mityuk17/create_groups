import pymysql
from telethon import TelegramClient
from telethon.tl import functions
import requests

host_name = ''
user_name = ''
password = ''
database = ''
bot = ''

api_id = 9411854
api_hash = '499c76606cefdeadd4b1ece84a5a9932'
client = TelegramClient('my_account', api_id, api_hash)


async def main():
    con = pymysql.connect(host=host_name, user=user_name, password=password, database=database)
    with con:
        cur = con.cursor()
        query = '''SELECT order_id, order_team FROM ealinnlw_fqz.quiz_order '''
        cur.execute(query)
        response = cur.fetchall()
    await client.connect()
    for row in response:
        result = await client(functions.channels.CreateChannelRequest(
            title=row[1],
            megagroup=True,
            about='quiz'
        ))
        chat = (result.updates[1].channel_id)
        print(chat, bot)
        await client.edit_admin(entity=chat, user=bot, is_admin=True)
        link = (await client(functions.messages.ExportChatInviteRequest(peer=chat))).link
        print(link)
        result = await client(functions.channels.InviteToChannelRequest(channel=chat, users=[bot]))
        print(result)
        await client(functions.channels.TogglePreHistoryHiddenRequest(channel=chat, enabled=True))
        # result = await client(functions.channels.LeaveChannelRequest(channel=chat))
        with con:
            cur = con.cursor()
            query = ''' '''
            cur.execute(query)
            con.commit()
        url = ''
        requests.get(url)

    await client.disconnect()


with client:
    client.loop.run_until_complete(main())
