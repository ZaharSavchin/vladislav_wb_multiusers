from database.database import users_items, save_users_items, users_db
from services.search_function import get_price, main_search, bot, get_item, get_item_details, get_qty
import asyncio
from config_data.config import admin_id, chat_id


async def monitoring(procent):
    loop_counter = 0
    while True:

        for id_, list_of_items in users_items.copy().items():
            user_channel_status = await bot.get_chat_member(chat_id=chat_id, user_id=id_)
            if user_channel_status.status == 'left':
                continue
            if len(list_of_items[1]) > 0:
                for item_id, price in list_of_items[1].copy().items():
                    try:
                            # actual_price = await get_price(list_of_items[0], item_id)
                            # actual_price_float = actual_price.pop()
                            response = await get_item(currency=list_of_items[0], item_id=item_id)
                            item_details = await get_item_details(response)
                            actual_price = float(item_details.get('salePriceU', None) / 100) if item_details.get('salePriceU', None) is not None else None


                            try:
                                qty = await get_qty(currency=list_of_items[0], item_id=item_id)
                            except Exception:
                                qty = 0
                            name = item_details.get('name', None)

                            if price != 0 and qty == 0:
                                # for id_, user_name in users_db.copy().items():
                                try:
                                    await bot.send_message(chat_id=id_,
                                                               text=f"товара: '{name}'\n"
                                                                    f"(Артикул: {item_id})\n"
                                                                    f"!!!БОЛЬШЕ НЕТ В НАЛИЧИИ!!!"
                                                               )
                                    await main_search(list_of_items[0], item_id, id_, item_details=item_details)
                                except Exception as err:
                                    print(err)

                            if qty == 0:
                                users_items[id_][1][int(item_id)] = 0
                                await save_users_items()
                                continue

                            # if price - actual_price >= price * procent * 0.01:
                            if price - actual_price != 0:
                                if price > actual_price:
                                    sale = price - actual_price
                                    # for id_, user_name in users_db.copy().items():
                                    try:
                                        await bot.send_message(chat_id=id_, text=f"цена товара '{name}' (Артикул: {item_id})"
                                                                                     f" снизилась на {round(sale, 2)} "
                                                                                     f"{list_of_items[0]}")

                                        await main_search(list_of_items[0], int(item_id), id_, item_details=item_details)
                                    except Exception as err:
                                        print(err)
                                if price < actual_price and price != 0:
                                    sale = actual_price - price
                                    # for id_, user_name in users_db.copy().items():
                                    try:
                                        await bot.send_message(chat_id=id_,
                                                                   text=f"цена товара '{name}' (Артикул: {item_id})"
                                                                        f" увеличилась на {round(sale, 2)} "
                                                                        f"{list_of_items[0]}")

                                        await main_search(list_of_items[0], int(item_id), id_,
                                                              item_details=item_details)
                                    except Exception as err:
                                        print(err)

                            if price == 0 and qty != 0:
                                # for id_, user_name in users_db.copy().items():
                                try:
                                    await bot.send_message(chat_id=id_,
                                                               text=f'ТОВАР ПОЯВИЛСЯ В ПРОДАЖЕ!'
                                                                    f"Название: '{name}'\n"
                                                                    f"(Артикул: {item_id})\n"

                                                               )
                                    await main_search(list_of_items[0], item_id, id_, item_details=item_details)
                                except Exception as err:
                                    print(err)

                    except Exception as e:
                        print(e)
            await asyncio.sleep(3)
        loop_counter += 1
        if loop_counter % 25 == 0 or loop_counter == 1:
            await bot.send_message(chat_id=admin_id, text=f"{loop_counter}")
        await asyncio.sleep(5)

