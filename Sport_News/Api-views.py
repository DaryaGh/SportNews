from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.template.defaultfilters import title
from pyexpat.errors import messages
from rest_framework.decorators import api_view
from rest_framework.views import APIView, Response
from rest_framework import status
from .import serializers
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view
from .models import NewsPaper, Podcast, News, Media, PhotoGallery, ContactUs, Advertising, Comment, Category, Slider, \
    FileUpload, ReportingAViolation, User
from .forms import NewsForm, MediaForm, PodcastForm, PhotoGalleryForm, FileUploadForm
from django.urls import reverse
from django.db.models import Q
from .serializers import NewsSerializer



# API

@api_view(['GET', 'POST'])
def Newss_Api(request):
    if request.method == "GET":
        newss = (News.objects
                 .select_related('Category')
                 .filter(is_approved=True)
                 .order_by('-published_at'))
        serialized_newss = NewsSerializer(newss, many=True)
        # NewsSerializer()
        return Response(serialized_newss.data)
    elif request.method == 'POST':
        # print(request.data)
        serializer = NewsSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def News_Api(request, id):
    news = get_object_or_404(News, pk=id)

    if request.method == "PUT":
        serializer = NewsSerializer(news, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': 'Update Successfully'
            }, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':


        #check file exist or not
        if news.main_picture is not None :
            return Response({
                'message': 'You have not to delete the main_picture'
            } , status=status.HTTP_405_METHOD_NOT_ALLOWED)



        # tags
        if news.tags.count() > 0:
            return Response({
                'message': 'You have not to delete the tags'
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)



        news.delete()

        return Response({
            'message': ' Deleted Successfully'
        },
            status=status.HTTP_204_NO_CONTENT)

    serialized_news = NewsSerializer(news)
    return Response(serialized_news.data)

# news = News.objects.get(pk=id)
# # print(news)
# serialized_news = NewsSerializer(news)
# return Response(serialized_news.data)
# return HttpResponse(id)


# try :
#     news = News.objects.get(pk=id)
#     serialized_news = NewsSerializer(news)
#     return Response(serialized_news.data)
# except News.DoesNotExist:
#     return  Response(status=404)