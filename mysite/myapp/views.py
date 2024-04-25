from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import TemplateView, View, DeleteView
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def save_invitm(request):
    if request.method =='POST':
        item = request.POST['itmname']
        price = request.POST['price']
        qty = request.POST['qty']
        amont = request.POST['amont']

        #     s = Student(name=name, email=email, phone=phone)
        #     s.save()
        #     stu = Student.objects.values()
        #     stu_data = list(stu)
        return JsonResponse({'status':'success'})
        # else:
        #     return JsonResponse({'status':'error'})

