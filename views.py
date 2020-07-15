from django.http import HttpResponse

def about(request):
    return HttpResponse('welcome to About page ... !')

def homepage(request):
    return HttpResponse('welcome to homepage... !')
