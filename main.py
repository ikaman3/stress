from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apis import board, comment, utils

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"]
)

app.include_router(router=board.router)
app.include_router(router=comment.router)
app.include_router(router=utils.router)