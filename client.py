from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp



async def command_start(message: types.Message):
    await message.answer(f"Салалекум {message.from_user.id}")
    await message.reply(f"Привет босс {message.from_user.first_name}!")



async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "в чем смысл жизни?"
    answers = [
        'ни в чем',
        'его нет',
        'я хз',
        'вроде есть',
        'да',
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="смысла жизни нет)))",
        reply_markup=markup
    )



async def mem(message: types.Message):
    photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)

async def pin(message: types.Message):
    if not message.reply_to_message:
        await message.reply('команда должна быть ответов на сообщение')
    else:
        await bot.pin_chat_message(message.chat.id, message.message_id)

async def vetka_quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()

    button_call_5 = InlineKeyboardButton("Хорошо",callback_data="button_call_5")

    button_call_6 = InlineKeyboardButton("Плохо", callback_data="button_call_6")

    markup.add(button_call_5, button_call_6)

    await bot.send_message(message.chat.id, 'Как настроение?',reply_markup=markup)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(vetka_quiz_1, commands=['vetka'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')