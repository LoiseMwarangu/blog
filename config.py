
class Config:
    pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig,"testing":TestConfig}

