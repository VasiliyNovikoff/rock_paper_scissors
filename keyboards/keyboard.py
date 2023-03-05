from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# -------- Создадим клавиатуры в 2х вариантах (с билдером и без)
# -------- Создаём клавиатуру через ReplyKeyboardBuilder --------

# Создаем кнопки с ответами согласия и отказа
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для кнопок согласия и отказа
builder_yes_no: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметром width=2
builder_yes_no.row(button_yes, button_no, width=2)

# Создаем клавиатуру для кнопок согласия и отказа
kb_yes_no: ReplyKeyboardMarkup = builder_yes_no.as_markup(one_time_keyboard=True,
                                                          resize_keyboard=True)

# -------- Создадим клавиатуру без билдера ----------------------

# Создадим кнопки для камня, ножниц и бумаги
button_rock: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_scissors: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_paper: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
kb_game: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_rock], [button_scissors], [button_paper]],
                                                   resize_keyboard=True)
