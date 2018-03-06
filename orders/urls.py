from django.conf.urls import url

from .views import ArticleList, ArticleDetail

urlpatterns = [
    url(r'^articles/?$', ArticleList.as_view(), name='article_list'),
    url(r'^articles/(?P<pk>[0-9]+)/?$', ArticleDetail.as_view(), name='article_detail')
]
