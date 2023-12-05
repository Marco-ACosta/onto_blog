
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('most_liked', views.most_liked, name='most_liked'),
    path('<int:post_id>/', views.show, name='show'),
    path('like_dislike', views.like_dislike, name='like_dislike'),
    path('comment', views.comment, name='comment'),
    path('find', views.find, name='find'),
]