import asyncio
import logging
import os
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardBuilder, InlineKeyboardButton

load_dotenv(".env")
TOKEN = os.getenv("TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu aleykum, <b>{message.from_user.full_name} Link yuboring !!!</b>")


@dp.message()
async def send_message(message: Message) -> None:
    copied_message = message.text
    result = copied_message[:12] + "dd"
    sss = copied_message[12:]
    await message.answer(text=result + sss, parse_mode=ParseMode.HTML)


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
