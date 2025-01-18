from django import forms
from Sport_News.models import News, Media, Podcast , PhotoGallery , FileUpload

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title' , 'body']

class MediaForm(forms.ModelForm):

    class Meta:
        model = Media
        fields = ['title' , 'body']

class PodcastForm(forms.ModelForm):

    class Meta:
        model = Podcast
        fields = ['title' , 'body']

class PhotoGalleryForm(forms.ModelForm):

    class Meta:
        model = PhotoGallery
        fields = ['title' , 'body']


class FileUploadForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        fields = ('title', 'files')
