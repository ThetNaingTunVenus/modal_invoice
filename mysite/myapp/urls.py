from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
    path('test/', views.test, name = 'test'),
    path('saleview/', saleview.as_view(), name='saleview'),
    path('pos_view/', pos_view.as_view(), name='pos_view'),
    path('save_invitm/', views.save_invitm, name= 'save_invitm'),
    path('invoiceview/<int:pk>/', invoiceview.as_view(), name='invoiceview'),

]