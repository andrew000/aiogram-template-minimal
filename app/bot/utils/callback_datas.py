from __future__ import annotations

from typing import ClassVar, TypeVar

from aiogram.filters.callback_data import CallbackData

from utils.callback_data_prefix_enums import CallbackDataPrefix

# Type that is a subclass of CallbackData and has an owner_id attribute of type int
OwnerCallbackData = TypeVar("OwnerCallbackData", bound=CallbackData)
OwnerCallbackData.owner_id = ClassVar[int]


class UniversalWindowCloseCB(CallbackData, prefix=CallbackDataPrefix.universal_close):
    owner_id: int
