from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views

app_name = 'home'

urlpatterns = [
    path('blog', views.home, name='home'),
    path('article', views.ArticleView.as_view(), name='article_list'),
    path('article/detail/<slug:slug>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/add', views.AddArticleView.as_view(), name='article_add'),
    path('article/update/<int:pk>', views.ArticleUpdateView.as_view(), name='article_update'),
    path('check_token', views.CheckToken.as_view(), name='check_token'),
    path('login', token_views.obtain_auth_token),
    path('article/comments/<int:pk>', views.GetArticlesCommentView.as_view(), name='article_comments'),
]
