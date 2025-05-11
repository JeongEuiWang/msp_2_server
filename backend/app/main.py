from fastapi import FastAPI
from app.routers import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="MSP Server",
    description="FastAPI와 MySQL을 사용하는 마이크로서비스 프로젝트",
    version="0.1.0",
)


app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
