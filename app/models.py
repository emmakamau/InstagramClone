from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
CASCADE will propagate the change when the parent changes. (If you delete a row, rows in constrained tables that reference that row will also be deleted, etc.)

SET NULL sets the column value to NULL when a parent row goes away.

RESTRICT causes the attempted DELETE of a parent row to fail.
'''

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    prof_pic = models.ImageField(blank=True, upload_to='media')
    bio = models.TextField(blank=True, max_length=255)
    website = models.URLField(blank=True, max_length=50)
    name = models.CharField(blank=True,max_length=50)

    def __str__(self):
        return self.bio

class Post(models.Model):
    image_upload = models.ImageField(upload_to='media',blank=False)
    image_name = models.CharField(max_length=50,blank=True)
    image_caption = models.TextField(max_length=255,blank=True)
    image_owner = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

class Comment(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    user_comment = models.CharField(blank=False, max_length=255)
    post_associated = models.ForeignKey(Post,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_comment

    def save_comment(self):
        self.save()

class PostVote(models.Model):
    vote = models.IntegerField()
    user_vote = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    post_voted = models.OneToOneField(Post,null=True,on_delete=models.CASCADE)


    