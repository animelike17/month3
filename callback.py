from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = 'Лучшее направление'
    answers = [
        'frontend',
        'backend',
        'android',
        'ios'
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):

    question = 'Сколько лет Geektech?'
    answers = [
        "4",
        "2",
        "5",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,


    )

async def vetka_quiz_good_1(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Почему хорошо?')


async def vetka_quiz_bad_1(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,",болит голова")





def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(vetka_quiz_good_1,
                                       lambda call: call.data == "button_call_5")
    dp.register_callback_query_handler(vetka_quiz_bad_1,
                                       lambda call: call.data == "button_call_6")