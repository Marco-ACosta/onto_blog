from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from blog.forms import CommentForm
from blog.models import Comment, Like, Post
from django.contrib import messages


# Create your views here.

def index(request):
    posts = Post.objects.filter(posted_at__lt=datetime.now()).order_by('-posted_at')
    post_likes= []
    
    for post in posts:
        likes = len(Like.objects.filter(post_id=post.id).all())
        post_likes.append([post, likes])

    return render(request, 'blog/index.html', {'posts': post_likes})

def show(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    likes = Like.objects.filter(post_id=post_id).all()
    comments = Comment.objects.filter(post_id=post_id).all().order_by('-created_at')

    comment_form = CommentForm()

    return render(request, 'blog/post.html', {'post': post, 'likes': likes.count(), 'comments': comments, 'form': comment_form})

def most_liked(request):
    posts = Post.objects.all()
    post_likes= []
    
    for post in posts:
        likes = len(Like.objects.filter(post_id=post.id).all())
        post_likes.append([post, likes])

    post_likes.sort(key=lambda x: x[1], reverse=True)

    return render(request, 'blog/index.html', {'posts': post_likes})

def find(request):
    posts = Post.objects.all().order_by('-created_at').filter(title__contains=request.GET['find'])
    post_likes= []
    
    for post in posts:
        likes = len(Like.objects.filter(post_id=post.id).all())
        post_likes.append([post, likes])

    return render(request, 'blog/index.html', {'posts': post_likes})

@login_required
def like_dislike(request):
    if request.method != 'POST':
        return redirect('index')

    messages.get_messages(request).used = True
    post_id = request.POST['post_id']
    like = Like.objects.filter(post_id=post_id, user_id=request.user.id).first()

    if like is not None:
        like.delete()
        return redirect('show', post_id=post_id)
    
    l = Like(post_id=post_id, user_id=request.user.id)
    l.save()
    return redirect('show', post_id=post_id)

@login_required
def comment(request):
    if request.method != 'POST':
        return redirect('index')

    messages.get_messages(request).used = True
    comment = CommentForm(request.POST)
    post_id = request.POST['post_id']
    
    if comment.is_valid():
        Comment.objects.create(post_id=post_id, user_id=request.user.id, body=request.POST['comment'])
        messages.success(request, 'Comentário adicionado com sucesso!')
        return redirect('show', post_id=post_id)

    messages.error(request, 'Algo deu errado, tente novamente!')
    return redirect('show', post_id=post_id)
