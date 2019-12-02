from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# HelloWorld 是 TemplateView 的一个子类
class HelloWorld(TemplateView):
    template_name = 'test.html'