import os

from flask_script import Manager

from FlaskAPI import create_app

# 从环境中获取 运行配置信息
# env = os.environ.get("FLASK_ENV") or "default"
env = "develop"

app = create_app(env)
app.app_context().push()
manager = Manager(app)
# manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()


# python manage.py runserver -h 0.0.0.0 -p 9527 --threaded