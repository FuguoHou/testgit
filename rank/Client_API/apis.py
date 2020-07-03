from flask_restful import Api

from Client_API.views import ClientResource
client_api = Api()

client_api.add_resource(ClientResource,"/client_msg/")








