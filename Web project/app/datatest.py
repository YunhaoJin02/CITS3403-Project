import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from app import app
from app.extensions import db
from app.models import UserModel

def add_users():
    # 创建用户实例
    user1 = UserModel(username='user1', password='password1', email='user1@example.com')
    user2 = UserModel(username='user2', password='password2', email='user2@example.com')

    # 添加到数据库会话
    db.session.add(user1)
    db.session.add(user2)

    # 提交会话以保存更改到数据库
    db.session.commit()
    print("Users added to the database.")

if __name__ == '__main__':
    with app.app_context():
        add_users()
