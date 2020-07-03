from flask_caching import Cache
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# ext 负责第三方库的初始化

db = SQLAlchemy()
migrate = Migrate()
# 迁移同步生成数据库
cache = Cache(config={
    "CACHE_DEFAULT_TIMEOUT": 24*3600,
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_HOST": "118.25.145.182",
    "CACHE_REDIS_PORT": "6379",
    "CACHE_REDIS_PASSWORD": "tianrandai1995",
    "CACHE_REDIS_DB": "6"
})


def init_ext(app):  # 随用随导

    db.init_app(app)

    cache.init_app(app)

    migrate.init_app(app,db)
    # app.app_context().push()
    # 将app与数据库绑定







