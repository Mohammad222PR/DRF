from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

app_name = 'home'

urlpatterns = [
    # path('blog', views.home, name='home'),
    # path('article', views.ArticleView.as_view(), name='article_list'),
    # path('article/detail/<slug:slug>', views.ArticleDetailView.as_view(), name='article_detail'),
    # path('article/add', views.AddArticleView.as_view(), name='article_add'),
    # path('article/update/<int:pk>', views.ArticleUpdateView.as_view(), name='article_update'),
    path('check_token', views.CheckToken.as_view(), name='check_token'),
    # path('login', token_views.obtain_auth_token),
    path('article/comments/<int:pk>', views.GetArticlesCommentView.as_view(), name='article_comments'),
    path('user/detail/<int:pk>', views.UserDetailView.as_view(), name='article_comments'),
    path('users', views.UserView.as_view(), name='article_comments'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),

]

router = DefaultRouter()
router.register(r'articles/viewset', views.ArticleListView, basename='articles')
urlpatterns += router.urls
