# from rest_framework import viewsets
# from rest_framework import mixins
# # Create your views here.
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from .models import favor_article
# from users import models
# from .serializers import UserFavorsSerializers, CreateImageSerializer
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated

# import json
# import requests
# import datetime

# import requests
# # import lxml
# from lxml import etree

# class UserFavorsViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
#     """
#     retrieve:
#     查看某一条收藏记录。
#     articles_id：文章收藏记录表数据的id

#     list:
#     查看所有收藏记录

#     create:
#     新建一条收藏记录
#     articles_id：文章收藏记录表数据的id
#     delete:
#     删除一条收藏记录
#     articles_id：文章收藏记录表数据的id
#     """
#     serializer_class = UserFavorsSerializers
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
#     lookup_field = "articles_id"

#     def get_queryset(self):
#         return favor_article.objects.filter(user=self.request.user)


# class ApiLaohuangliView(APIView):
#     """
#     老黄历接口
#     """

#     def get(self, request):
#         # print(request.get_full_path())
#         # print(request.path)
#         format_today = datetime.date.today()
#         # print(format_today)
#         url = 'http://v.juhe.cn/laohuangli/d?date=' + str(format_today) + '&key=6dafce8786d51b9598c1127f1061a25c'
#         try:
#             result = requests.get(url, timeout=1)
#             data = json.loads(result.content)
#             return Response(data)
#         except:
#             data = {'未显示': '接口去旅游了'}
#             return Response(data)

# class ConstellationView(APIView):
#     """
#     星座运势接口
#     """
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
#     def get(self, request):
#         # print(request.user.id)
#         user_birth = models.UserModel.objects.get(id=request.user.id).birth_date
#         if user_birth:
#             month_day = str(user_birth)[5:10].split('-')
#             # print(month_day[0][0])
#             if month_day[0][0] == '0':
#                 month = int(month_day[0][1])
#             else:
#                 month = int(month_day[0])

#             if month_day[1][0] == '0':
#                 day = int(month_day[1][1])
#             else:
#                 day = int(month_day[1])

#             zodiac_name = ['摩羯座','水瓶座','双鱼座','白羊座','金牛座', '双子座', '巨蟹座','狮子座',
#                             '处女座','天秤座','天蝎座','射手座']
#             zodiac_date = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23),
#                            (9, 23), (10, 23), (11, 23), (12, 23))
#             user_consName = zodiac_name[len(list(filter(lambda x: x < (month, day), zodiac_date))) % 12]
#             print(user_consName)
#             # user_consName = u_zodiac_name
#             key = 'fca134b8d0bfb21a671350266cbdc1fd'
#             url = 'http://web.juhe.cn:8080/constellation/getAll?consName=' + user_consName + '&type=today&key=' + key
#             try:
#                 result = requests.get(url, timeout=1)
#                 data = json.loads(result.content)
#                 return Response(data)

#             except:
#                 data = {'未获取到信息': '接口出了点小问题'}
#                 return Response(data)
#         else:
#             return Response({'msg':'快去在编辑个人资料里设置自己的生日吧！'})



# # class CreateImageViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
# class CreateImageViewset(viewsets.ModelViewSet):
#     """
#     头像修改
#     """
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
#     serializer_class = CreateImageSerializer
#     queryset = models.UserModel.objects.all()


# class HotTrendsView(APIView):
#     """
#     热搜数据爬取
#     """
#     def get(self, request):
#         try:
#             res = requests.get('https://s.weibo.com/top/summary?Refer=top_hot')
#             # print(res.text)
#             xhtml = etree.HTML(res.text)
#             # result = etree.tostring(xhtml, encoding='utf-8')
#             result_text = xhtml.xpath("//td[@class='td-02']/a/text()")
#             result_href = xhtml.xpath("//td[@class='td-02']/a/@href")
#             # dict(zip())
#             data = {
#                 'text': result_text,
#                 'link': ['https://s.weibo.com/'+ i for i in result_href]
#             }   
#             return Response(data)
#         except:
#             data = {'未显示': '为爬取到数据'}
#             return Response(data)

