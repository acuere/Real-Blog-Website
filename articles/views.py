from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Article


# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'



class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = '__all__'
    success_url = reverse_lazy('article_list.html')


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'summary', 'body', 'picture']
    success_url = reverse_lazy('article_list')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
