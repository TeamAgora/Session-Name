from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝐇𝐞𝐲 {msg.from_user.mention}🍷,

𝐈 𝐀𝐦 {me2},
𝐓𝐑𝐔𝐒𝐓𝐄𝐃 𝐒𝐓𝐑𝐈𝐍𝐆 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐎𝐑 𝐁𝐎𝐓.
𝐅𝐔𝐋𝐋𝐘 𝐒𝐀𝐅𝐄 & 𝐒𝐄𝐂𝐔𝐑𝐄.
𝐍𝐎 𝐀𝐌𝐘 𝐄𝐑𝐑𝐎𝐑.

sᴇssɪᴏɴ ɴᴀᴍᴇ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [@ᴛᴇᴀᴍᴀɢᴏʀᴀ](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🦋 ɢᴇɴᴇʀᴀᴛᴏʀ sᴇssɪᴏɴ 🦋", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("🦋 sᴜᴘᴘᴏʀᴛ ¹ 🦋", url="https://t.me/agoraworld"),
                    InlineKeyboardButton("🦋 sᴜᴘᴘᴏʀᴛ ² 🦋", url="https://t.me/agorasmuseum")
                    InlineKeyboardButton("🦋 ᴜᴘᴅᴀᴛᴇs 🦋", url="https://t.me/Teamagora"),
                    InlineKeyboardButton("🦋 ᴀɢᴏʀᴀ ʀᴇᴘᴏs 🦋", url="https://t.me/agorarepos")
                    InlineKeyboardButton("🦋 ᴏᴡɴᴇʀ 🦋", url="https://user?id={OWNER_ID}"),
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
