from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import TemplateView, View, DeleteView,DetailView
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
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = invoice.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        context['itm'] = item.objects.all()
        context['invitem'] = invitem.objects.filter(inv=cart)
                
        return context


class pos_view(TemplateView):
    template_name= 'pos_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = invoice.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        context['itm'] = item.objects.all()
        context['invitem'] = invitem.objects.filter(inv=cart)
        context['cart_id'] = cart_id
                
        return context


# @csrf_exempt
def save_invitm(request, *args, **kwargs):
    if request.method =='GET':
        item = request.GET.get('itmname')
        price = request.GET.get('price')
        qty = request.GET.get('qty')
        amont = request.GET.get('amont')
        cu = request.GET.get('cu')
        sid = request.session.get("cart_id", None)
        # test
        if sid:
            inv_obj = invoice.objects.get(id=sid)
            s = invitem(inv=inv_obj, item=item, qty=qty, rate=price, amount=amont)
            s.save()
            inv_obj.total += int(amont)
            inv_obj.save()
            print('add item to invitem')
            return JsonResponse({'status':'success'})
        else:
            inv_obj = invoice.objects.create(customer=cu, total=0)
            request.session['cart_id'] = inv_obj.id
            print('add sid')
            s = invitem(inv=inv_obj, item=item, qty=qty, rate=price, amount=amont)
            s.save()

            return JsonResponse({'status':'success'})
        

    #     s = invitem(invoice=2, item=item, qty=qty, rate=price, amount=amont)
    #     s.save()
        #     stu = Student.objects.values()
        #     stu_data = list(stu)
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'error'})



def invoicelist(request):
    inm = invitem.objects.all()
    invs = invoice.objects.all()
    context = {'inv':inm, 'invs':invs}
    return render(request, 'invoicelist.html', context)




class InvoiceThermalPrintView(DetailView):
    template_name = 'test_slip.html'
    model = invoice
    context_object_name = 'ord_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ord_obj'] =

        return context