import os
class Config:
    SECRET_KEY='1234'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST= 'app/static/images'
    SQLALCHEMY_TRACK_MODIFICATIONS ='False'


    #Setting Database location

    
    simpleMDE_JS_IIFE= True
    simpleMDE_USE_CDN= True
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://loise:32123772@localhost/blogpost_test'
          

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://loise:32123772@localhost/blogs'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig,

}
