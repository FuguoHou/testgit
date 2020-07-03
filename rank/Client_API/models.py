from FlaskAPI.ext import db


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            return False
        finally:
            db.session.close()

        return True

class Client_Model(BaseModel):
    __tablename__ = "client_config"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)  # id自增
    client_number = db.Column(db.String(255))  # 客户端编号/ip
    member_grade = db.Column(db.Integer)  # 分数
    flag_0 = db.Column(db.Integer)  # 标志位
    flag_1 = db.Column(db.String(100))
    flag_2 = db.Column(db.String(100))
    flag_3 = db.Column(db.String(100))
    __mapper_args__ = {
        "order_by": member_grade.desc()}




