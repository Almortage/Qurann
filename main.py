import asyncio

import os
import time
import requests
from config import Config
from pyrogram import filters
import random
from pyrogram import Client
import app
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from random import  choice, randint

api_id: int = Config.API_ID
api_hash: str = Config.API_HASH
bot_token: str = Config.TG_BOT_TOKEN

bot = Client(
    "azkar-bot",
     api_id=api_id,
     api_hash=api_hash,
     bot_token=bot_token)

REPLY_MESSAGE = "**🧑🏻‍✈️︙اهلا بك عزيزي العضو ♥️**\n**⤵️︙ في بوت اذكار الاسلامي اختر ما تريد من الاسفل**"
REPLY_MESSAGE_BUTTONS = [
    [
             ("المبرمج")
          ],
          [
             ("احاديث دينية"),
              ("خطب دينيه")
          ],
          [
             ("قران"),
              ("نقشبندي")
          ],
          [
              ("عبدالباسط"),
              ("تلاوات")
          ],
          [
             ("كتب دينية")
          ],
          [           
        ("❎ ¦ حذف الكيبورد")
    ]
]

@app.on_message(filters.command(commands=['help','start'], prefixes=['!', '/'], case_sensitive = False))
async def madison(client: Client, message: Message): 
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )


@app.on_message(filters.command(["كتب دينية"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,1959)
    url = f"https://t.me/kotobeslameah/{rl}"
    await client.send_document(message.chat.id,url,caption="💙 ¦ تـم اختيـار كتاب لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["احاديث دينية"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(799,1341)
    url = f"https://t.me/dmatrix12/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار احاديث لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["تلاوات", "تلاوة"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(24,618)
    url = f"https://t.me/EIEI06/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار تلاوة قرآنيه لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["خطب دينيه"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,201)
    url = f"https://t.me/fresdewi/{rl}"
    await client.send_voice(message.chat.id,url,caption="💙 ¦ تـم اختيـار خطبه لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["سوره", "قران"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,82)
    url = f"https://t.me/opuml/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار ايـه قرآنيه لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["الشيخ", "النقشبندي", "نقشبندي"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,114)
    url = f"https://t.me/ggcnjj/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ نقشبندي لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["عبدالباسط", "عبدالباسط عبدالصمد"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(7,265)
    url = f"https://t.me/telawatnader/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ عبدالباسط لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["المبرمج"],""))
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/d0a2e1e5a0dd7ddbd6512.mp4",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[ᯓ 𓆩 ˹ ᴍʀ ᴇʟᴍᴏʀᴛᴀɢᴇʟ ˼⍣⃝🇪🇬𓆪𓆃](https://t.me/Almortagel_12)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @Almortagel_12 ❫
◉ 𝙸𝙳      : ❪ 5089553588 ❫
◉ 𝙱𝙸𝙾    : ❪ صلي علي الحبيب محمد ✨♥ ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ 𓆩 ˹ ᴍʀ ᴇʟᴍᴏʀᴛᴀɢᴇʟ ˼⍣⃝🇪🇬𓆪𓆃", url=f"https://t.me/Almortagel_12"),
                ],

            ]

        ),

    )
    
bot.run()