from django.urls import path
from .views import HomePage, ArticleDetailPage

urlpatterns = [
#    path('', views.home, name="home"),
    path('', HomePage.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailPage.as_view(), name="article-detail"),
]
