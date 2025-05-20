from dataclasses import dataclass
from environs import Env

# admin_id = 6031519620
admin_id = 1042048167
# admin_id = 237863005
chat_id = 'https://t.me/+Z6ZhNqYQ_SxlNjBi'

@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN")))