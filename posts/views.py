from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import PermissionDenied
from django.shortcuts import HttpResponse, HttpResponseRedirect, Http404
from . models import Post
from . forms import PostForm


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise PermissionDenied

    form = PostForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    
    context = {
        'form' : form,
    }

    return render(request, 'posts/post_form.html', context)



def post_list(request, slug=None):
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






def post_detail(request, slug=None):
    result = get_object_or_404(Post, slug=slug)
    context = {
        'post' : result,
        'title' : 'My Posts'
    }
    return render(request, 'posts/post.html', context)


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
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

def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")

