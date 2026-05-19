from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from backend.api.routes.upload_routes import (
    router as upload_router
)

from backend.api.routes.ask_routes import (
    router as ask_router
)

from backend.api.routes.chat_routes import (
    router as chat_router
)

app = FastAPI()


# ---------- CORS ----------

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# ---------- ROUTES ----------

app.include_router(upload_router)

app.include_router(ask_router)

app.include_router(chat_router)