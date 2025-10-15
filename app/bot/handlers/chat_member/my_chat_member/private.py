from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from aiogram import F, Router
from aiogram.enums import ChatType
from aiogram.filters import KICKED, MEMBER, ChatMemberUpdatedFilter

if TYPE_CHECKING:
    from aiogram.types import ChatMemberUpdated

router = Router()
logger = logging.getLogger(__name__)


@router.my_chat_member(ChatMemberUpdatedFilter(KICKED >> MEMBER), F.chat.type == ChatType.PRIVATE)
async def my_chat_member_private_member(chat_member: ChatMemberUpdated) -> None:
    logger.info("Bot was whitelisted by user %s", chat_member.from_user.id)


@router.my_chat_member(ChatMemberUpdatedFilter(MEMBER >> KICKED), F.chat.type == ChatType.PRIVATE)
async def my_chat_member_private_kicked(chat_member: ChatMemberUpdated) -> None:
    logger.info("Bot was blacklisted by user %s", chat_member.from_user.id)
