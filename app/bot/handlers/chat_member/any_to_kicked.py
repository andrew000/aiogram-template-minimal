from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import KICKED, ChatMemberUpdatedFilter

if TYPE_CHECKING:
    from aiogram.types import ChatMemberUpdated

router = Router()
logger = logging.getLogger(__name__)


@router.chat_member(ChatMemberUpdatedFilter(KICKED))
async def any_to_kicked(chat_member: ChatMemberUpdated) -> None:
    logger.info(
        "User %s has been kicked from chat %s",
        chat_member.new_chat_member.user.id,
        chat_member.chat.id,
    )
