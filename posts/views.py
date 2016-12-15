from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import HttpResponse, HttpResponseRedirect
from . models import Post
from . forms import PostForm


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    
    context = {
        'form' : form,
    }

    return render(request, 'posts/post_form.html', context)



def post_list(request):
    queryset_list = Post.objects.all()
    pgntr = Paginator(queryset_list, 2) # Show 25 object_list per page

    page = request.GET.get('p')
    try:
        queryset = pgntr.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = pgntr.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = pgntr.page(paginator.num_pages)

    return render(request, 'posts/index.html', {'object_list': queryset})






def post_detail(request, id=None):
    result = get_object_or_404(Post, id=id)
    context = {
        'post' : result,
        'title' : 'My Posts'
    }
    return render(request, 'posts/post.html', context)


def post_update(request, id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_id())
    
    context = {
        'form' : form,
        'instance' : instance
    }
    
    return render(request, 'posts/post_form.html', context)

def post_delete(request):
    return render(request, 'posts/base.html')

