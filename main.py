from aiogram import types
from aiogram.utils import executor
from config import bot,dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(f'привет {message.from_user.full_name}')

@dp.message_handler(commands=['quiz'])
async def quiz1(message:types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('NEXT', callback_data='button_1')
    markup.add(button_1)
    question = "Кто создал Java?"
    answer = [
         'James Gosling',
         'Brad Pitt',
         'Tatjana Bakaltschuk',
         'Napoleon',
         'Bob Marley',
         'Ansu Fati'
     ]
    await bot.send_poll(
        chat_id= message.chat.id,
        question= question,
        options=answer,
        correct_option_id=1,
        explanation='Так кто создал',
        type='quiz',
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == 'button_1')
async def quiz_2(call: types.CallbackQuery):
    question = "Лучший кинорежиссер"
    answer = [
        'James Cameron',
        'Christopher Nolan',
        'Quentin Tarantino',

    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        correct_option_id=0,
        type='quiz'
    )


@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text) * int(message.text))
    else:
        await bot.send_message(message.from_user.id, message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

