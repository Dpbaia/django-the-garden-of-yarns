from django.shortcuts import render
from django.http import HttpResponse
from amigurumis.models import Amigurumi, AmigurumiImage


def index(request):
    # imports photos and save it in database
    latest_amigurumis = Amigurumi.objects.all()[:3]

    # Get all the latest amigurumis
    for amigurumi in latest_amigurumis:
        # Then find the images belonging to them, and print only the first one. To display in the first page!
        AmigurumiImage.objects.filter(amigurumi=amigurumi)[0]
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'index.html')

# Create your views here.
