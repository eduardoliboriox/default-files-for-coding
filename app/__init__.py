from flask import Flask
from app.config import Config
from app.routes.pages import pages_bp
from app.routes.api import api_bp
from app.extensions import get_db

