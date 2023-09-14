from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from rest_framework.authentication import TokenAuthentication
from .models import Article, Comment
from .serializers import UserSerializers, ArticleSerializers, CommentSerializers
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserOrReadOnly

# Create your views here.


URL = "https://api.binance.com/api/v3/triker/price?symbol=BTCUSDT"


@api_view(['GET', 'POST'])
def home(request):
    products = [
        {'name': 'iphone',
         'price': 1233333},
        {'name': 'laptop',
         'price': '10000000'}
    ]
    return Response(products)


class Home(APIView):
    def get(self, request):
        products = [
            {'name': 'iphone',
             'price': 1233333},
            {'name': 'laptop',
             'price': '10000000'}
        ]
        return Response(products)

    def post(self, request):
        return Response({'product': 'hello'})


class ArticleView(APIView):
    def get(self, request):
        queryset = Article.objects.all()
        ser = ArticleSerializers(instance=queryset, many=True)
        return Response(data=[ser.data], status=status.HTTP_200_OK)


class ArticleDetailView(APIView):
    def get(self, request, slug):
        instance = Article.objects.get(slug=slug)
        ser = ArticleSerializers(instance=instance)
        return Response(data=[ser.data], status=status.HTTP_200_OK)


class AddArticleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ArticleSerializers(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Done"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleUpdateView(APIView):
    permission_classes = [IsUserOrReadOnly]

    def put(self, request, pk):
        instance = Article.objects.get(id=pk)
        self.check_object_permissions(request, instance)
        serializer = ArticleSerializers(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = Article.objects.get(id=pk)
        self.check_object_permissions(request, instance)
        instance.delete()
        return Response({"response": "Deleted"}, status=status.HTTP_200_OK)


class CheckToken(APIView):
    def get(self, request):
        user = request.user
        return Response({'user': user.username}, status=status.HTTP_200_OK)


class GetArticlesCommentView(APIView):
    def get(self, request, pk):
        comments = Article.objects.get(id=pk).comments.all()
        ser = CommentSerializers(instance=comments, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
