"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os
from mangum import Mangum
from django.core.asgi import get_asgi_application
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_asgi_application()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from polls.routers import choices_router, questions_router
from fastapi import FastAPI, APIRouter, Query, Depends
from fastapi.responses import JSONResponse
router = APIRouter()
fastapp = FastAPI(root_path=os.getenv("API_BASE_PATH", ""))
fastapp.include_router(questions_router, tags=["questions"], prefix="/question")
fastapp.include_router(choices_router, tags=["choices"], prefix="/choice")

if settings.MOUNT_DJANGO_APP:
    fastapp.mount("/django", application)
    fastapp.mount("/static", StaticFiles(directory="staticfiles"), name="static")

fastapp.include_router(router, prefix="/mysite.asgi")
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#fastapp.mount("/", StaticFiles(directory=f"{PROJECT_ROOT}/staticfiles", html=True), name="front")
fastapp.mount("/", StaticFiles(directory=f"{PROJECT_ROOT}/front_dist", html=True), name="front")

# CORS: https://fastapi.tiangolo.com/tutorial/cors/
fastapp.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(fastapp)
