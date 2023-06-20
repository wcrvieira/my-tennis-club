from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Vendor

def vendors(request):
    myvendors = Vendor.objects.all().values()
    template = loader.get_template('all_vendors.html')
    context = {
        'myvendors': myvendors,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myvendor = Vendor.objects.get(id=id)
    template = loader.get_template('detailsVend.html')
    context = {
        'myvendor': myvendor,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def add(request):
    template = loader.get_template('addVend.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    cnpj = request.POST['cnpj']
    razaosocial = request.POST['razaosocial']
    vendor = Vendor(cnpj=cnpj, razaosocial=razaosocial)
    vendor.save()
    return HttpResponseRedirect(reverse('vendors'))

def delete(request, id):
    vendor = Vendor.objects.get(id=id)
    vendor.delete()
    return HttpResponseRedirect(reverse('vendors'))

def update(request, id):
    myvendor = Vendor.objects.get(id=id)
    template = loader.get_template('updateVend.html')
    context = {
        'myvendor' : myvendor,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    cnpj = request.POST['cnpj']
    razaosocial = request.POST['razaosocial']
    vendor = Vendor.objects.get(id=id)
    vendor.cnpj = cnpj
    vendor.razaosocial = razaosocial
    vendor.save()
    return HttpResponseRedirect(reverse('vendors'))