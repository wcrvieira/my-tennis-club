from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    telefone = request.POST['telefone']
    data_cadastro = request.POST['data_cadastro']
    member = Member(firstName=nome, lastName=sobrenome, phone=telefone, joined_date=data_cadastro)
    member.save()
    return HttpResponseRedirect(reverse('members'))

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('members'))

def update(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    telefone = request.POST['telefone']
    data_cadastro = request.POST['data_cadastro']
    member = Member.objects.get(id=id)
    member.firstName = nome
    member.lastName = sobrenome
    member.phone = telefone
    member.joined_date = data_cadastro
    member.save()
    return HttpResponseRedirect(reverse('members'))