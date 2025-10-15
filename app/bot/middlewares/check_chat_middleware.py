from __future__ import annotations

from typing import TYPE_CHECKING, Any

from aiogram import BaseMiddleware
from aiogram.enums import ChatType

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable

    from aiogram.types import Chat, TelegramObject, Update

ALLOWED_CHAT_TYPES: frozenset[ChatType] = frozenset(
    (ChatType.GROUP, ChatType.SUPERGROUP),
)


class CheckChatMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        chat: Chat = data["event_chat"]

        if TYPE_CHECKING:
            assert isinstance(event, Update)

        match event.event_type:
            case "message":
                if chat.type in ALLOWED_CHAT_TYPES:
                    if (
                        event.message.migrate_to_chat_id
                        or event.message.group_chat_created
                        or event.message.supergroup_chat_created
                    ):
                        return None

                    if event.message.migrate_from_chat_id:
                        return await handler(event, data)

            case "callback_query" | "my_chat_member" | "chat_member":
                # Some logic like get chat settings from DB
                pass

            case _:
                pass

        return await handler(event, data)
