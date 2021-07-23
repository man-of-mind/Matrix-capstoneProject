from timmyBlog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


#def home(request):
#    return render(request, 'home.html', {})

class HomePage(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailPage(DetailView):
    model = Post
    template_name = 'article_details.html'
    