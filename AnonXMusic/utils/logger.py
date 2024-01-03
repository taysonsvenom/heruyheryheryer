from pyrogram.enums import ParseMode

from AnonXMusic import app
from AnonXMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>سجل التشغيل {app.mention}</b>
≺•━━﴾࿈ 𝐒𝐎𝐔᚜𝐀𝐕𝐀𝐓𝐀𝐑᚛𝐑𝐂𝐄 ࿈﴿━━•≻
<b>🖤 ايدي المجموعه :</b> <code>{message.chat.id}</code>
<b>🏴‍☠ اسم المجموعه :</b> {message.chat.title}
<b>🔥 يوزر المجموعه :</b> @{message.chat.username}
≺•━━﴾࿈ 𝐒𝐎𝐔᚜𝐀𝐕𝐀𝐓𝐀𝐑᚛𝐑𝐂𝐄 ࿈﴿━━•≻
<b>🕸 ايدي المستخدم :</b> <code>{message.from_user.id}</code>
<b>🥀 اسم المستخدم :</b> {message.from_user.mention}
<b>🕷 يوزر المستخدم :</b> @{message.from_user.username}
≺•━━﴾࿈ 𝐒𝐎𝐔᚜𝐀𝐕𝐀𝐓𝐀𝐑᚛𝐑𝐂𝐄 ࿈﴿━━•≻
<b>🎸 المطلوب :</b> {message.text.split(None, 1)[1]}
<b>👨🏻‍🎤 نوع التشغيل :</b> {streamtype}
≺•━━﴾࿈ 𝐒𝐎𝐔᚜𝐀𝐕𝐀𝐓𝐀𝐑᚛𝐑𝐂𝐄 ࿈﴿━━•≻"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
