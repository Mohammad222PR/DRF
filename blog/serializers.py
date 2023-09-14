from django.utils.timezone import now
from rest_framework import serializers

from blog.models import Article, Comment


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
        if value == "fuck":
            raise serializers.ValidationError('You Cant use bad title')
        else:
            return value

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user
        return Article.objects.create(**validated_data)


class CommentSerializers(serializers.ModelSerializer):
    days_ago = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"

    def get_days_ago(self, obj):
        return (now().date() - obj.created).days
