from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict()

    dev: bool = False
    test_server: bool = False
    developer_id: int
    webhooks: bool = False
    bot_token: SecretStr
    webhook_url: SecretStr
    webhook_secret_token: SecretStr
