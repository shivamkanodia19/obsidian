from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


_PROJECT_ROOT = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(_PROJECT_ROOT / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Anthropic
    anthropic_api_key: str = Field(default="", alias="ANTHROPIC_API_KEY")
    anthropic_model: str = Field(default="claude-sonnet-4-6", alias="ANTHROPIC_MODEL")

    # Kalshi
    kalshi_base_url: str = Field(
        default="https://demo-api.kalshi.co/trade-api/v2", alias="KALSHI_BASE_URL"
    )
    kalshi_api_key_id: str = Field(default="", alias="KALSHI_API_KEY_ID")
    kalshi_private_key_path: str = Field(default="", alias="KALSHI_PRIVATE_KEY_PATH")
    kalshi_environment: str = Field(default="demo", alias="KALSHI_ENVIRONMENT")

    # Robinhood
    robinhood_username: str = Field(default="", alias="ROBINHOOD_USERNAME")
    robinhood_password: str = Field(default="", alias="ROBINHOOD_PASSWORD")
    robinhood_environment: str = Field(default="paper", alias="ROBINHOOD_ENVIRONMENT")

    # Database
    database_url: str = Field(
        default="sqlite+aiosqlite:///./trading.db", alias="DATABASE_URL"
    )

    # Risk gates (hard config — not soft preferences)
    allow_live_trading: bool = Field(default=False, alias="ALLOW_LIVE_TRADING")
    require_manual_confirmation: bool = Field(
        default=True, alias="REQUIRE_MANUAL_CONFIRMATION"
    )

    @property
    def project_root(self) -> Path:
        return Path(__file__).parent.parent.parent


_settings: Settings | None = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
