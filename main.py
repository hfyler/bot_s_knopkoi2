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
    builder.button(text = "Тыкай сюда", callback_data = "tiknul")
    builder.button(text = "Чё?", callback_data = "che")
    builder.button(text = "А?", callback_data = "aa")
    builder.button(text = "Кнопка в кнопке, это че", callback_data = "kp_in_kp")
    builder.button(text = "Ютуб втф, ты итак можешь??", url = "https://www.youtube.com/")
    builder.adjust(2)
    await message.answer('Тыкай на кнопку', reply_markup=builder.as_markup())

@dp.callback_query(F.data == 'tiknul')
async def pidor(callback: CallbackQuery):
    await callback.message.answer('Ты пидор!')

@dp.callback_query(F.data == 'che')
async def pidor(callback: CallbackQuery):
    await callback.message.answer('Хуй  через плечо11')

@dp.callback_query(F.data == 'aa')
async def pidor(callback: CallbackQuery):
    await callback.message.answer('Хуй на!')

@dp.callback_query(F.data == 'kp_in_kp')
async def dalshe(callback: CallbackQuery):
    builder.button(text = "Дальше", callback_data = "kp_in_kp2")
    await callback.message.answer('Дальше?', reply_markup=builder.as_markup())

if __name__ == "__main__":
    asyncio.run(main())