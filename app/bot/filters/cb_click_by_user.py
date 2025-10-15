from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram.filters import Filter

if TYPE_CHECKING:
    from aiogram.types import CallbackQuery

    from utils.callback_datas import OwnerCallbackData


class CallbackClickedByTargetUser(Filter):
    async def __call__(
        self,
        query: CallbackQuery,
        callback_data: OwnerCallbackData | None = None,
    ) -> bool:
        if not callback_data or not hasattr(callback_data, "owner_id"):
            return False

        if query.from_user.id != callback_data.owner_id:
            await query.answer("❌", show_alert=True)
            return False

        return True
