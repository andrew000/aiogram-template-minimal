from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router

from filters.cb_click_by_user import CallbackClickedByTargetUser
from utils.callback_datas import UniversalWindowCloseCB

if TYPE_CHECKING:
    from aiogram.types import CallbackQuery


router = Router()


@router.callback_query(UniversalWindowCloseCB.filter(), CallbackClickedByTargetUser())
async def universal_close_cb(cb: CallbackQuery) -> None:
    await cb.message.edit_text("✅ Closed")
