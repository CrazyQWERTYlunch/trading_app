"""
This file serves as the entry point to the Trading App application.
It contains the configuration of FastAPI and integrates various components of the application,
such as routers, authentication settings, CORS Middleware, and caching settings using Redis.
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
import uvicorn

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate
from src.config import REDIS_HOST, REDIS_PORT
from src.operations.router import router as router_operation
from src.tasks.router import router as router_tasks
from src.pages.router import router as router_pages
from src.chat.router import router as router_chat

# Создаем экземпляр FastAPI
app = FastAPI(
    title="Trading App"
)

# Монтируем статические файлы
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Включаем маршруты аутентификации и регистрации пользователей
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_operation)
app.include_router(router_tasks)
app.include_router(router_pages)
app.include_router(router_chat)

# Устанавливаем CORS (Cross-Origin Resource Sharing) Middleware для разрешения запросов с других доменов
origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS","DELETE", "PUT", "PATCH"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Origin",
                   "Access-Control-Allow-Headers",
                   "Authorization"]
)


async def startup_event():
    """
    Function called when the FastAPI application starts up.

    It establishes a connection with Redis and initializes FastAPICache
    for caching data in the application.

    Returns:
        None
    """
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
app.add_event_handler("startup", startup_event)

# if __name__ == '__main__':
#     uvicorn.run('main:app', reload=True)