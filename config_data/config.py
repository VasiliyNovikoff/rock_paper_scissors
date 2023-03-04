from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str          # Токен для доступа к Телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env()
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))


"""Можно упростить: избавиться от класса TgBot, 
а у класса Config атрибут tg_bot заменить на атрибут token. 
Но оставим как есть, подразумевая, что проект может расширяться."""
