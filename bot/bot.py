from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from app.config import settings

bot = Bot(
    token=settings.bot_token,
    default=DefaultBotProperties(parse_mode="HTML"),
)
