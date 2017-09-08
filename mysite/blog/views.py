from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .form import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts_all = Post.objects.all()
    posts_unpublished = posts_all.filter(published_date__isnull=True)
    posts_published = posts_all.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts_published' : posts_published, 'posts_unpublished' : posts_unpublished })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' : form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form' : form})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_list')

@login_required
def post_unpublish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.unpublish()
    return redirect('post_list')

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form' : form})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
