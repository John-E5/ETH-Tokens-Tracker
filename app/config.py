import os
from dotenv import load_dotenv


class Config:
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    dotenv_path = os.path.join(SITE_ROOT, '.env')
    load_dotenv(dotenv_path)
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_HOST = os.getenv('DB_HOST')
