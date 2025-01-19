from django.core.paginator import Paginator
from django.shortcuts import render , redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import NewsPaper, Podcast, News, Media, PhotoGallery, ContactUs, Advertising, Comment, Category, Slider,FileUpload,ReportingAViolation
from .forms import NewsForm, MediaForm, PodcastForm , PhotoGalleryForm ,FileUploadForm
from django.urls import reverse
from django.db.models import Q

def advertising_list(request):
    advertisings = Advertising.objects.filter(id__range=(2,4)).values()

    if 'mode' not in request.session:
        request.session['mode'] ='dark'
        mode = request.session['mode']
    else :
        mode = request.session['mode']

    return render(request, 'advertising.html', {'all_advertising': advertisings ,'mode':mode})

def Media_list(request , cat_id=None):
    request.session["page_route_name"] = "Media_list"
    if cat_id:
        medias = Media.objects.filter(is_active=True).filter(Category = cat_id).order_by('-published_at')
    else:
        medias = Media.objects.filter(is_active=True).order_by('-published_at')

    if 'mode' not in request.session:
        request.session['mode'] ='dark'
        mode = request.session['mode']
    else :
        mode = request.session['mode']

    categories = Category.objects.all()

    return render(request, 'medias.html',context={'medias':medias , 'mode':mode , 'categories': categories})

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

        return render(request, 'media.html', context={'media':media,'all_comments':comments , 'mode':mode})

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
        return render(request , 'Media_Create.html' , context={'form':form})

def PhotoGallery_list(request , cat_id=None):
    if cat_id:
        photogallery =PhotoGallery.objects.filter(is_active=True).filter(Category = cat_id).order_by('-published_at')
    else:
        photogallery =PhotoGallery.objects.filter(is_active=True).order_by('-published_at')

    if 'mode' not in request.session:
        request.session['mode'] ='dark'
        mode = request.session['mode']
    else :
        mode = request.session['mode']

    return render(request, 'photogallery.html', context={'photogallery':photogallery , 'mode':mode })

def PhotoGallery_detail(request, photogallery_id):

    photogallery = PhotoGallery.objects.filter(pk=photogallery_id).first()
    comments = (Comment.objects
                .filter(photogallery = photogallery_id)
                .order_by('created_date'))

    sliders = Slider.objects.all()

    if 'mode' not in request.session:
        request.session['mode'] ='dark'
        mode = request.session['mode']
    else :
        mode = request.session['mode']

    return render(request,'photogallerie.html',context={'all_photo__gallery':photogallery,'all_comments':comments , 'sliders':sliders , 'mode':mode })

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
        return render(request , 'PhotoGallery_Create.html' , context={'form':form})

def podcast_list(request , cat_id=None):
    if cat_id:
        podcasts = Podcast.objects.filter(is_approved=True).filter(Category = cat_id)
    else:
        podcasts = Podcast.objects.all().order_by('-published_at')

    if 'mode' not in request.session:
        request.session['mode'] ='dark'
        mode = request.session['mode']
    else :
        mode = request.session['mode']

    return render (request , 'Podcasts.html' , context={'podcasts':podcasts , 'mode':mode})

def podcast_detail(request, podcast_id):
    podcast = Podcast.objects.filter(pk=podcast_id).first()
    comments = (Comment.objects.filter(podcast = podcast_id))

    if 'mode' not in request.session:
        request.session['mode'] ='dark'
        mode = request.session['mode']
    else :
        mode = request.session['mode']

    return render(request,'podcastss.html' , context={'podcast':podcast,'all_comments':comments , 'mode':mode})

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
        return render(request , 'Podcast_Create.html' , context={'form':form})

def contact_list(request):
    contacts = ContactUs.objects.all()

    if 'mode' not in request.session:
        request.session['mode'] ='dark'
        mode = request.session['mode']
    else :
        mode = request.session['mode']

    return render(request,'contactus.html',context={'contacts':contacts , 'mode':mode})

def contact_detail(request , contact_id):
    contact = ContactUs.objects.filter(pk=contact_id).first()

    if 'mode' not in request.session:
        request.session['mode'] ='dark'
        mode = request.session['mode']
    else :
        mode = request.session['mode']

    return render(request,'contactuss.html',context={'contact':contact , 'mode':mode})

def newspaper_list(request):
    newspapers = NewsPaper.objects.all()[1:]

    if 'mode' not in request.session:
        request.session['mode'] ='dark'
        mode = request.session['mode']
    else :
        mode = request.session['mode']

    return render(request,'newspaper.html',context={'all_newspapers':newspapers , 'mode':mode})

def newspaper_detail(request , newspaper_id):
    newspaper = NewsPaper.objects.filter(pk=newspaper_id).first()

    if 'mode' not in request.session:
        request.session['mode'] ='dark'
        mode = request.session['mode']
    else :
        mode = request.session['mode']

    return render(request , 'newspapers.html' ,context={'newspaper':newspaper , 'mode':mode})

def News_list(request , cat_id=None):

    if request.method =='POST':
        if request.POST['q'] != "":
            q = request.POST['q']
            print(News.objects.filter(is_approved=True)
                  .filter(title__icontains = q)
                  .order_by('-id'))

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('auth_login'))

    request.session["page_route_name"] = "News_list"

    query = request.GET.get('query',None)

    if 'mode' not in request.session:
        request.session['mode'] ='dark'
        mode = request.session['mode']
    else :
        mode = request.session['mode']

    if cat_id:
        newss = News.objects.filter(is_approved=True).filter(Category = cat_id).order_by('-id')
    elif query:
        request.session['query'] = query
        q = Q(title__icontains= query) | Q(body__icontains= query)
        newss = News.objects.filter(q).order_by('-id')
    elif 'query' in request.session and request.session['query'] is not None:
        old_query = request.session['query']
        q = Q(title__icontains= old_query) | Q(body__icontains= old_query)
        newss = News.objects.filter(q).order_by('-id')
    else:
        newss = News.objects.filter(is_approved=True).order_by('-id')

    categories = Category.objects.all()

    paginator = Paginator(newss, 3)
    # print(news.count)
    # print(news.num_pages)
    #print(news.page(3))
    page_number = request.GET.get('p',1)
    news_with_pagination = paginator.get_page(page_number)
    return render (request , 'Newss.html' , context={'newss':news_with_pagination , 'categories':categories , 'mode':mode})

def News_cancel(request):
    if 'query' in request.session and request.session['query'] is not None:
        del request.session['query']
    return HttpResponseRedirect(reverse('News_list'))

def News_detail(request , news_id):
    news = News.objects.filter(pk=news_id).first()
    comments = (Comment.objects
                .filter(news = news_id)
                .filter(parent_id__isnull=True)
                .filter(status='PF')
                .order_by('-created_date'))


    for comment in comments:
        children = (Comment.objects
                .filter(parent_id = comment.id)
                .filter(status='PF')
                .order_by('-created_date'))

        comment['children'] = children

    tags =news.tags.all()

    jorms ={
        'IN', 'Insult'
        'PO', 'Political'
        'SP', 'Spam'
        'VW', 'Vulgar Words'
     }

    if 'mode' not in request.session:
        request.session['mode'] ='dark'
        mode = request.session['mode']
    else :
        mode = request.session['mode']

    return render(request , 'News.html' , context={'news':news,'all_comments':comments ,'tags':tags ,'mode':mode, 'Jorms':jorms })

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
        return render(request , 'News_Create.html' , context={'form':form})

def Home(request):
    request.session["page_route_name"] = "Home"
    return HttpResponse(' Hi Dear '
                        'Thank You your welcome to my site '
                        'I Hope so enjoy visit my site ')

def Change_mode(request):
    if 'mode' in request.session:
        if request.session.get('mode') == 'dark':
            request.session['mode'] = 'light'
        else :
            request.session['mode'] = 'dark'
    else:
        request.session['mode'] = 'dark'

    page = request.session.get('page_route_name','Home')
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

def register_Jorm (request):
    if request.method == "POST":
        print(request)
    return HttpResponse('save')

