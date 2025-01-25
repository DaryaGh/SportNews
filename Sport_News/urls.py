from django.urls import path
# from .views import News_list , News_detail ,Media_list, PhotoGallery_list, Media_detail,PhotoGallery_detail, podcast_detail, podcast_list, contact_list, contact_detail, newspaper_list, newspaper_detail,advertising_list,News_Create,Media_Create,Podcast_Create,PhotoGallery_Create,News_cancel,Change_mode,Home
from .import views
urlpatterns = [
    path('PhotoGallery', views.PhotoGallery_list, name='PhotoGallery_sport'),
    path('PhotoGallery/<int:photogallery_id>', views.PhotoGallery_detail, name='PhotoGallery_detail'),
    path('PhotoGallery/cat/<int:cat_id>', views.PhotoGallery_list, name='PhotoGallery_sport'),
    path('PhotoGallery/Create' , views.PhotoGallery_Create, name='PhotoGallery_Create'),
    path('Media', views.Media_list, name='Media_list'),
    path('Media/<int:media_id>', views.Media_detail, name='Media_detail'),
    path('Media/cat/<int:cat_id>', views.Media_list, name='Media_list_by_cat'),
    path('Media/Create' , views.Media_Create , name='Media_Create'),
    path('podcast', views.podcast_list, name='podcast_list'),
    path('podcast/<int:podcast_id>', views.podcast_detail, name='podcast_detail'),
    path('podcast/cat/<int:cat_id>', views.podcast_list, name='podcast_list'),
    path('Podcast/Create' , views.Podcast_Create , name='Podcast_Create'),
    path('ContactUs', views.contact_list, name='contact_list'),
    path('ContactUs/<int:contact_id>', views.contact_detail, name='contact_detail'),
    path('NewsPaper', views.newspaper_list, name='newspaper_list'),
    path('NewsPaper/<int:newspaper_id>', views.newspaper_detail, name='newspaper_detail'),
    path('Advertising', views.advertising_list, name='advertising_list'),
    path('News', views.News_list , name='News_list'),
    path('News/<int:news_id>' , views.News_detail , name='News_detail'),
    path('News/cat/<int:cat_id>' , views.News_list , name='News_list_by_cat'),
    path('News/Create', views.News_Create, name='News_Create'),
    path('News/Cancel' , views.News_cancel , name='Cancel_Search'),
    path('Change/mode' , views.Change_mode , name='Change_mode'),
    path('Home', views.Home , name='Home'),
    path('register_Jorm', views.register_Jorm , name='register_Jorm'),


    # url for APIS
    path('Api/Newss', views.Newss_Api , name='Newss_Api'),
path('Api/News/<int:id>', views.News_Api , name='News_Api'),
]
