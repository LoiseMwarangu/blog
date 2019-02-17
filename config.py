import os
class Config:
    QUOTES_API_BASE_URL='http://quotes.stormconsultancy.co.uk/quotes/{}'
    QUOTES_API_KEY = os.environ.get('QUOTES_API_KEY') 
    SECRET_KEY = os.environ.get('SECRET KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    #Setting Database location
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://loise:32123772@localhost/blogs'
    
     
class ProdConfig(Config):
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
     

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}