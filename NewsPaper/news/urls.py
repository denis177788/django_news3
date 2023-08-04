from django.urls import path
from .views import PostList, PostDetail, PostSearch, NewsCreate, NewsEdit, PostDelete #create_news

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detal'),
   path('search/', PostSearch.as_view(), name='search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
#  path('create/', create_news, name='create_news'),
]
