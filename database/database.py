import redis
import json

users_db = {}
# users_db = {5754662958: ['Захар Пчеловод', 'pchelovod_belarus'], 1042048167: ['Zahar', 'ZaharMaster'],
#             6031519620: ["тех поддержка бота 'Енот на куфаре'", 'help_enot_kufar']}

users_items = {}

# users_items = {
#     "6031519620": [
#         "rub",
#         {
#             "183894614": 750.0,
#             "186530511": 2914.0,
#             "136772383": 0.0,
#             "164458866": 782.0,
#             "98679786": 639.0,
#             "167892964": 8983.0,
#             "183894663": 12783.0,
#             "183894366": 0.0,
#             "183894368": 0.0,
#             "183894365": 0.0,
#             "183894361": 0.0,
#             "183894363": 0.0,
#             "145894363": 0,
#             "146894363": 0,
#             "146894368": 783.0,
#             "144810560": 0.0,
#             "183887161": 492.0,
#             "183815963": 590.0,
#             "109750063": 0.0,
#             "177120725": 150000,
#             "182564406": 30000,
#             "177900891": 78291.0,
#             "173142297": 100753.0,
#             "183815992": 0.0,
#             "177819726": 143990.0,
#             "177838392": 158400.0,
#             "177120732": 26516,
#             "154149878": 7946.0,
#             "5274856": 2496.0,
#             "155241213": 18549.0,
#             "177462095": 3691.0,
#             "169370060": 4214.0,
#             "151620293": 3999.0,
#             "150249483": 5200.0,
#             "159944373": 6150.0
#         }
#     ],
#     "1042048167": [
#         "rub",
#         {}
#     ]
# }
# users_items = {5754662958: ['byn', {64161614: 29.07, 60197297: 30.13, 106122360: 33.26,
#                8940466: 5.76, 119448764: 48.73}], 1042048167: ['rub', {77510248: 1648.0,
#                153353594: 389.0, 83862402: 282.0, 14231589: 1168.0}], 6031519620: ['byn', {84296486: 28.57}]}

url_images: [int, str] = {}

users_max_items: [int, int] = {}
# users_max_items: [int, int] = {5754662958: 1, 6031519620: 3}

commercial_dict = {}
# commercial_dict = {65165165165: {'name': 'reclamodatel, anisimova, @katerina',
#                                  'image_url': 'http//...jpg',
#                                  'commercial_url': 'https//...zverugi.com',
#                                  'countries': 'rub, byn, kzt'
#                                  'message': 'join me!!!',
#                                  'sent_messages': 5100,
#                                  'users_go_on_url': 1200}}

r = redis.Redis(host='127.0.0.1', port=6379, db=14)


commercial_dict_json = r.get('commercial_dict')
if commercial_dict_json is not None:
    commercial_dict = json.loads(commercial_dict_json)
    commercial_dict = {int(k): v for k, v in commercial_dict.items()}
    for key, value in commercial_dict.items():
        int(value["sent_messages"])
        int(value["users_go_on_url"])
else:
    commercial_dict = {}



# Получение словаря из Redis
user_dict_json = r.get('users_db')
if user_dict_json is not None:
    users_db = json.loads(user_dict_json)
    users_db = {int(k): v for k, v in users_db.items()}
else:
    users_db = {}


users_max_items_json = r.get('users_max_items')
if users_max_items_json is not None:
    users_max_items = json.loads(users_max_items_json)
    users_max_items = {int(k): int(v) for k, v in users_max_items.items()}
else:
    users_max_items = {}

users_items_dict_json = r.get('users_items')
if users_items_dict_json is not None:
    users_items = json.loads(users_items_dict_json)
    users_items = {int(k): v for k, v in users_items.items()}
    for k, v in users_items.items():
        if len(v) > 1:
            v[1] = {int(k): float(v) for k, v in v[1].items()}
else:
    users_items = {}

url_images_dict_json = r.get('url_images')
if url_images_dict_json is not None:
    url_images = json.loads(url_images_dict_json)
    url_images = {int(k): v for k, v in url_images.items()}
else:
    url_images = {}


async def save_url_images():
    r.set('url_images', json.dumps(url_images))


async def save_users_db():
    r.set('users_db', json.dumps(users_db))


async def save_users_items():
    r.set('users_items', json.dumps(users_items))


async def save_users_max_items():
    r.set('users_max_items', json.dumps(users_max_items))


async def save_commercial_dict():
    r.set('commercial_dict', json.dumps(commercial_dict))
