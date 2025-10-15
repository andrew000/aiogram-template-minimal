from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import RESTRICTED, ChatMemberUpdatedFilter

if TYPE_CHECKING:
    from aiogram.types import ChatMemberUpdated

router = Router()
logger = logging.getLogger(__name__)


@router.chat_member(ChatMemberUpdatedFilter(RESTRICTED))
async def any_to_restricted(chat_member: ChatMemberUpdated) -> None:
    logger.info(
        "User %s has been restricted in chat %s",
        chat_member.new_chat_member.user.id,
        chat_member.chat.id,
    )
