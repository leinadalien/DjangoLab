from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Создать аферу", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


class NoScamHome(ListView):
    model = Scamer
    template_name = 'noscamapp/index.html'
    context_object_name = 'scamers'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная'
        return context

class ShowScams(ListView):
    model = Scam
    template_name = 'noscamapp/index.html'
    context_object_name = 'scams'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Скамы'
        return context

    def get_queryset(self):
       return Scam.objects.filter(scamer__id=self.kwargs['scamer_id'])
