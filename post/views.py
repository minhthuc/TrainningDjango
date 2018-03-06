from django.http import HttpResponse
from post.models import Post, Author
from django.shortcuts import render, get_object_or_404
from pdb import set_trace as byebug

# Create your views here.
app_name = "post"
def index(request):
    posts = Post.objects.all()[:10]
    context = {
        'title': 'Posts',
        'all_post': posts,
    }
    return render(request,'posts/index.html',context)

def detail(request, post_id):
    # post = Post.objects.prefetch_related(Author).get(pk = post_id)
    post = get_object_or_404(Post.objects.select_related('author'), pk = post_id)
    # byebug()
    context = {
        'post': post,
        'title': post.title,
    }
    return render(request, 'posts/details.html', context)

def create(request):
    author = Author.objects.first()


def destroy(request, post_id):
    return HttpResponse("Delete post %s" %post_id)