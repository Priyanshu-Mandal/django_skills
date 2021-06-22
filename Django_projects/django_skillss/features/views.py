from features.models import data
from django.http import HttpResponse

# Create your views here.

def run(request):
    return HttpResponse('Hello world!')
