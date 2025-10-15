from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from aiogram import F, Router

if TYPE_CHECKING:
    from aiogram.types import Message

router = Router()
logger = logging.getLogger(__name__)


@router.message(F.migrate_from_chat_id)
async def chat_migrate(msg: Message) -> None:
    logger.info("Chat %s migrated to supergroup %s", msg.migrate_from_chat_id, msg.chat.id)
