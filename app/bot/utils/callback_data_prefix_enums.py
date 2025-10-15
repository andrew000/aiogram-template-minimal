from dataclasses import dataclass
from typing import Literal


@dataclass
class __CallbackDataPrefix:
    universal_close: Literal["universal_close"] = "u_cls"


CallbackDataPrefix = __CallbackDataPrefix()

__all__ = ("CallbackDataPrefix",)
