from django.shortcuts import render
from blog.models import Category, Blog
from django.core.paginator import Paginator
from forums.models import Forum



# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    latest_blog = Blog.objects.order_by('-date')[:3]
    paginator = Paginator(blogs, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    latest_comment = Forum.objects.order_by('-date')[:3]

    context = {
        'blogs': blogs,
        'latest_blog': latest_blog,
        'page_obj': page_obj,
        'latest_comment':latest_comment,
    }
    return render(request, 'blog/categories.html', context)



#from django.shortcuts import render
#from .models import Review

# Create your views here.
#def games(request):
 #   data = Review.objects.order_by('-review_int')
  #  recent = Review.objects.order_by('-release_date')[:4]
   # context = {
    #    'data': data,
     #   'recent': recent,
#
 #   }
  #  return render(request,'games/review.html', context)
#<section class="review-section review-dark spad set-bg" data-setbg="{% static 'img/review-bg-2.jpg' %}">
#		<div class="container">
#			<div class="section-title text-white">
#				<div class="cata new">new</div>
#				<h2>Recent Games</h2>
#			</div>
#			<div class="row text-white">
 #           {% if latest_blog %}
  #            {% for r in latest_blog %}
	#			<div class="col-lg-3 col-md-6">
	#				<div class="review-item">
	#					<div class="review-cover set-bg" data-setbg="{{ r.photo.url }}">
	#						<div class="score yellow">{{r.review_int}}</div>
	#					</div>
	#					<div class="review-text">
	#						<h5>{{ r.name }}</h5>
	#						<p>{{ r.content}}</p>
	#					</div>
	#				</div>
#				</div>
 #           {% endfor %}
  #              {% else %}
   #             <p> do nothing </p>
    #    {% endif %}
     #       </div>
	#	</div>
	#</section>