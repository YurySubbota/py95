from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def post_iist(request):
    posts = Post.objects.order_by('id')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post_list.html', {'posts': posts,
                                              'page': page})

