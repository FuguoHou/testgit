from flask import Flask

from FlaskAPI.ext import init_ext
from FlaskAPI.settings import envs
from FlaskAPI.urls import init_apis


def create_app(env):
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(envs.get(env))
    # app.host='0.0.0.0'
    # 初始化第三方扩展库 除去路由
    init_ext(app)
    # 初始化路由
    init_apis(app)

    return app