from django.contrib import admin

from amigurumis.models import AboutInfo, Amigurumi, AmigurumiImage


class AmigurumiImageInline(admin.TabularInline):
    model = AmigurumiImage
    extra = 3


class AmigurumiAdmin(admin.ModelAdmin):
    inlines = [
        AmigurumiImageInline,
    ]
    list_display = ("name", "authorship")
    list_filter = ["authorship"]


class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ["description"]


admin.site.register(Amigurumi, AmigurumiAdmin)
admin.site.register(AboutInfo, AboutInfoAdmin)
