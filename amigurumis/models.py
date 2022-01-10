from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.utils.html import mark_safe

# Create your models here.
class Amigurumi(models.Model):
    #Fields: 
    name = models.CharField(max_length=50, help_text='Enter name of the amigurumi')
    authorship = models.BooleanField(default=False, help_text="If you're the author of the recipe")

    

    #Metadata:
    class Meta:
        ordering = ['name', 'authorship']

    #Methods
    def get_absolute_url(self):
        #NOT WORKING YET, have to replace the model-detail-view with the view yet to be created
        return reverse('amigurumis:amigurumi-detail', args=[str(self.id)])

    # How it displays:
    def __str__(self):
        return self.name

class AmigurumiImage(models.Model):
    amigurumi = models.ForeignKey(Amigurumi, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')

class AboutInfo(models.Model):
    photo = CloudinaryField('photo')
    description = models.TextField(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ut pellentesque nulla. Donec quis nulla at libero laoreet tempor. Ut egestas nulla diam, sit amet varius tellus iaculis sit amet. Aenean porta, mauris quis pellentesque lobortis, elit nisl pulvinar nunc, eu pellentesque leo augue non ante. Vivamus faucibus aliquet neque, vel viverra diam pulvinar vel. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse placerat ultricies nisi id malesuada.", help_text="Enter the description of your about page")

    def save(self, *args, **kwargs):
        # Can only have one instance of this object
        # Unless it's the object that already exists AND an object actually exists, throw an error
        if not self.pk and AboutInfo.objects.exists():
            raise ValidationError('There can be only one About Info instance')
        return super(AboutInfo, self).save(*args, **kwargs)
    
    def admin_photo(self):
        return '<img src="%s"/>' % self.photo
    admin_photo.allow_tags = True