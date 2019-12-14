from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    DestroyAPIView, UpdateAPIView
)
from articles.models import Article
from .serializers import ArticleSerializer

""" 
class ArticlesListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticlesDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticlesCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticlesUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticlesDeleteView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
 """
from rest_framework import viewsets

class ArticleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()