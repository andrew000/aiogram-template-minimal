from __future__ import annotations

import logging

from aiogram import Router
from aiogram.filters import CommandObject, CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from utils.callback_datas import UniversalWindowCloseCB

router = Router()
logger = logging.getLogger(__name__)


@router.message(CommandStart(deep_link=True))
async def start_cmd_with_deep_link(msg: Message, command: CommandObject) -> None:
    args = command.args.split() if command.args else []
    deep_link = args[0]

    logger.info("User %s started bot with deeplink: %s", msg.from_user.id, deep_link)

    await start_cmd(msg)


@router.message(CommandStart(deep_link=False))  # Deeplink in False will not work as expected
async def start_cmd(msg: Message) -> None:
    await msg.answer(
        f"👋 Hi, {msg.from_user.mention_html()}\n"
        "\n"
        "🤖 This bot demonstrates a Aiogram template.\n"
        "\n"
        "💁‍♂️ Template created for developing bots in the Python programming language using the Aiogram library.\n"
        "\n"
        "🔗 Template: https://github.com/andrew000/aiogram-template\n"
        "<tg-spoiler>😏 Star ⭐️ my repository!</tg-spoiler>\n"
        "\n"
        "💁‍♂️ This template uses the following technologies:\n"
        "<blockquote expandable>\n"
        "<b>Libraries:</b>\n"
        '─ <a href="https://docs.aiogram.dev/en/dev-3.x/">aiogram</a> (library for working with the Telegram Bot API)\n'
        "\n"
        "<b>Other technologies:</b>\n"
        '─ <a href="https://docs.astral.sh/uv/">uv</a> (package and project manager)</blockquote>',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="❌ Close",
                        callback_data=UniversalWindowCloseCB(owner_id=msg.from_user.id).pack(),
                    ),
                ],
            ],
        ),
        disable_web_page_preview=True,
    )
