# from rest_framework import serializers
# from datetime import datetime
# from datetime import timedelta
# from rest_framework.validators import UniqueValidator
# from .models import VerifyCode, UserModel
# from blogs.models import Article
# from rest_framework.response import Response



# class EmailSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=20, help_text='用户邮箱')

#     def validate_email(self, email):
#         """
#         验证邮箱是否合法
#         :param data:
#         :return:
#         """

#         # 邮箱是否注册
#         if UserModel.objects.filter(email=email).count():
#             raise serializers.ValidationError("用户已经存在")

#         # 验证邮箱号码是否合法，写在前端
#         # if not re.match(REGEX_MOBILE, email):
#         #     raise serializers.ValidationError("手机号码非法")

#         # 验证码发送频率
#         one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
#         if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, email=email).count():
#             raise serializers.ValidationError("距离上一次发送未超过60s")

#         return email


# class UserRegSerializer(serializers.ModelSerializer):
#     code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
#                                  error_messages={
#                                      "blank": "请输入验证码",
#                                      "required": "请输入验证码",
#                                      "max_length": "验证码格式错误",
#                                      "min_length": "验证码格式错误"
#                                  },
#                                  help_text="验证码")
#     username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
#                                      validators=[UniqueValidator(queryset=UserModel.objects.all(), message="用户已经存在")])

#     email = serializers.CharField(label="电子邮箱", help_text="电子邮箱", required=True, allow_blank=False,
#                                      validators=[UniqueValidator(queryset=UserModel.objects.all(), message="此邮箱已经注册过啦，您老还是换一个吧。")])


#     password = serializers.CharField(
#         style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
#     )
#     # 密码储存前使用 django 自带的 user 类的加密方法加密
#     def create(self, validated_data):
#         user = super(UserRegSerializer, self).create(validated_data=validated_data)
#         user.set_password(validated_data["password"])
#         user.save()
#         return user

#     def validate_code(self, code):
#         verify_records = VerifyCode.objects.filter(email=self.initial_data["email"]).order_by("-add_time")
#         print(self.initial_data["email"])
#         if verify_records:
#             last_record = verify_records[0]
#             five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
#             print(five_mintes_ago)
#             # time_to_offset_naive = last_record.add_time.replace(tzinfo=None)
#             # print(time_to_offset_naive)
#             print(datetime.now)
#             if five_mintes_ago > last_record.add_time:
#                 raise serializers.ValidationError("验证码过期")
#             if last_record.code != code:
#                 raise serializers.ValidationError("验证码错误")
#         else:
#             raise serializers.ValidationError("验证码错误")
#         # try:
#         #     verify_records = VerifyCode.objects.get(mobile=self.initial_data["username"], code=code)
#         # except VerifyCode.DoesNotExist as e:
#         #     pass
#         # except VerifyCode.MultipleObjectsReturned as e:
#         #     pass

#     def validate(self, attrs):
#         # attrs["email"] = attrs["username"]
#         del attrs["code"]
#         return attrs

#     class Meta:
#         model = UserModel
#         fields = ("username", "code", "email", "password")


# class UserBlogSerializer(serializers.ModelSerializer):
#     author = serializers.SerializerMethodField()
#     def get_author(self, row):
#         ret = {'name': str(row.author.name), 'avatar': str(row.author.avatar)}
#         return ret

#     class Meta:
#         model = Article
#         fields = ("title", "body", "tags", "author")
#         depth = 1


# class UserDetailSerializer(serializers.ModelSerializer):
#     """
#     用户详情序列化类
#     """
#     like_articles = serializers.SerializerMethodField()
#     def get_like_articles(self, row):
#         # ret = str(row.favors_a.all())
#         ret = (row.favors.all())
#         retx = [i.articles for i in ret]
#         ser = UserBlogSerializer(instance=retx, many=True)
#         return ser.data

#     my_article = serializers.SerializerMethodField()
#     def get_my_article(self, row):
#         ret = row.myarticles.all()
#         ser = UserBlogSerializer(instance=ret, many=True)
#         # return Response(ser.data)
#         return ser.data


#     article_viewed = serializers.SerializerMethodField()
#     def get_article_viewed(self, row):
#         ret = sum([i.views for i in row.myarticles.all()])
#         return ret

#     class Meta:
#         model = UserModel
#         fields = ("name", "username", "avatar", "email", "date_joined", "birth_date", "user_dsc", "user_state", "like_articles", "my_article", "article_viewed")
