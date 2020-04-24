from django.shortcuts import render
from .models import Review
# Create your views here.

def games(request):
    data = Review.objects.order_by('-review_int')
    recent = Review.objects.order_by('-release_date')[:4]
    context = {
        'data': data,
        'recent': recent,
    }
    return render(request,'games/review.html', context)

def single_review(request,game_id):
    single = Review.objects.filter(pk=game_id)
    context = {
        'single': single,
    }
    return render(request, 'games/single_review.html', context)