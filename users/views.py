from django.shortcuts import render

# Create your views here.
from random import choice

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import serializers, authentication, permissions
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets, mixins
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import EmailSerializer, UserRegSerializer, UserDetailSerializer
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import send_mail
# User = get_user_model()
from .models import UserModel, VerifyCode
from pepsicola import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

def jwt_response_payload_handler(token, user=None, request=None):
    """
    设置返回的 token 和附加 user 信息
    :param token:
    :param user:
    :param request:
    :return:
    """
    return {
        'token': token,
        'user': UserDetailSerializer(user, context={'request': request}).data
    }

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class EmailCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送邮件验证码
    """
    serializer_class = EmailSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = "1234567890yuhaoze"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        code = self.generate_code()

        subject = 'YuY注册激活码'
        message = '你的激活码是：<h1>%s</h1>' % code
        sender = settings.EMAIL_FROM
        receiver = [email]
        try:
            send_mail(subject, message, sender, receiver)
        # if sms_status["code"] != 1:
        #     return Response({
        #         "email": sms_status["msg"]
        #     }, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     code_record = VerifyCode(code=code, email=email)
        #     code_record.save()
        #     return Response({
        #         "email": email
        #     }, status=status.HTTP_201_CREATED)
            code_record = VerifyCode(code=code, email=email)
            code_record.save()
            return Response({"email": email}, status=status.HTTP_201_CREATED)
        except:
            return Response({"email": email}, status=status.HTTP_400_BAD_REQUEST)


# class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
class UserViewset(viewsets.ModelViewSet):
    """
    retrieve:
    查看某一个用户的信息。

    list:
    查看所有用户信息

    create:
    新增一条用户信息

    update:
    更新用户信息

    partial_update:
    局部更新用户信息

    delete:
    删除一条用户信息
    """
    serializer_class = UserRegSerializer
    queryset = UserModel.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer

        return UserDetailSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []

        return []

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = self.perform_create(serializer)
    #
    #     re_dict = serializer.data
    #     payload = jwt_payload_handler(user)
    #     re_dict["token"] = jwt_encode_handler(payload)
    #     re_dict["name"] = user.name if user.name else user.username
    #
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    # def perform_create(self, serializer):
    #     return serializer.save()