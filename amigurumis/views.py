from django.http import Http404
from django.shortcuts import render

from amigurumis.models import AboutInfo, Amigurumi, AmigurumiImage


def index(request):
    lastest_amigurumis = Amigurumi.objects.all().order_by("-pk")[:3]
    num_amigurumis = Amigurumi.objects.all().count()
    ami_images = {}
    for amigurumi in lastest_amigurumis:
        ami_images[amigurumi.id] = AmigurumiImage.objects.filter(amigurumi=amigurumi)[
            0
        ].image
    context = {
        "num_amigurumis": num_amigurumis,
        "lastest_amigurumis": lastest_amigurumis,
        "amigurumi_images": ami_images,
    }
    return render(request, "amigurumis/index.html", context=context)


def list(request, authorship):
    if authorship == "false":
        all_amigurumis = Amigurumi.objects.all()
        context = {
            "amigurumi_list": all_amigurumis,
            "page_name": "All Works",
        }
        return render(request, "amigurumis/amigurumi_list.html", context=context)
    elif authorship == "true":
        authorship_amigurumis = Amigurumi.objects.filter(authorship=True)
        context = {
            "amigurumi_list": authorship_amigurumis,
            "page_name": "My designs",
        }
        return render(request, "amigurumis/amigurumi_list.html", context=context)
    else:
        raise Http404


def detail(request, pk):
    context = {
        "amigurumi": Amigurumi.objects.get(pk=pk),
    }
    return render(request, "amigurumis/amigurumi_detail.html", context=context)


def about(request):
    context = {
        "about": AboutInfo.objects.first(),
    }
    return render(request, "amigurumis/about.html", context=context)


def socials(request):
    return render(request, "amigurumis/socials.html")
