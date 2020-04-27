from django.shortcuts import render
from games.models import Review
from blog.models import Blog
from forums.models import Forum


# Create your views here.
def home(request):
    data = Review.objects.order_by('-review_int')
    recent_post = Review.objects.order_by('-release_date')[:4]
    latest_blog = Blog.objects.order_by('-date')[:3]

    context = {
        'data': data,
        'recent_post': recent_post,
        'latest_blog': latest_blog,
    }
    return render(request, 'home/index.html', context)


##def allfooter(request):
  ##  top_comment = Forum.objects.order_by('-date')[:3]

    ##context2 = {
      ##  'top_comment': top_comment,
    ##}
    ##return render(request, 'partial/_footer.html', context2)
