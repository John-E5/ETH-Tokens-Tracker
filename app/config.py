import os


class Config:
    SECRET_KEY = 'f5e7522cec73e9e33b8c496a7e073f0d'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
