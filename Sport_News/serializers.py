from rest_framework import serializers
from Sport_News.models import Category , News


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    class Meta:
        model = Category
        fields = ('id', 'title')


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

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title','like_count','dislike_count','Category','avg_like_count']
        fields = ['title', 'like_count', 'dislike_count']

    # Category = CategorySerializer()
    # avg_like_count = serializers.SerializerMethodField('get_avg_like_count')

    # def get_avg_like_count(self, obj : News):
    #     if obj.like_count is None or obj.dislike_count is None:
    #         return 0
    #     return (obj.like_count + obj.dislike_count) / 2