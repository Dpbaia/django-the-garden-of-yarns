from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from amigurumis.models import Amigurumi, AmigurumiImage
from django.views import generic


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
    if authorship == "false":
        all_amigurumis = Amigurumi.objects.all()
        context={
            'amigurumi_list': all_amigurumis,
            'page_name': 'All Works',
        }
        return render(request, 'amigurumis/amigurumi_list.html', context=context)
    elif authorship == "true":
        authorship_amigurumis = Amigurumi.objects.filter(authorship=True)
        context={
            'amigurumi_list': authorship_amigurumis,
            'page_name': 'Own Recipes',
        }
        return render(request, 'amigurumis/amigurumi_list.html', context=context)
    else:
        raise Http404

def detail(request, pk):
    context={
        'amigurumi': Amigurumi.objects.get(pk=pk),
    }
    return render(request, 'amigurumis/amigurumi_detail.html', context = context)

def about(request):
    return render(request, 'amigurumis/about.html')

def socials(request):
    return render(request, 'amigurumis/socials.html')

# class AmigurumiListView(generic.ListView): # Cannot use additional arguments here! But an example of how a generic view would work.
#     model = Amigurumi
#     ## Overriding the default configurations:
#     # context_object_name = 'my_book_list'   # your own name for the list as a template variable
#     # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
#     # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get the context
#         context = super(AmigurumiListView, self).get_context_data(**kwargs)
#         # Create any data and add it to the context
#         context['page_name'] = 'All Works'
#         return context

# Create your views here.
