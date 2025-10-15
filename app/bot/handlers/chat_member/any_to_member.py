from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from aiogram import Bot, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import JOIN_TRANSITION, MEMBER, ChatMemberUpdatedFilter

from errors.errors import TopicClosedError, resolve_exception

if TYPE_CHECKING:
    from aiogram.types import ChatMemberUpdated


router = Router()
logger = logging.getLogger(__name__)


@router.chat_member(ChatMemberUpdatedFilter(JOIN_TRANSITION))
async def left_to_member(chat_member: ChatMemberUpdated, bot: Bot) -> None:
    logger.info(
        "User %s has joined the chat %s",
        chat_member.new_chat_member.user.id,
        chat_member.chat.id,
    )

    try:
        await bot.send_message(
            chat_id=chat_member.chat.id,
            text=f"Welcome, {chat_member.new_chat_member.user.mention_html()}",
        )

    except TelegramBadRequest as e:
        e = resolve_exception(e)

        match e:
            case TopicClosedError():
                return

            case _:
                raise


@router.chat_member(ChatMemberUpdatedFilter(MEMBER))
async def any_to_member(chat_member: ChatMemberUpdated) -> None:
    logger.info(
        "User %s is now a member of chat %s",
        chat_member.new_chat_member.user.id,
        chat_member.chat.id,
    )
