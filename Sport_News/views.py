from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.template.defaultfilters import title
from pyexpat.errors import messages
from rest_framework.decorators import api_view
from rest_framework.views import APIView, Response
from rest_framework import status
from . import serializers
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

def advertising_list(request):
    advertisings = Advertising.objects.filter(id__range=(2, 4)).values()

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    return render(request, 'advertising.html', {'all_advertising': advertisings, 'mode': mode})


def Media_list(request, cat_id=None):
    request.session["page_route_name"] = "Media_list"

    medias = Media.objects.filter(is_active=True)

    if request.method == 'POST':
        cat = request.POST.get('search_by_cat', None)
        # print(request.POST)
        # print(request.POST['q'])
        if cat is not None and len(cat) > 0:
            # cat = request.POST.get('search_by_cat')
            medias = medias.filter(Category=cat)
            # print(medias)
            request.session['search_by_cat'] = int(cat)

        else:
            if request.session.get('search_by_cat', None) is not None:
                del request.session['search_by_cat']




        user = request.POST.get('search_by_user', None)

        if user is not None and len(user) > 0:
            # cat = request.POST.get('search_by_cat')
            medias = medias.filter(createdUsers=user)
            # print(medias)
            request.session['search_by_user'] = int(user)

        else:
            if request.session.get('search_by_user', None) is not None:
                del request.session['search_by_user']





        if request.POST.get('q', None) is not None:
            q = request.POST.get('q')
            medias = medias.filter(title__icontains=q)
            request.session['q'] = q

        else:
            if request.session.get('q', None) is not None:
                del request.session['q']



    if cat_id:
        medias = medias.filter(Category=cat_id)

    # if cat_id:
    #     medias = Media.objects.filter(is_active=True).filter(Category=cat_id).order_by('-published_at')
    # else:
    #     medias = Media.objects.filter(is_active=True).order_by('-published_at')

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']


    medias = medias.order_by('-id')

    categories = Category.objects.all().order_by('title')
    users = User.objects.all().order_by('first_name')


    return render(request, 'medias.html', context={'medias': medias, 'mode': mode, 'categories': categories, 'users': users})


def Media_detail(request, media_id):
    media = Media.objects.filter(pk=media_id).first()
    comments = (Comment.objects
                .filter(news=media_id)
                .filter(status='PF')
                .order_by('created_date'))

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    return render(request, 'media.html', context={'media': media, 'all_comments': comments, 'mode': mode})


def Media_Create(request):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            media = form.save(commit=True)
            media.Category_id = 1
            media.save()
            return HttpResponseRedirect(reverse('Media_detail', args=(media.id,)))
        else:
            return HttpResponse('No Valid Form')
    else:
        form = MediaForm()
        return render(request, 'Media_Create.html', context={'form': form})


def Media_cancel(request):

    if 'q' in request.session and request.session['q'] is not None:
        del request.session['q']
    if 'search_by_cat' in request.session and request.session['search_by_cat']:
        del request.session['search_by_cat']

    if 'search_by_user' in request.session and request.session['search_by_user']:
        del request.session['search_by_user']

    return HttpResponseRedirect(reverse('Media_list'))


def PhotoGallery_list(request, cat_id=None):
    if cat_id:
        photogallery = PhotoGallery.objects.filter(is_active=True).filter(Category=cat_id).order_by('-published_at')
    else:
        photogallery = PhotoGallery.objects.filter(is_active=True).order_by('-published_at')

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    return render(request, 'photogallery.html', context={'photogallery': photogallery, 'mode': mode})


def PhotoGallery_detail(request, photogallery_id):
    photogallery = PhotoGallery.objects.filter(pk=photogallery_id).first()
    comments = (Comment.objects
                .filter(photogallery=photogallery_id)
                .order_by('created_date'))

    sliders = Slider.objects.all()

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    return render(request, 'photogallerie.html',
                  context={'all_photo__gallery': photogallery, 'all_comments': comments, 'sliders': sliders,
                           'mode': mode})


def PhotoGallery_Create(request):
    if request.method == 'POST':
        form = PhotoGalleryForm(request.POST)
        if form.is_valid():
            photogallery = form.save(commit=True)
            return HttpResponseRedirect(reverse('PhotoGallery_detail', args=(photogallery.id,)))
        else:
            return HttpResponse('No Valid Form')
    else:
        form = PhotoGalleryForm()
        return render(request, 'PhotoGallery_Create.html', context={'form': form})


def podcast_list(request, cat_id=None):


    podcasts = Podcast.objects.filter(is_approved=True)

    if request.method == 'POST':
        cat = request.POST.get('search_by_cat', None)
        # print(request.POST)
        # print(request.POST['q'])
        if cat is not None and len(cat) > 0:
            # cat = request.POST.get('search_by_cat')
            podcasts = podcasts.filter(Category=cat)
            # print(podcasts)
            request.session['search_by_cat'] = int(cat)

        else:
            if request.session.get('search_by_cat', None) is not None:
                del request.session['search_by_cat']



        user = request.POST.get('search_by_user', None)

        if user is not None and len(user) > 0:
            # cat = request.POST.get('search_by_cat')
            podcasts = podcasts.filter(createdUsers=user)
            # print(podcasts)
            request.session['search_by_user'] = int(user)

        else:
            if request.session.get('search_by_user', None) is not None:
                del request.session['search_by_user']




        if request.POST.get('q', None) is not None:
            q = request.POST.get('q')
            podcasts = podcasts.filter(title__icontains=q)
            request.session['q'] = q

        else:
            if request.session.get('q', None) is not None:
                del request.session['q']

    if cat_id:
        podcasts = podcasts.filter(Category=cat_id)


    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    podcasts = podcasts.order_by('-id')

    categories = Category.objects.all().order_by('title')
    users = User.objects.all().order_by('first_name')

    return render(request, 'podcasts.html',
                  context={'podcasts': podcasts, 'categories': categories, 'users': users, 'mode': mode})


    # if cat_id:
    #     podcasts = Podcast.objects.filter(is_approved=True).filter(Category=cat_id)
    # else:
    #     podcasts = Podcast.objects.all().order_by('-published_at')


def podcast_detail(request, podcast_id):
    podcast = Podcast.objects.filter(pk=podcast_id).first()
    comments = (Comment.objects.filter(podcast=podcast_id))

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    return render(request, 'podcastss.html', context={'podcast': podcast, 'all_comments': comments, 'mode': mode})


def Podcast_Create(request):
    if request.method == 'POST':
        form = PodcastForm(request.POST)
        if form.is_valid():
            podcast = form.save(commit=True)
            return HttpResponseRedirect(reverse('podcast_detail', args=(podcast.id,)))
        else:
            return HttpResponse('No Valid Form')
    else:
        form = PodcastForm()
        return render(request, 'Podcast_Create.html', context={'form': form})


def Podcast_cancel(request):
    if 'q' in request.session and request.session['q'] is not None:
        del request.session['q']
    if 'search_by_cat' in request.session and request.session['search_by_cat']:
        del request.session['search_by_cat']

    if 'search_by_user' in request.session and request.session['search_by_user']:
        del request.session['search_by_user']

    return HttpResponseRedirect(reverse('Podcast_list'))


def contact_list(request):
    contacts = ContactUs.objects.all()

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    return render(request, 'contactus.html', context={'contacts': contacts, 'mode': mode})


def contact_detail(request, contact_id):
    contact = ContactUs.objects.filter(pk=contact_id).first()

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    return render(request, 'contactuss.html', context={'contact': contact, 'mode': mode})


def newspaper_list(request):
    newspapers = NewsPaper.objects.all()[1:]

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    return render(request, 'newspaper.html', context={'all_newspapers': newspapers, 'mode': mode})


def newspaper_detail(request, newspaper_id):
    newspaper = NewsPaper.objects.filter(pk=newspaper_id).first()

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    return render(request, 'newspapers.html', context={'newspaper': newspaper, 'mode': mode})


def News_list(request, cat_id=None):


    newss = News.objects.filter(is_approved=True)

    if request.method == 'POST':
        cat = request.POST.get('search_by_cat', None)
        # print(request.POST)
        # print(request.POST['q'])
        if cat is not None and len(cat) > 0:
            # cat = request.POST.get('search_by_cat')
            newss = newss.filter(Category=cat)
            # print(newss)
            request.session['search_by_cat'] = int(cat)

        else:
            if request.session.get('search_by_cat', None)is not None:
                del request.session['search_by_cat']



        user = request.POST.get('search_by_user', None)

        if user is not None and len(user) > 0:
            # cat = request.POST.get('search_by_cat')
            newss = newss.filter(createdUsers=user)
            # print(newss)
            request.session['search_by_user'] = int(user)

        else:
            if request.session.get('search_by_user', None)is not None:
                del request.session['search_by_user']



        if request.POST.get('q', None) is not None:
            q = request.POST.get('q')
            newss = newss.filter(title__icontains=q)
            request.session['q'] = q

        else:
            if request.session.get('q', None)is not None:
                del request.session['q']


    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('auth_login'))



    request.session["page_route_name"] = "News_list"


    query = request.GET.get('query', None)

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']



    if cat_id:
        newss = newss.filter(Category=cat_id)
        # newss = (News.objects.filter(is_approved=True)
        #          .filter(Category=cat_id)
        #          .order_by('-id'))


    # elif query:
    #     request.session['query'] = query
    #     q = Q(title__icontains=query) | Q(body__icontains=query)
    #     newss = News.objects.filter(q).order_by('-id')
    # elif 'query' in request.session and request.session['query'] is not None:
    #     old_query = request.session['query']
    #     q = Q(title__icontains=old_query) | Q(body__icontains=old_query)
    #     newss = News.objects.filter(q).order_by('-id')
    # else:
    #     newss = (News.objects.filter(is_approved=True)
    #              .order_by('-id'))

    newss = newss.order_by('-id')

    categories = Category.objects.all().order_by('title')
    users = User.objects.all().order_by('first_name')

    paginator = Paginator(newss, 3)
    # print(news.count)
    # print(news.num_pages)
    # print(news.page(3))
    page_number = request.GET.get('p', 1)
    news_with_pagination = paginator.get_page(page_number)
    return render(request, 'Newss.html',
                  context={'newss': news_with_pagination, 'categories': categories, 'mode': mode, 'users': users})


def News_cancel(request):
    # if 'query' in request.session and request.session['query'] is not None:
    #     del request.session['query']
    # return HttpResponseRedirect(reverse('News_list'))

    if 'q' in request.session and request.session['q'] is not None:
        del request.session['q']
    if 'search_by_cat' in request.session and request.session['search_by_cat']:
        del request.session['search_by_cat']

    if 'search_by_user' in request.session and request.session['search_by_user']:
        del request.session['search_by_user']

    return HttpResponseRedirect(reverse('News_list'))


def News_detail(request, news_id):
    news = News.objects.filter(pk=news_id).first()
    comments = (Comment.objects
                .filter(news=news_id)
                .filter(parent_id__isnull=True)
                .filter(status='PF')
                .order_by('-created_date'))

    for comment in comments:
        children = (Comment.objects
                    .filter(parent_id=comment.id)
                    .filter(status='PF')
                    .order_by('-created_date'))

        comment['children'] = children

    tags = news.tags.all()

    jorms = {
        'IN', 'Insult'
              'PO', 'Political'
                    'SP', 'Spam'
                          'VW', 'Vulgar Words'
    }

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    return render(request, 'News.html',
                  context={'news': news, 'all_comments': comments, 'tags': tags, 'mode': mode, 'Jorms': jorms})


def News_Create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=True)
            return HttpResponseRedirect(reverse('News_detail', args=(news.id,)))
        else:
            return HttpResponse('No Valid Form')
    else:
        form = NewsForm()
        return render(request, 'News_Create.html', context={'form': form})


def Home(request):
    request.session["page_route_name"] = "Home"
    return HttpResponse(' Hi Dear '
                        'Thank You your welcome to my site '
                        'I Hope so enjoy visit my site ')


def Change_mode(request):
    if 'mode' in request.session:
        if request.session.get('mode') == 'dark':
            request.session['mode'] = 'light'
        else:
            request.session['mode'] = 'dark'
    else:
        request.session['mode'] = 'dark'

    page = request.session.get('page_route_name', 'Home')
    return HttpResponseRedirect(reverse(page))


def file_upload_view(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')  # Redirect to a success page
    else:
        form = FileUploadForm()

    return render(request, 'file_upload.html', {'form': form})


def handle_multiple_file_uploads(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')

        for file in files:
            new_entry = FileUpload(title=request.POST['title'], files=file)
            new_entry.save()

        return redirect('success_page')
    return render(request, 'multiple_file_upload_form.html')


def register_Jorm(request):
    if request.method == "POST":
        print(request)
    return HttpResponse('save')

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