from django.contrib import admin
from .models import User, Category, News, Comment, Tag, Media, PhotoGallery, Image, ErrorReporting, \
    ReportingAViolation, ContactUs, Podcast, NewsPaper, Advertising, AboutUs, Avatar, MetaAdvertising, MetaContactUs, \
    ReplyAnswer, Role, Slider, ReportingAViolation , Popularity ,FileUpload


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title' , 'status')

class MediaAdmin(admin.ModelAdmin):
    list_display = ('title','like_count','status','is_active','like_counts')
    list_filter = ('Category' , )
    search_fields = ('title' ,)
    list_editable = ('status', 'is_active','like_count')
    list_per_page = 2

    def like_counts(self , media):
        if int(media.like_count) > 5000:
            return 'Good'
        else:
            return 'Bad'

class TagAdmin(admin.ModelAdmin):
    list_display = ('name_tag' ,'visibility' , 'status','is_active')
    list_editable = ('visibility', 'status' , 'is_active')
    list_per_page = 2

class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title' ,'like_count' ,'like_counts','download_count')
    list_editable = ('like_count', 'download_count')
    list_per_page = 2

    def like_counts(self , podcast):
        if int(podcast.like_count) > 50:
            return 'Good'
        else:
            return 'Bad'

class UserAdmin(admin.ModelAdmin):
    list_display = ('nick_name','is_approved','user_type','mobile')
    list_editable = ('is_approved','user_type')
    list_per_page = 2

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'like_counts', 'like_count', 'dislike_count', 'Category', 'news_type', 'published_at')
    list_filter = ('Category',)
    search_fields = ('title',)
    list_editable = ('news_type', 'like_count', 'dislike_count')
    # date_hierarchy = "news__pub_date"
    # empty_value_display = "-empty-"
    # fields = ["title"]
    # exclude = ["like_count"]
    list_per_page = 2

    def like_counts(self, news):
        if int(news.like_count) > 5000:
            return 'Good'
        else:
            return 'Bad'

    # def published_at_a(self , news):
    # if str(news.published_at).lower() == 'true':
    # return 'Published'
    # else:
    # return 'Not Published'

admin.site.register(User ,UserAdmin)
admin.site.register(Category)
admin.site.register(News ,NewsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag , TagAdmin)
admin.site.register(Media , MediaAdmin)
admin.site.register(PhotoGallery)
admin.site.register(Image)
admin.site.register(ErrorReporting)
admin.site.register(ReportingAViolation)
admin.site.register(ContactUs)
admin.site.register(Podcast,PodcastAdmin)
admin.site.register(NewsPaper)
admin.site.register(Advertising)
admin.site.register(AboutUs)
admin.site.register(Avatar)
admin.site.register(MetaAdvertising)
admin.site.register(MetaContactUs)
admin.site.register(ReplyAnswer)
admin.site.register(Role)
admin.site.register(Slider)
admin.site.register(Popularity)
admin.site.register(FileUpload)