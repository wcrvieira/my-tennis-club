from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('vendors/', views.vendors, name='vendors'),
    path('vendors/details/<int:id>', views.details, name='details'),
    path('vendors/add/', views.add, name='add'),
    path('vendors/add/addrecord/', views.addrecord, name='addrecord'),
    path('vendors/delete/<int:id>', views.delete, name='delete'),
    path('vendors/update/<int:id>', views.update, name='update'),
    path('vendors/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]