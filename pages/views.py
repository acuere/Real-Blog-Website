from django.views.generic.base import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'