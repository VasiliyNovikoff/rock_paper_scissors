from aiogram import Router
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message
from keyboards.keyboard import kb_yes_no, kb_game
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner


router: Router = Router()


# Этот хэндлер будет срабатывать на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=kb_yes_no)


# Этот хэндлер будет срабатывать на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'],
                         reply_markup=kb_yes_no)


# Этот хэндлер будет срыбатывать на согласие пользователя сыграть в игру
@router.message(Text(text=LEXICON_RU['yes_button']))
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'],
                         reply_markup=kb_game)


# Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
@router.message(Text(text=LEXICON_RU['no_button']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])


# Этот хэндлер будет срабатывает на любую из игровых кнопок
@router.message(Text(text=[LEXICON_RU['rock'],
                           LEXICON_RU['scissors'],
                           LEXICON_RU['paper']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} - {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=kb_yes_no)
