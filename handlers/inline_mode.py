from aiogram import html, Router
from aiogram.enums import ChatType
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from fluent.runtime import FluentLocalization

router = Router()


@router.inline_query()
async def inline_mode_handler(query: InlineQuery):
    result = InlineQueryResultArticle(
        id=".",
        title="ID",
        description="ID description",
        input_message_content=InputTextMessageContent(
            message_text="inline-mode-text"
        )
    )
    # Do not forget about is_personal parameter! Otherwise, all people will see the same ID
    # switch_pm_text = l10n.format_value("inline-mode-tryme") if query.chat_type != ChatType.SENDER else None
    await query.answer(
        results=[result], cache_time=3600, is_personal=True
    )