from django.urls import path
from .views import AddPostView, HomePage, ArticleDetailPage, UpdatePostView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailPage.as_view(), name="article-detail"),
    path('add_new_post/', AddPostView.as_view(), name="add_new_post"),
    path('articles/edit/<int:pk>', UpdatePostView.as_view(), name="edit-post")
]
