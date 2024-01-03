from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.database import set_loop
from AnonXMusic.utils.decorators import AdminRightsCheck
from AnonXMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["/end", "/stop","/cend", "/cstop","end","stop","cend","cstop","ايقاف","#ايقاف","انهاء","#انهاء"], "") & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Anony.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )


@app.on_message(
    filters.command(["/end", "/stop","/cend", "/cstop","end","stop","cend","cstop","ايقاف","#ايقاف","انهاء","#انهاء"], "") & filters.channel & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music_ch(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Anony.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    if message.sender_chat:
        mention = f'<a href=tg://user?id={message.chat.id}>{message.chat.title}</a>'
    else:
        mention = message.from_user.mention
    await message.reply_text(
        _["admin_5"].format(mention)
    )
