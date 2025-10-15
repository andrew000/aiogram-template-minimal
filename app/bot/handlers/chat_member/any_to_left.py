from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from aiogram import Bot, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import (
    KICKED,
    LEAVE_TRANSITION,
    LEFT,
    RESTRICTED,
    ChatMemberUpdatedFilter,
    or_f,
)

from errors.errors import TopicClosedError, resolve_exception

if TYPE_CHECKING:
    from aiogram.types import ChatMemberUpdated


router = Router()
logger = logging.getLogger(__name__)


@router.chat_member(ChatMemberUpdatedFilter(LEAVE_TRANSITION))
async def leave_transition(chat_member: ChatMemberUpdated, bot: Bot) -> None:
    logger.info(
        "User %s has left chat %s",
        chat_member.new_chat_member.user.id,
        chat_member.chat.id,
    )

    try:
        await bot.send_message(
            chat_id=chat_member.chat.id,
            text=f"Bye, {chat_member.new_chat_member.user.mention_html()}",
        )

    except TelegramBadRequest as e:
        e = resolve_exception(e)

        match e:
            case TopicClosedError():
                return

            case _:
                raise


@router.chat_member(
    or_f(ChatMemberUpdatedFilter(KICKED >> LEFT), ChatMemberUpdatedFilter(RESTRICTED >> LEFT))
)
async def kicked_to_left(chat_member: ChatMemberUpdated) -> None:
    logger.info(
        "User %s has left chat %s after being kicked or restricted",
        chat_member.new_chat_member.user.id,
        chat_member.chat.id,
    )
