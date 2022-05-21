from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Article


# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'



class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ['title','picture','body','summary']
    success_url = reverse_lazy('article_list')


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'summary', 'body', 'picture']
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDetailView( DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
