from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import ArticleSerializer
from .models import Article


@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    
    serializer = ArticleSerializer(articles, many=True)
    # context = {
    #     'serializer': serializer.data
    # }
    # return JsonResponse(context)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    # print(request.data)

    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        a = serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
