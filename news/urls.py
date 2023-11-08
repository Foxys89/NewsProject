from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostsList, PostDetail, PostSearch, NewsCreate,\
   PostEdit, PostDelete, ArticleCreate, IndexView, upgrade_me, BaseRegisterView

urlpatterns = [
   path('posts/', PostsList.as_view(), name = 'post_list'),
   path('posts/<int:pk>', PostDetail.as_view(), name = 'post_detail'),
   path('posts/search/', PostSearch.as_view(), name = 'post_search'),
   path('posts/newscreate/', NewsCreate.as_view(), name='news_create'),
   path('posts/<int:pk>/newsedit/',PostEdit.as_view(), name='news_edit'),
   path('posts/<int:pk>/newsdelete/', PostDelete.as_view(), name='news_delete'),
   path('posts/articlecreate/', ArticleCreate.as_view(), name='article_create'),
   path('posts/<int:pk>/articleedit/',PostEdit.as_view(), name='article_edit'),
   path('posts/<int:pk>/articledelete/', PostDelete.as_view(), name='article_delete'),
   path('', IndexView.as_view()),
   path('upgrade/', upgrade_me, name = 'upgrade'),
   path('login/', LoginView.as_view(template_name = 'login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name = 'logout.html'),name='logout'),
   path('signup/', BaseRegisterView.as_view(template_name = 'signup.html'), name='signup')
]