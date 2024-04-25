from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import TemplateView, View, DeleteView
from django.core import serializers
from django.http import JsonResponse
# Create your views here.
def test(request):
    return render(request, 'saleview.html')

class saleview(TemplateView):
    template_name = 'saleview.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itm'] = item.objects.all()
        context['invitem'] = invitem.objects.all()
        return context