from handlers.admin_handlers import MaxItemsCallbackFactory
from aiogram import Router
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from database.database import users_max_items, save_users_max_items, users_items, save_users_items, users_db

router = Router()


@router.callback_query(MaxItemsCallbackFactory.filter())
async def plus_press(callback: CallbackQuery,
                     callback_data: MaxItemsCallbackFactory):
    user_id = callback_data.user_id
    change = callback_data.change
    if change == '+10':
        users_max_items[user_id] += 10
    if change == '+100':
        users_max_items[user_id] += 100
    if change == '+1000':
        users_max_items[user_id] += 1000
    if change == '-10':
        if users_max_items[user_id] > 9:
            users_max_items[user_id] -= 10
        if user_id in users_items and len(users_items[user_id][1]) > users_max_items[user_id]:
            my_dict = users_items[user_id][1]
            while len(users_items[user_id][1]) > users_max_items[user_id]:
                last_key = None
                for key in my_dict:
                    last_key = key
                if last_key:
                    my_dict.pop(last_key)
    if change == '-100':
        if users_max_items[user_id] > 99:
            users_max_items[user_id] -= 100
        if user_id in users_items and len(users_items[user_id][1]) > users_max_items[user_id]:
            my_dict = users_items[user_id][1]
            while len(users_items[user_id][1]) > users_max_items[user_id]:
                last_key = None
                for key in my_dict:
                    last_key = key
                if last_key:
                    my_dict.pop(last_key)
    if change == '-1000':
        if users_max_items[user_id] > 999:
            users_max_items[user_id] -= 1000
        if user_id in users_items and len(users_items[user_id][1]) > users_max_items[user_id]:
            my_dict = users_items[user_id][1]
            while len(users_items[user_id][1]) > users_max_items[user_id]:
                last_key = None
                for key in my_dict:
                    last_key = key
                if last_key:
                    my_dict.pop(last_key)

    i = user_id
    name = users_db[i][0]
    username = users_db[i][1]
    refs = users_max_items[i]
    if i in users_items:
        cur = users_items[i][0]
        items = users_items[i][1:]
        answer = f"{name}(@{username}, {i}, {refs}): {cur}, {items}✅\n"
    else:
        answer = f"{name}(@{username}, {i}, {refs})🤷\n"

    button_plus10 = InlineKeyboardButton(text='+10',
                                         callback_data=MaxItemsCallbackFactory(user_id=i, change='+10').pack())
    button_minus10 = InlineKeyboardButton(text='-10',
                                          callback_data=MaxItemsCallbackFactory(user_id=i, change='-10').pack())
    button_plus100 = InlineKeyboardButton(text='+100',
                                          callback_data=MaxItemsCallbackFactory(user_id=i, change='+100').pack())
    button_minus100 = InlineKeyboardButton(text='-100',
                                           callback_data=MaxItemsCallbackFactory(user_id=i, change='-100').pack())
    button_plus1000 = InlineKeyboardButton(text='+1000',
                                           callback_data=MaxItemsCallbackFactory(user_id=i, change='+1000').pack())
    button_minus1000 = InlineKeyboardButton(text='-1000',
                                            callback_data=MaxItemsCallbackFactory(user_id=i, change='-1000').pack())
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [button_minus10, button_plus10],
        [button_minus100, button_plus100],
        [button_minus1000, button_plus1000]
    ])

    await callback.message.edit_text(text=answer, reply_markup=markup)

    await callback.answer()
    await save_users_items()
    await save_users_max_items()
