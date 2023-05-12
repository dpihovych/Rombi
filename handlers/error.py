from aiogram import Router, types, Bot
import config

router = Router()


# @router.message()
# async def cmd_not_found(message: types.Message):
#     upd_msg = message.text
#     upd_msg = upd_msg[1:]
#     if upd_msg not in config.ALL_CMD:
#         # if message.chat.id in config.ADMIN_GROUP:
#         #     await message.answer()
#         # else:
#             await message.answer(f"{message.from_user.full_name} вибач, але я такої команди не знаю, передивися, будь ласка, команду яку ти написав, можливо там є помилка( щоб перевірити чи є помилка в твоїй команді, то напиши - /help.\nЯкщо у тебе є якась скарга, пропозиція і так далі, то у нас є тех. підтримка - @RombiTech_bot, і наші адміністратори і модератори обов'язково дадуть тобі відповідь!")