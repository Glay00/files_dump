from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    name: str

    class Config:
        env_prefix = "DB_"

    @property
    def dsn(self) -> str:
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
        )


class Config:
    db: DatabaseConfig = DatabaseConfig()


def setup_config() -> Config:
    return Config()
