# coding: utf-8

from django.views.generic import TemplateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import ArticleSerializer
from .models import Article


class ArticleList(ListCreateAPIView):
    """
    List all the articles.
    /api/v1/articles/
    
    Create article
    {
        "name": "Blusa",
        "description": "Seda blanca",
        "price": 34.90
    }
    """
    model = Article
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    """
    GET/PUT/DELETE article:
    /api/v1/articles/<article_id>
    """
    model = Article
    serializer_class = ArticleSerializer


class EasterEgg(TemplateView):
    """
    /donald-trump
    """
    template_name = 'orders/donald_trump.html'
