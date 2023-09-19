from rest_framework.response import Response
from rest_framework.views import APIView
import json
import logging

from seahub.base.accounts import User
from seahub.base.templatetags.seahub_tags import email2nickname, email2contact_email


logger = logging.getLogger(__name__)


class CallbackCreate(APIView):
    def post(self, request, *args, **kwargs):
        # 获取POST请求的数据
        data = json.loads(request.body)
        print(data)

        # 获取用户信息
        # user_data = data.get('data')
        new_user_username = data.get('name').strip()
        if new_user_username:
            # new_user_role = user_data.get('role')
            # new_user_email = data.get('email')
            new_user_email = new_user_username + "@seafile.com"

            # 创建新用户
            self.create_user(new_user_email)

        # 返回成功响应
        return Response(status=200)

    def create_user(self, email):
        # 创建新用户的逻辑
        if email2contact_email(email):
            logger.info(f"Contact Email {email} already exist. Ignore this procedure!")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist as e:
            logger.info(e)
            logger.info(f"Email {email} not exist. Will do this procedure!")
            user = None
        if user:
            logger.info(f"Email {email} already exist. Ignore this procedure!")
        else:
            try:
                User.objects.create_user(email=email, password="abcd123456", is_staff=True, is_active=True)
            except Exception as e:
                logger.info(e)
                logger.info(f"Create Email {email} has found it already exist. Ignore this procedure! Beware this causes a virtual user remained.")
        return


class CallbackDelete(APIView):
    def post(self, request, *args, **kwargs):
        # 获取POST请求的数据
        data = json.loads(request.body)
        print(data)

        # 获取用户信息
        # user_data = data.get('data')
        deleted_user_username = data.get('name')
        deleted_user_email = deleted_user_username + "@seafile.com"
        # deleted_user_email = data.get('email')

        # 删除用户
        self.delete_user(deleted_user_email)

        # 返回成功响应
        return Response(status=200)

    def delete_user(self, email):
        # 删除用户的逻辑
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist as e:
            logger.info(e)
            user = None
        if not user:
            logger.info(f"Email {email} not existed. Ignore this procedure!")
        else:
            user.delete()
        return
