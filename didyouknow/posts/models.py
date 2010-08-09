from django.db import models
import datetime
import md5
# Create your models here.

#USER MODEL
class User(models.Model):
    username = models.CharField(max_length = 40)
    password = models.CharField(max_length = 100)
    email = models.CharField(max_length = 50)
    registered_date = models.DateField('registered_date')
    biography = models.TextField()

    def __unicode__(self):
        return self.username



#POST MODEL
class Post(models.Model):
     user = models.ForeignKey(User)
     post = models.CharField(max_length = 255)
     pub_date = models.DateTimeField('date_published')

     def __unicode__(self):
         return self.post
    
    #is published today
     def is_published_today(self):
         return self.pub_date == datetime.date.today()
         

#COMMENT MODEL
class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    comment = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.comment
        
     