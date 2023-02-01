from django.shortcuts import HttpResponse, render


def home_func(request):
    return render(request, 'index.html')
