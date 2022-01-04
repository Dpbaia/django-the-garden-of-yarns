from django.shortcuts import render
from django.http import HttpResponse
from amigurumis.models import Amigurumi, AmigurumiImage


def index(request):
    # imports photos and save it in database
    lastest_amigurumis = Amigurumi.objects.all().order_by('-pk')[:3]
    num_amigurumis = Amigurumi.objects.all().count()
    ami_images = {}
    # Get all the latest amigurumis
    for amigurumi in lastest_amigurumis:
        # Then find the images belonging to them, and print only the first one. To display in the first page!
        ami_images[amigurumi.id] = AmigurumiImage.objects.filter(amigurumi=amigurumi)[0].image
    # adding context 

    context = {
        'num_amigurumis': num_amigurumis,
        'lastest_amigurumis': lastest_amigurumis,
        'amigurumi_images': ami_images,
    }
    return render(request, 'amigurumis/index.html', context=context)

def list(request, authorship):
    # GOTTA ADD PROTECTION TO THE AUTHORSHIP! SOMETHING LIKE ONLY RESPOND IF TRUE OR FALSE, ELSE THROW 404
    all_amigurumis = Amigurumi.objects.all()
    return render(request, 'amigurumis/list.html')

# Create your views here.
