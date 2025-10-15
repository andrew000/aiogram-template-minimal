from aiogram import Router

from . import universal_close

router = Router()
router.include_routers(
    universal_close.router,
)
