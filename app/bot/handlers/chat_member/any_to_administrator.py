from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import ADMINISTRATOR, CREATOR, PROMOTED_TRANSITION, ChatMemberUpdatedFilter

if TYPE_CHECKING:
    from aiogram.types import ChatMemberUpdated

router = Router()
logger = logging.getLogger(__name__)


@router.chat_member(ChatMemberUpdatedFilter(PROMOTED_TRANSITION))
@router.chat_member(ChatMemberUpdatedFilter(ADMINISTRATOR >> ADMINISTRATOR))
@router.chat_member(ChatMemberUpdatedFilter(CREATOR >> CREATOR))
async def any_to_administrator(chat_member: ChatMemberUpdated) -> None:
    logger.info(
        "User %s has been promoted to administrator in chat %s",
        chat_member.new_chat_member.user.id,
        chat_member.chat.id,
    )
