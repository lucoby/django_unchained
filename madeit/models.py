import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Thread(models.Model):
    thread_title = models.CharField(max_length=200)
    thread_text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.thread_text
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Comment(models.Model):
    thread = models.ForeignKey(Thread)
    comment_text = models.TextField(max_length=1000)
    votes = models.IntegerField(default=0)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.comment_text