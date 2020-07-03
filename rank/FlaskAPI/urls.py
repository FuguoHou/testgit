from flask_cors import CORS

from Client_API.apis import client_api



def init_apis(app):
    CORS(app, supports_credentials=True)  # 跨域
    client_api.init_app(app)

