from aiogram.filters.text import Text
from aiogram import types, Router

router = Router()


@router.message(lambda message: 'Окупант' in message.text)
async def putin(message: types.Message):
    await message.answer("а ти фашист")


@router.message(lambda message: 'ОКУПАНТ' in message.text)
async def putin(message: types.Message):
    await message.answer("а ти фашист")


@router.message(lambda message: 'окупант' in message.text)
async def putin(message: types.Message):
    await message.answer("а ти фашист")


@router.message(Text(text=['путін']))
async def putin(message: types.Message):
    await message.answer(" - ху*ло")

@router.message(Text(text=['ІДИ В ДУПУ']))
async def putin(message: types.Message):
    await message.answer("Там платно как би да, такщо іди сам в дупу і поцілуй мене в дупу!")


@router.message(Text(text=['Зеленський', 'ЗЕЛЕНСЬКИЙ']))
async def zelenskiy(message: types.Message):
    await message.answer(" - Наш призидент!")


@router.message(Text(text=['москва']))
async def moskva(message: types.Message):
    await message.answer(" - Горіла, палала🔥🔥🔥🔥")


@router.message(Text(text=['Ромбі', 'ромбі', 'РОМБІ']))
async def rombi(message: types.Message):
    await message.answer(f"Привіт, {message.from_user.full_name}! Що треба?")


@router.message(Text(text=['Ромбі, що таке coding?', 'ромбі, що таке coding?', 'РОМБІ, ЩО ТАКЕ CODING?']))
async def rombi(message: types.Message):
    await message.answer(f"{message.from_user.full_name}, coding це googling")


@router.message(Text(text=['Ромбі, ти де?', 'ромбі, ти де?', 'РОМБІ, ТИ ДЕ?']))
async def rombi(message: types.Message):
    await message.answer(f"Та тут я, навіть поспати не дадуть!")


@router.message(Text(text=['Ромб', 'ромб', 'РОМБ']))
async def rombi(message: types.Message):
    await message.answer(
        f"{message.from_user.full_name}, тебе шо в гуглі забанили? Ну ладно, на покликання https://uk.wikipedia.org/wiki/%D0%A0%D0%BE%D0%BC%D0%B1")


@router.message(Text(text=['А ти хто?', 'а ти хто?', ' А ТИ ХТО?']))
async def rombi(message: types.Message):
    await message.answer(f"Дід пихто!")


@router.message(Text(text=['Хто тут красава?)', 'хто тут красава?)', 'ХТО ТУТ КРАСАВА?)']))
async def moskva(message: types.Message):
    await message.answer("Я")