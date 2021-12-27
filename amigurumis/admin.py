from django.contrib import admin

from amigurumis.models import Amigurumi, AmigurumiImage

# Register your models here.

class AmigurumiImageInline(admin.TabularInline):
    model = AmigurumiImage
    extra = 3

class AmigurumiAdmin(admin.ModelAdmin):
    inlines = [AmigurumiImageInline,]

admin.site.register(Amigurumi, AmigurumiAdmin)