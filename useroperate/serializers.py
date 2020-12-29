from rest_framework import serializers
from .models import favor_article
# from blogs.models import Article
from users.models import UserModel
import os

class UserFavorsSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = favor_article
        fields = ("user", "articles", "id")


class CreateImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ("avatar", )

    def create(self, validated_data):
        # file_obj = self.context["request"].data.get("file", None)
        user_obj = UserModel.objects.get(id=self.context["request"].user.id)
        user_obj.avatar = self.context["request"].data.get("file", None)

        # obj = UserModel.objects.filter(id=self.context["request"].user.id).update(
        #     avatar=file_obj
        # )
        user_obj.save()
        return user_obj