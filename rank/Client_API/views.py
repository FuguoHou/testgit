from flask import request
from flask_restful import Resource
from Client_API.models import Client_Model


class ClientResource(Resource):

    def post(self):
        """
        如需功能扩展则在下面加入action即可

        """
        action = request.args.get("action")
        if action == "send_grade":
            return self.send_grade()
        elif action == "search_grade":
            return self.search_grade()
        else:
            return {"errorcode": 0, "error": "error action"}

    def send_grade(self):
        """
        接口1：上传客户端号和分数
        若已存在更新分数

        """

        # ip = request.remote_addr
        try:
            client_number = request.form.get("client_number")  # 客户端编号/ip皆可 string类型
            member_grade = request.form.get("member_grade")  # 客户端的分数，要求为小于10000000的int

            if member_grade >=10000000:
                return {"errorcode":0, "error":"数值过大，怀疑开挂！"}

            user = Client_Model.query.filter(Client_Model.client_number==client_number,Client_Model.flag_0==1).first()

            if user:
                user.member_grade = member_grade
                user.save()
            else:
                user = Client_Model()
                user.client_number = client_number
                user.member_grade = member_grade
                user.save()

            return "ok"
        except Exception as e:
            print(e)
            return {"errorcode": 0, "error": "接口返回失败"}

    def search_grade(self):
        """
        查询接口
        根据输入范围返回对应的排名，名字，分数以及此客户端对应信息
        """
        try:
            data = {"ranks":{}}
            start_search = int(request.form.get("start_number"))-1  # 查询开始位数（>=0,默认传0）
            end_search = int(request.form.get("end_number"))  # 查询结束位数（>=0,默认传0，想查所有就俩参数都传0）
            client_number = request.form.get("client_number")  # 客户端编号/ip皆可 string类型

            if start_search <= 1:
                start_search = 0
            if end_search <= 0:
                end_search = None

            user = Client_Model.query.filter(Client_Model.client_number == client_number,Client_Model.flag_0==1).first()

            users = Client_Model.query.filter(Client_Model.flag_0==1).all()
            rank = 0
            for user in users[start_search:end_search]:
                rank += 1
                data["ranks"][rank] = {('客户端'+user.client_number):user.member_grade}
            if user:
                data["user_rank"] = {users.index(user)+1:{('客户端'+user.client_number):user.member_grade}}
            else:
                data["user_rank"]={"查无此客户端信息，请重新确认"}
            return data
        except Exception as e:
            print(e)
            return {"errorcode": 0, "error": "接口返回失败"}

















