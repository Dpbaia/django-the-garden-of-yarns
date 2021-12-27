from django.shortcuts import render
from django.http import HttpResponse
from amigurumis.models import Amigurumi, AmigurumiImage


def index(request):
    # imports photos and save it in database
    photo = AmigurumiImage.objects.all()
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'index.html')

# Create your views here.
