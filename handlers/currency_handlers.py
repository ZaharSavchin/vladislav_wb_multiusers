from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from database.database import users_items, save_users_items

from config_data.config import Config, load_config
from aiogram import Bot


router = Router()

config: Config = load_config()
BOT_TOKEN = config.tg_bot.token
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')


help_text = "Теперь отправь боту артикул товара и " \
            "когда наличие или цена изменится, бот пришлет уведомление!"


@router.callback_query(Text(text='rub'))
async def process_rub_press(callback: CallbackQuery):
    users_items[callback.from_user.id][0] = 'rub'
    await callback.answer()
    await bot.send_message(chat_id=callback.from_user.id, text=f"Цены будут отображаться в Российских рублях 🇷🇺\n\n"
                                                               f"{help_text}")
    await save_users_items()
    await callback.message.delete()


@router.callback_query(Text(text='byn'))
async def process_rub_press(callback: CallbackQuery):
    users_items[callback.from_user.id][0] = 'byn'
    await callback.answer()
    await bot.send_message(chat_id=callback.from_user.id, text=f"Цены будут отображаться в Беларусских рублях 🇧🇾\n\n"
                                                               f"{help_text}")
    await save_users_items()
    await callback.message.delete()


@router.callback_query(Text(text='kzt'))
async def process_rub_press(callback: CallbackQuery):
    users_items[callback.from_user.id][0] = 'kzt'
    await callback.answer()
    await bot.send_message(chat_id=callback.from_user.id, text=f"Цены будут отображаться в Казахских тенге 🇰🇿\n\n"
                                                               f"{help_text}")
    await save_users_items()
    await callback.message.delete()


@router.callback_query(Text(text='kgs'))
async def process_rub_press(callback: CallbackQuery):
    users_items[callback.from_user.id][0] = 'kgs'
    await callback.answer()
    await bot.send_message(chat_id=callback.from_user.id, text=f"Цены будут отображаться в Киргизских сомах 🇰🇬\n\n"
                                                               f"{help_text}")
    await save_users_items()
    await callback.message.delete()


@router.callback_query(Text(text='uzs'))
async def process_rub_press(callback: CallbackQuery):
    users_items[callback.from_user.id][0] = 'uzs'
    await callback.answer()
    await bot.send_message(chat_id=callback.from_user.id, text=f"Цены будут отображаться в Узбекских сумах 🇺🇿\n\n"
                                                               f"{help_text}")
    await save_users_items()
    await callback.message.delete()


@router.callback_query(Text(text='usd'))
async def process_rub_press(callback: CallbackQuery):
    users_items[callback.from_user.id][0] = 'usd'
    await callback.answer()
    await bot.send_message(chat_id=callback.from_user.id, text=f"Цены будут отображаться в Долларах США 🇺🇸\n\n"
                                                               f"{help_text}")
    await save_users_items()
    await callback.message.delete()


@router.callback_query(Text(text='amd'))
async def process_rub_press(callback: CallbackQuery):
    users_items[callback.from_user.id][0] = 'amd'
    await callback.answer()
    await bot.send_message(chat_id=callback.from_user.id, text=f"Цены будут отображаться в Армянских драмах 🇦🇲\n\n"
                                                               f"{help_text}")
    await save_users_items()
    await callback.message.delete()
