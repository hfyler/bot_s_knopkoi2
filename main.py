from aiogram import Bot, Dispatcher,  F
from token_ import token
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackQuery


bot = Bot(token=token)
dp = Dispatcher ()
builder = InlineKeyboardBuilder ()


async def main():
    await dp.start_polling(bot)

@dp.message(Command('кнопки'))
async def knopki(message: Message):
    builder.button(
        text = "Тыкай сюда",
        callback_data = "tiknul"
    )
    await message.answer('Тыкай на кнопку', reply_markup=builder.as_markup())

@dp.callback_query(F.data == 'tiknul')
async def pidor(callback: CallbackQuery):
    await callback.message.answer('Ты пидор!')



if __name__ == "__main__":
    asyncio.run(main())