from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

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
        return Response({'product':'hello'})
