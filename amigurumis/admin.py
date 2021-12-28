from django.contrib import admin

from amigurumis.models import Amigurumi, AmigurumiImage

# Register your models here.

class AmigurumiImageInline(admin.TabularInline):
    model = AmigurumiImage
    extra = 3

class AmigurumiAdmin(admin.ModelAdmin):
    # Show the images too! So you can change them in the same page.
    inlines = [AmigurumiImageInline,]
    #The fields attribute lists just those fields that are to be displayed on the form, in order. 
    # Fields are displayed vertically by default, 
    # but will display horizontally if you further group them in a tuple.
    list_display = ('name', 'authorship')
    list_filter = ['authorship']


admin.site.register(Amigurumi, AmigurumiAdmin)