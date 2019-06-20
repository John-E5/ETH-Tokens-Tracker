import os
from dotenv import load_dotenv


class Config:
    """ Load env vars and app config """

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    dotenv_path = os.path.join(SITE_ROOT, '.env')
    load_dotenv(dotenv_path)
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
