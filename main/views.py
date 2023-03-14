from django.shortcuts import render

def Home(request):
    return render(request, 'main/home.html')

def Manual(request):
    return render(request, 'main/manual.html')

def PageNotFound(request, exception = None):
    return render(request, 'main/notFound.html')
