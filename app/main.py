# マイグレーション実行
from alembic import command
from alembic.config import Config

alembic_cfg = Config("alembic.ini")
command.upgrade(alembic_cfg, "head")

# fastapiアプリケーション実行
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


from app.api.routes.user import router as user_router
from app.api.routes.word import router as word_router

# from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# app.add_middleware(
#     # CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,  # 追記により追加
#     allow_methods=["*"],  # 追記により追加
#     allow_headers=["*"],  # 追記により追加
# )


# エラーハンドリング
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


app.include_router(user_router)
app.include_router(word_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
