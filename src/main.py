from fastapi import FastAPI
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from apis.modulename import router_name
from apis.health_check_module import health_check_router
from apis.github import github_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_name)
app.include_router(health_check_router)
app.include_router(github_router)