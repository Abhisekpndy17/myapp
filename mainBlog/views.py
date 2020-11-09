from django.shortcuts import render, redirect
from .models import Posts
from .forms import CommentForm


# Create your views here.
def home(request):
    
    posts = Posts.objects.all()

    return render(request, 'mainblog/home.html', {'posts':posts})

def post_detail(request, slug):
    post = Posts.objects.get(slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug )
    else:
        form = CommentForm()


    return render(request, 'mainblog/post_detail.html', {'post': post, 'form':form})