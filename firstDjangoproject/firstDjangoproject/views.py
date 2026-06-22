from django.http import HttpResponse


def Home(request):
    return HttpResponse("Hello World, This is Home page.")


def About(request):
    return HttpResponse("Hello World, This is About page.")

def Contact(request):
    return HttpResponse("Hello World, This is Contact page.")