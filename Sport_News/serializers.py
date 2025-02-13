from datetime import datetime as dt
from rest_framework import serializers
# from Sport_News.models import Category , News
from Sport_News.models import *


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

    class Meta:
        model = Category
        fields = ('id', 'title')


# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     # class Meta:
#     #     model = Category
#     #     fields = ('id', 'title')

class NewsSerializer(serializers.ModelSerializer):
    tags_count = serializers.SerializerMethodField()
    Category = serializers.StringRelatedField()

    # count_like = serializers.SerializerMethodField()

    class Meta:
        model = News
        # fields = ['title','like_count','dislike_count','Category','avg_like_count']
        fields = ['id', 'title', 'body', 'like_count', 'dislike_count', 'avg_like_count', 'Category', 'tags',
                  'tags_count']
        # در سورس اصلی تغییر کند
        # fields = ['id', 'title', 'body', 'count_like', 'dislike_count', 'avg_like_count', 'Category', 'tags', 'tags_count']

    # Category = CategorySerializer()

    # def get_count_like(self, obj : News):
    #     return obj.like_count

    avg_like_count = serializers.SerializerMethodField('get_avg_like_count')

    def get_avg_like_count(self, obj: News):
        if obj.like_count is None or obj.dislike_count is None:
            return 0
        return (obj.like_count + obj.dislike_count) / 2

    def get_tags_count(self, obj: News):
        return obj.tags.count()

    def create(self, validated_data):
        validated_data['published_at'] = dt.now()
        return super().create(validated_data)

# class NewsSerializer(serializers.Serializer):
# id = serializers.IntegerField()
# title = serializers.CharField(max_length=200)
# body = serializers.CharField(max_length=1024)
# news_type = serializers.CharField(max_length=200)
# like_count = serializers.IntegerField()
# dislike_count = serializers.IntegerField()
# Category_id = serializers.IntegerField()
# Category = serializers.StringRelatedField()
# Category = CategorySerializer()

# avg_like_count = serializers.SerializerMethodField('get_avg_like_count')
#
# def get_avg_like_count(self, obj : News):
#     if obj.like_count is None or obj.dislike_count is None:
#         return 0
#     return (obj.like_count + obj.dislike_count) / 2

# Category = serializers.PrimaryKeyRelatedField(
#     queryset = Category.objects.all(),
#     serializer = CategorySerializer,
# )
