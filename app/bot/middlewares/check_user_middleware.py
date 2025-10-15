from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final, cast

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject, Update, User

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable


# 777000 is Telegram's user id of service messages
TG_SERVICE_USER_ID: Final[int] = 777000


class CheckUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        user: User = data["event_from_user"]

        if TYPE_CHECKING:
            assert isinstance(event, Update)

        match event.event_type:
            case "message":
                if user.is_bot is False and user.id != TG_SERVICE_USER_ID:
                    # Some logic like get or create user in DB
                    pass

                msg: Message = cast(Message, event.event)

                if (
                    msg.reply_to_message
                    and msg.reply_to_message.from_user
                    and not msg.reply_to_message.from_user.is_bot
                    and msg.reply_to_message.from_user.id != TG_SERVICE_USER_ID
                ):
                    # Some logic like get or create user in DB for msg.reply_to_message.from_user
                    pass

            case "callback_query" | "my_chat_member" | "chat_member" | "inline_query":
                if user.is_bot is False and user.id != TG_SERVICE_USER_ID:
                    # Some logic like get or create user in DB
                    pass

            case _:
                pass

        return await handler(event, data)
