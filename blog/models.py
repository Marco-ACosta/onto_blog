# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     intro = models.TextField()
#     body = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
#     created_at = models.DateTimeField(auto_now_add=True)
#     posted_at = models.DateTimeField()
#     comments = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='comments')
#     likes = models.ForeignKey('Like', on_delete=models.CASCADE, related_name='likes')
    
#     readonly_fields = ['comments', 'likes']

#     def __str__(self):
#         return self.title

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

# class Like(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_at = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {
            'post': self.post,
            'user': self.user,
            'body': self.body,
            'created_at': self.created_at
        }

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
