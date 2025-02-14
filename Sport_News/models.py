from django.db import models
from django.db.models import Model

class Category(models.Model):
    title = models.CharField(max_length=225)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    # parent = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
         return self.title

class Role(models.Model):
    title = models.CharField(max_length=200,default='title')
    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True , editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True , editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class User(models.Model):
    class user_type(models.TextChoices):
        VIP_USERS = 'VIP', 'VIP'
        MANAGER_USERS = 'MANAGER', 'MANAGER'
        USER = 'USER', 'USER'

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length=200)
    mobile= models.CharField(max_length=11)
    password = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=200 , null=True , blank=True)
    join_website_date = models.DateField(null=True, blank=True)
    main_picture = models.ImageField(null=True,blank=True)
    user_type = models.CharField(max_length=200, choices=user_type.choices, default=user_type.USER , blank=True)
    is_approved = models.BooleanField(default=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=None , null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Comment(models.Model):

    class status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PF', 'Published'
        PENDING = 'PN', 'Pending'

    class replay_type(models.TextChoices):
        QUESTION = 'Q', 'Question'
        RESPONSE = 'R', 'Response'

    title = models.CharField(max_length=200,default='title')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children_comment', on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0 , null=True , blank=True)
    dislike_count = models.IntegerField(default=0 , null=True , blank=True)
    body = models.TextField(null=True,blank=True)
    reply_answer = models.TextField(null=True,blank=True)
    published_at = models.DateTimeField(default=None , null=True , blank=True)
    is_approved = models.BooleanField(default=False)
    # ip_address = models.GenericIPAddressField()
    status = models.CharField(choices=status.choices, default=status.DRAFT, max_length=3 , null=True , blank=True)
    replay_type = models.CharField(choices=replay_type.choices, default=replay_type.QUESTION, max_length=3 , null=True , blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None , null=True , blank=True)
    admin_approve = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_approve', default=None , null=True , blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class News(models.Model):
    class news_type(models.TextChoices):
        # UNKNOWN = 'N', 'Unknown'
        IRAN_NEWS = 'IR','IRAN_NEWS'
        WORLD_NEWS = 'WO','WORLD_NEWS'

    title = models.CharField(max_length=200,default='title')
    like_count = models.IntegerField(default=0 , null=True , blank=True)
    dislike_count = models.IntegerField(default=0 , null=True , blank=True)
    published_at = models.DateTimeField(default=None , null=True , blank=True)
    number_of_visited = models.IntegerField( default=0 , null=True , blank=True)
    main_picture = models.FileField(upload_to='news/' , null=True , blank=True)
    body = models.TextField(null=True , blank=True)
    summary = models.TextField(null=True , blank=True)
    is_approved = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    news_type = models.CharField(choices=news_type.choices,default=news_type.IRAN_NEWS,max_length=3 , null=True , blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None , null=True , blank=True)
    createdUsers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_0', default=None , null=True , blank=True)
    updatedUsers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_1', default=None , null=True , blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default=None, null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='tags' , blank=True)
    image = models.ManyToManyField('Image', related_name='images_news' , blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class Avatar(models.Model):
    title = models.CharField(max_length=200,default=None)
    body = models.TextField(null=True,blank=True)
    color_background = models.CharField(max_length=200 , null=True , blank=True )
    color_skin = models.CharField(max_length=200 , null=True , blank=True )
    hair_color = models.CharField(max_length=200 , null=True , blank=True )
    hair_style = models.CharField(max_length=200 , null=True , blank=True )
    eyes = models.CharField(max_length=200 , null=True , blank=True )
    eyebrow = models.CharField(max_length=200 , null=True , blank=True )
    nose = models.CharField(max_length=200 , null=True , blank=True )
    mouth = models.CharField(max_length=200 , null=True , blank=True )
    shirt = models.CharField(max_length=200 , null=True , blank=True )
    is_approved = models.BooleanField(default=False)
    color_shirt = models.CharField(max_length=200 ,null=True , blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None , null=True , blank=True)
    created_date = models.DateTimeField(auto_now_add=True , editable=False , null=True , blank=True)
    updated_date = models.DateTimeField(auto_now=True , editable=False , null=True , blank=True)

    def __str__(self):
        return self.title

class ReplyAnswer(models.Model):

    class status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PF', 'Published'
        PENDING = 'PN', 'Pending'

    class replay_type(models.TextChoices):
        QUESTION = 'Q', 'Question'
        RESPONSE = 'R', 'Response'

    like_count = models.IntegerField(default=0, null=True, blank=True)
    dislike_count = models.IntegerField(default=0, null=True, blank=True)
    body = models.TextField(null=True,blank=True)
    is_approved = models.BooleanField(default=False)
    reply_answer = models.TextField(null=True,blank=True)
    status = models.CharField(choices=status.choices, default=status.DRAFT, max_length=3 , null=True , blank=True)
    replay_type = models.CharField(choices=replay_type.choices, default=replay_type.QUESTION, max_length=3 , null=True , blank=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, default=None , null=True , blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default=None , null=True , blank=True)
    avatar =  models.ForeignKey(Avatar, on_delete=models.CASCADE, default=None , null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.status

class Podcast(models.Model):
    title = models.CharField(max_length=200,default=None)
    like_count = models.IntegerField(default=0 , null=True , blank=True)
    dislike_count = models.IntegerField(default=0, null=True, blank=True)
    body = models.TextField(null=True,blank=True)
    download_count = models.IntegerField(default=0 , null=True, blank=True)
    number_of_visited = models.IntegerField(default=0 , null=True, blank=True)
    file_name = models.CharField(max_length=200)
    published_at = models.DateTimeField(default=None , null=True , blank=True)
    is_approved = models.BooleanField(default=False)
    createdUsers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='podcasts_0', default=None , null=True , blank=True)
    updatedUsers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='podcasts_1', default=None , null=True , blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default=None , null=True , blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class Media(models.Model):
    class status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PF', 'Published'
        PENDING = 'PN', 'Pending'

    class media_type(models.TextChoices):
        IRAN_MEDIA = 'IR', 'Iran_Media'
        WORLD_MEDIA = 'WO', 'World_Media'

    title = models.CharField(max_length=200,default=None)
    cover = models.ImageField(upload_to='media/' , null=True , blank=True)
    body = models.TextField(null=True,blank=True)
    poster_file_name = models.ImageField(null=True, blank=True)
    like_count = models.IntegerField(default=0 , null=True , blank=True)
    dislike_count = models.IntegerField(default=0, null=True, blank=True)
    download_count = models.IntegerField(default=0 , null=True, blank=True)
    published_at = models.DateTimeField(default=None , null=True , blank=True)
    is_active = models.BooleanField(default=False)
    status = models.CharField(choices=status.choices, default=status.DRAFT, max_length=2 , null=True , blank=True)
    media_type = models.CharField(max_length=200, choices=media_type.choices, default=media_type.IRAN_MEDIA , null=True , blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None , null=True, blank=True)
    createdUsers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media_0', default=None , null=True , blank=True)
    updatedUsers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media_1', default=None , null=True , blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default=None , null=True , blank=True)
    tags = models.ManyToManyField('Tag', related_name='tags_1' , blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class PhotoGallery(models.Model):
    title = models.CharField(max_length=200,default=None)
    file_name = models.CharField(max_length=200)
    file = models.FileField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    photographer = models.CharField(max_length=200)
    body = models.TextField(null=True,blank=True)
    like_count = models.IntegerField(default=0 , null=True , blank=True)
    dislike_count = models.IntegerField(default=0, null=True, blank=True)
    number_of_visited = models.IntegerField(default=0, null=True, blank=True)
    published_at = models.DateTimeField(default=None , null=True , blank=True)
    is_active = models.BooleanField(default=False)
    news = models.ForeignKey(News, on_delete=models.CASCADE, default=None , null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None , null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default=None , null=True , blank=True)
    tags = models.ManyToManyField('Tag', related_name='tags_2' , blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title
    #def __str__(self):
        #return f'{self.title} {self.photographer}'

class Tag(models.Model):
    class status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PF', 'Published'
        PENDING = 'PN', 'Pending'

    class visibility(models.TextChoices):
        VISIBLE = 'VI', 'Visible'
        INVISIBLE = 'IN', 'Invisible'

    name_tag = models.CharField(max_length=200)
    main_picture = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    status = models.CharField(choices=status.choices, default=status.DRAFT, max_length=2 , null=True , blank=True)
    visibility = models.CharField(choices=visibility.choices, default=visibility.INVISIBLE, max_length=2 , null=True , blank=True)
    createdUsers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_2', default=None , null=True , blank=True)
    updatedUsers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_3', default=None , null=True , blank=True)
    image = models.ManyToManyField('Image', related_name='images_tag')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.name_tag

class Image(models.Model):
    title = models.CharField(max_length=200,default=None)
    file = models.FileField(upload_to='images/' , null=True , blank=True)
    file_name = models.CharField(max_length=200)
    news = models.ForeignKey(News, on_delete=models.CASCADE, default=None , related_name='images_1' , null=True , blank=True)
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class ErrorReporting(models.Model):

    class problem_type(models.TextChoices):
        CONTENT_PROBLEM = 'CP', 'Content Problem'
        WRITING_PROBLEM = 'WP', 'Writing Problem'
        OTHER_PROBLEM = 'OCP', 'Other Problem'

    class admin_reason_type(models.TextChoices):
        TRUE = 'TR', 'True'
        FALSE = 'FS', 'False'

    title = models.CharField(max_length=200, default=None)
    body = models.TextField(null=True,blank=True)
    admin_reason = models.TextField(null=True,blank=True)
    is_approved = models.BooleanField(default=False)
    problem_type = models.CharField(choices=problem_type.choices, default=problem_type.OTHER_PROBLEM, max_length=3 , null=True , blank=True)
    admin_reason_type = models.CharField(choices=admin_reason_type.choices, default=admin_reason_type.TRUE, max_length=3 , null=True , blank=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, default=None , null=True , blank=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE, default=None , null=True , blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class ReportingAViolation(models.Model):
    class violation_type(models.TextChoices):
        INSULT = 'IN', 'Insult'
        POLITICAL = 'PO', 'Political'
        SPAM = 'SP', 'Spam'
        VULGAR_WORDS = 'VW', 'Vulgar Words'

    class admin_reason_type(models.TextChoices):
        TRUE = 'TR', 'True'
        FALSE = 'FS', 'False'

    title = models.CharField(max_length=200,default=None)
    admin_reason = models.TextField(null=True,blank=True)
    published_at = models.DateTimeField(default=None , null=True , blank=True)
    is_approved = models.BooleanField(default=False)
    violation_type = models.CharField(choices=violation_type.choices, default=violation_type.INSULT, max_length=3 , null=True , blank=True)
    admin_reason_type = models.CharField(choices=admin_reason_type.choices, default=admin_reason_type.TRUE, max_length=3 , null=True , blank=True)
    comment = models.ManyToManyField('Comment', related_name='comments' , blank=True)
    users = models.ManyToManyField('User', related_name='users' , blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class MetaContactUs(models.Model):
    title = models.CharField(max_length=200,default=None)
    phone = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    class related_unit(models.TextChoices):
        NEWS = 'NE', 'News'
        MANAGEMENT_SITE = 'MS', 'Management Site'
        VIDEO = 'VD', 'Video'
        TECHNICAL = 'TE', 'Technical'
        ADVERTISING = 'AD', 'Advertising'
        MARKETING = 'MA', 'Marketing'

    first_name = models.CharField(max_length=200 , default=None)
    last_name = models.CharField(max_length=200 , default=None)
    e_mail = models.EmailField(max_length=200 , default=None)
    mobile = models.CharField(max_length=11 , default=None)
    body = models.TextField(null=True,blank=True)
    published_at = models.DateTimeField(default=None , null=True , blank=True)
    is_approved = models.BooleanField(default=False)
    related_unit = models.CharField(choices=related_unit.choices, default=related_unit.NEWS, max_length=3 , null=True , blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None , null=True , blank=True)
    metacontactus = models.ForeignKey(MetaContactUs, on_delete=models.CASCADE, default=None , null=True , blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    #def __str__(self):
        #return self.related_unit

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.related_unit}'
        # return self.first_name + ' ' + self.last_name

class NewsPaper(models.Model):
    title = models.CharField(max_length=200,default=None)
    name_of_newspaper = models.CharField(max_length=200)
    image_of_newspaper = models.ImageField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.name_of_newspaper

class Advertising(models.Model):
    title = models.CharField(max_length=200,default=None)
    published_date_start = models.DateTimeField()
    published_date_expire = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    title = models.CharField(max_length=200,default=None)
    body = models.TextField(null=True,blank=True)
    main_picture = models.ImageField(null=True,blank=True)
    logo = models.ImageField(null=True,blank=True)
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class MetaAdvertising(models.Model):
    title = models.CharField(max_length=200,default=None)
    phone = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length=200)
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class Slider(models.Model):
    file = models.FileField(upload_to='Sliders' , null=True, blank=True)
    title = models.CharField(max_length=200,default=None)
    body = models.TextField(null=True,blank=True)
    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

class Popularity(models.Model):
    class popularity_type(models.TextChoices):
        LIKE = 'LI', 'Like'
        DISLIKE = 'DIS', 'Dislike'
        COMMENT = 'COM', 'Comment'

    model_name = models.CharField(max_length=200,default=None)
    model_id = models.PositiveIntegerField()
    count_model = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None , null=True , blank=True)
    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.model_name

class FileUpload(models.Model):
    title = models.CharField(max_length=100)
    files = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, default=None, related_name='images_m', null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title