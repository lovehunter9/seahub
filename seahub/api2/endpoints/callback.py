from rest_framework.response import Response
from rest_framework.views import APIView
import json

from seahub.base.accounts import User


class Callback(APIView):
    def post(self, request, *args, **kwargs):
        # 获取POST请求的数据
        data = json.loads(request.body)

        # 检查事件类型
        event_type = data.get('event')

        if event_type == 'user.create':
            # 获取用户信息
            user_data = data.get('data')
            # new_user_username = user_data.get('name')
            # new_user_role = user_data.get('role')
            new_user_email = user_data.get('email')

            # 创建新用户
            self.create_user(new_user_email)

            # 返回成功响应
            return Response(status=200)

        elif event_type == 'user.delete':
            # 获取用户信息
            user_data = data.get('data')
            deleted_user_email = user_data.get('email')

            # 删除用户
            self.delete_user(deleted_user_email)

            # 返回成功响应
            return Response(status=200)

        # 如果事件类型不是user.create或user.delete，则返回错误响应
        return Response(status=400)

    def create_user(self, username, email):
        # 创建新用户的逻辑
        User.objects.create_user(email=email, password="abcd123456", is_staff=False, is_active=True)
        return

    def delete_user(self, username):
        # 删除用户的逻辑
        User.objects.get(email=username).delete()
        return
