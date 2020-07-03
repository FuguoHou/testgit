

def get_db_uri(dbinfo):
    backends = dbinfo.get("BACKENDS")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")
    # pool_size = 100

    return "{}+{}://{}:{}@{}:{}/{}".format(backends, driver, user, password, host, port, name)
    # 数据库+驱动+用户+密码+主机+端口+数据库

class Config:

    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):  # 在继承基类的前提对不同环境做细节修改

    DEBUG = True

    dbinfo = {
        "BACKENDS": "mysql",
        "DRIVER": "pymysql",
        "USER": "test00",
        "PASSWORD": "houxiaohuo",
        "HOST": "118.25.145.182",
        "PORT": "3306",
        "NAME": "test00",
        "CHARSET": "UTF-8"
    }


    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_RECYCLE = 30

class TestingConfig(Config):

    TESTING = True


class StagingConfig(Config):

    pass


class ProductConfig(Config):

    pass


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": ProductConfig
}

