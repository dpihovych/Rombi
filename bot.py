import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import MenuButtonWebApp, WebAppInfo
from aiogram.utils.i18n import I18n, ConstI18nMiddleware

import config
from config import BOT_OWNER
from aiogram.fsm.storage.memory import MemoryStorage
import handlers
import filters
from filters.bot_filters import IsChatAdmin
from handlers import personal_actions, rp_cmds, admin, moderation, qr, registration  # , no_prefix


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")

    # await bot.set_chat_menu_button(menu_button=MenuButtonWebApp(
    #     type="web_app", text="Open",
    #     web_app=WebAppInfo(url="https://google.com")
    # ))
    dp = Dispatcher(storage=MemoryStorage())


    # роутери
    dp.include_router(registration.router)
    dp.include_router(personal_actions.router)
    dp.include_router(rp_cmds.router)
    # dp.include_router(no_prefix.router)
    dp.include_router(admin.router)
    dp.include_router(moderation.router)
    dp.include_router(qr.router)
    # dp.include_router(error.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot started successfully!")
    asyncio.run(main())
