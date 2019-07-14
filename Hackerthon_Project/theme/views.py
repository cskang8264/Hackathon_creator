from django.shortcuts import render
from django.views.generic. base import TemplateView
# Create your views here.
class MainpageView(TemplateView):
    template_name = 'theme/main.html'