from rest_framework import serializers

from blog.models import Article


class UserSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    first_name = serializers.CharField(max_length=12)
    password = serializers.CharField(max_length=100)


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

    def validate_title(self, value):
        if value == "fuck" or "fuc" or "fuk" or "mf" or "bich":
            raise serializers.ValidationError('You Cant use bad title')
        return value
