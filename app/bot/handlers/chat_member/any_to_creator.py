from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import (
    ADMINISTRATOR,
    CREATOR,
    MEMBER,
    RESTRICTED,
    ChatMemberUpdatedFilter,
    or_f,
)

if TYPE_CHECKING:
    from aiogram.types import ChatMemberUpdated

router = Router()
logger = logging.getLogger(__name__)


@router.chat_member(
    or_f(
        ChatMemberUpdatedFilter(MEMBER >> CREATOR),
        ChatMemberUpdatedFilter(RESTRICTED >> CREATOR),
        ChatMemberUpdatedFilter(ADMINISTRATOR >> CREATOR),
        ChatMemberUpdatedFilter(CREATOR >> CREATOR),
    )
)
async def any_to_creator(chat_member: ChatMemberUpdated) -> None:
    logger.info(
        "User %s has been promoted to creator in chat %s",
        chat_member.new_chat_member.user.id,
        chat_member.chat.id,
    )
