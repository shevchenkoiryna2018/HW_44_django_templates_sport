from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'sport/index.html', context)


def football(request):
    context = {}
    return render(request, 'sport/football.html', context)


def hockey(request):
    context = {}
    return render(request, 'sport/hockey.html', context)


def basketball(request):
    context = {}
    return render(request, 'sport/basketball.html', context)

