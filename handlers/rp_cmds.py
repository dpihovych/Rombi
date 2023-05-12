from aiogram import types, Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import ADMINS, BOT_TOKEN
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram import Router
import config

router = Router()
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")


@router.message(Command(commands=["me"]))
async def me_rp_cmd(message: types.Message):
    rp = message.text
    rp = rp[4:]
    await message.answer(f"{message.from_user.full_name} " + rp)


@router.message(Text(text=["дати п'ять", "Дати п'ять", "Дати П'ять", "ДАТИ П'ЯТЬ"]))
async def give_five(message: types.Message):
    await message.answer(f"{message.from_user.full_name} дав п'ять {message.reply_to_message.from_user.full_name}")


@router.message(Text(text=["Вистрілити", "вистрілити", "ВИСТРІЛИТИ"]))
async def vstriluv(message: types.Message):
    if message.reply_to_message.from_user.id not in config.ADMINS:
        await message.answer(
            f"{message.from_user.full_name} вистрілив в {message.reply_to_message.from_user.full_name}")

    if message.reply_to_message.from_user.id in config.ADMINS:
        await message.answer(f"В моїх адміністраторів вистрілити не можна!")
        await bot.send_message(message.reply_to_message.from_user.id,
                               f"Доброго вечора, ми з України! {message.reply_to_message.from_user.full_name}, була спроба вистрілити в Вас, але я не дав цьому статися🙂\n\nКонтакти зрадника:\nХто: {message.from_user.full_name}\nUsername: {message.from_user.username}\nID: {message.from_user.id}")
        await bot.send_message(message.reply_to_message.from_user.id,
                               f"Хочете зв'язатися з {message.from_user.full_name}?")
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text="Нажми меняя", callback_data=f"1:{message.from_user.id}"))
        await bot.send_message(message.reply_to_message.from_user.id, f"Оберіть", reply_markup=builder.as_markup())


@router.callback_query((Text(startswith="1")))
async def user_id_inline_callback1(callback_query: types.CallbackQuery):
    user_id = callback_query.data.split(':')[1]
    await callback_query.answer("Повідомлення було успішно надіслане! Скоро негідник з вами зв'яжеться", True)
    await bot.send_message(user_id, f"З Вами хочуть зв'язатися")


@router.callback_query((Text(startswith="2")))
async def user_id_inline_callback2(callback_query: types.CallbackQuery):
    await callback_query.answer("Ви пожаліли негідника", True)


@router.message(Text(text=["Можна", "можна", "МОЖНА"]))
async def mojna(message: types.Message):
    await message.answer(f"Ща як дам пендика! Мовчи!")

@router.message(Text(text=["хто сказав?", "Хто сказав?", "ХТО СКАЗАВ?", "хто сказав", "Хто сказав", "ХТО СКАЗАВ"]))
async def hto_skzzav(message: types.Message):
    await message.answer(f"Я! Ща як дам пендика! Мовчи!")

@router.message(Text(text=["тваю дівізію", "Тваю дівізію", "ТВАЮ ДІВІЗІЮ", "тваю дівізію!", "Тваю дівізію!", "ТВАЮ ДІВІЗІЮ!", "твою дівізію", "Твою дівізію", "ТВОЮ ДІВІЗІЮ", "твою дівізію!", "Твою дівізію!", "ТВОЮ ДІВІЗІЮ!"]))
async def diviziu(message: types.Message):
    await message.answer(f"Не мою, а твою дівізію!")


@router.message(Text(text=["Дати пендика", "дати пендика", "ДАТИ ПЕНДИКА"]))
async def penduk(message: types.Message):
    if message.reply_to_message.from_user.id not in config.ADMINS:
        await message.answer(
            f"{message.from_user.full_name} дав пендика {message.reply_to_message.from_user.full_name}")

    if message.reply_to_message.from_user.id in config.ADMINS:
        await message.answer(f"Моїм адміністраторам дати пендика не можна!")
        await bot.send_message(message.reply_to_message.from_user.id,
                               f"Доброго вечора, ми з України! {message.reply_to_message.from_user.full_name}, була спроба Вам дати пендика, але я не дав цьому статися🙂\n\nКонтакти зрадника:\n Хто: {message.from_user.full_name}\nUsername: {message.from_user.full_name}\nID: {message.from_user.id}")
        await bot.send_message(message.reply_to_message.from_user.id,
                               f"Хочете зв'язатися з {message.from_user.full_name}?")
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text="✅Так, хочу", callback_data=f"1:{message.from_user.id}"))
        builder.add(types.InlineKeyboardButton(text="🚫Ні, не хочу", callback_data=f"2:{message.from_user.id}"))
        await bot.send_message(message.reply_to_message.from_user.id, f"Оберіть", reply_markup=builder.as_markup())


@router.callback_query((Text(startswith="1")))
async def user_id_inline_callback1(callback_query: types.CallbackQuery):
    user_id = callback_query.data.split(':')[1]
    await callback_query.answer("Повідомлення було успішно надіслане! Скоро негідник з вами зв'яжеться", True)
    await bot.send_message(user_id, f"З Вами хочуть зв'язатися")


@router.callback_query((Text(startswith="2")))
async def user_id_inline_callback2(callback_query: types.CallbackQuery):
    await callback_query.answer("Ви пожаліли негідника", True)
