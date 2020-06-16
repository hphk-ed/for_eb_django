from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created', 'updated']
