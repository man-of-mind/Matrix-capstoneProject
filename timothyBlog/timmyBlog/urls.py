from django.urls import path
from .views import AddPostView, HomePage, ArticleDetailPage

urlpatterns = [
#    path('', views.home, name="home"),
    path('', HomePage.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailPage.as_view(), name="article-detail"),
    path('add_new_post/', AddPostView.as_view(), name="add_new_post")
]
