from django.http import HttpResponse

# Create your views here.
def index_page(request): 
    return HttpResponse("hello from directors")