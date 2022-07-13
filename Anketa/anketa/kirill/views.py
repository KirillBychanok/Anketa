from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Soft, Hard, Work, Aducation


def index(request):
    return render(request, 'kirill/index.html')


def python(request):
    return HttpResponseRedirect('https://www.python.org/')


def django(request):
    return HttpResponseRedirect('https://www.djangoproject.com/')


def docker(request):
    return HttpResponseRedirect('https://docs.docker.com/')


def redis(request):
    return HttpResponseRedirect('https://redis.io/docs/')


def soft_and_hard(request):
    sskils = Soft.objects.all()
    hskils = Hard.objects.all()
    context = {'sskils': sskils, 'hskils': hskils}
    return render(request, 'kirill/soft_hard.html', context)


def experience(request):
    mwork = Work.objects.all()
    context = {'mwork': mwork}
    return render(request, 'kirill/work.html', context)


def education(request):
    educ = Aducation.objects.all()
    context = {'educ': educ}
    return render(request, 'kirill/aducation.html', context)


def contacts(request):
    context = {'number': '+375297499937', 'email': 'kirillbychanok89@gmail.com', 'adress': 'Минск, Беларусь'}
    return render(request, 'kirill/contact.html', context)
