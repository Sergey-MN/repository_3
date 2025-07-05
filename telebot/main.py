import asyncio
import logging


from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from sqlalchemy import select, update
from sqlalchemy.orm import Session

from database import Orders, Customuser, engine

TOKEN_API = '7529171556:AAFrrFzxO5MBPqaGOrfqdAiya8nKbhBnKT4'

bot = Bot(TOKEN_API)
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


@dp.message(CommandStart())
async def message(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ℹ️ Дать номер", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

    await message.answer('Поделись контактом!', reply_markup=keyboard)


@dp.message(F.contact)
async def get_contact(message: Message):
    phone_number = '+' + message.contact.phone_number
    telegram_id = message.contact.user_id
    with Session(engine) as session:
        # stmt = select(Customuser).where(Customuser.phone == phone_number)
        # result = session.execute(stmt)
        # user = result.scalar_one_or_none()
        # user.telegram_id = telegram_id
        # session.commit()

        stmt = (update(Customuser).where(Customuser.c.phone == phone_number).values(telegram_id=telegram_id)
        )
        result = session.execute(stmt)
        session.commit()

        if result.rowcount > 0:
            await message.answer("Вы успешно зарегистрированы в системе!")
        else:
            await message.answer("Пользователь с таким номером не найден.")




if __name__ == "__main__":
    asyncio.run(main())
