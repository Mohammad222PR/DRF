from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers

from blog.models import Article, Comment


class UserSerializers(serializers.ModelSerializer):
    articles = serializers.SlugRelatedField(read_only=True, slug_field='title', many=True, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "last_name", "articles")


class CommentSerializers(serializers.ModelSerializer):
    days_ago = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"

    def get_days_ago(self, obj):
        return (now().date() - obj.created).days


class ArticleSerializers(serializers.ModelSerializer):
    comments = CommentSerializers(many=True, required=False)
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    tag = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = "__all__"

    def validate_title(self, value):
        if value == "fuck":
            raise serializers.ValidationError('You Cant use bad title')
        else:
            return value

    # def get_comments(self, obj):
    #     serializer = CommentSerializers(instance=obj.comments.all(), many=True)
    #     return serializer.data

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user
        return Article.objects.create(**validated_data)
