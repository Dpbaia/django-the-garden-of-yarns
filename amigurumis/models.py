from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

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
        return reverse('amigurumi-detail', args=[str(self.id)])

    # How it displays:
    def __str__(self):
        return self.name

class AmigurumiImage(models.Model):
    amigurumi = models.ForeignKey(Amigurumi, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')
