from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe


class Amigurumi(models.Model):
    name = models.CharField(
        max_length=50, help_text="Enter name of the amigurumi", blank=False
    )
    authorship = models.BooleanField(
        default=False, help_text="If you're the author of the recipe"
    )
    url = models.CharField(
        max_length=100, help_text="Enter url of the amigurumi", blank=True
    )

    class Meta:
        ordering = ["name", "authorship"]

    def get_absolute_url(self):
        return reverse("amigurumis:amigurumi-detail", args=[str(self.id)])

    def __str__(self):
        return self.name


class AmigurumiImage(models.Model):
    amigurumi = models.ForeignKey(
        Amigurumi, related_name="images", on_delete=models.CASCADE
    )
    image = CloudinaryField("image")


class AboutInfo(models.Model):
    photo = CloudinaryField("photo")
    description = models.TextField(
        default="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ut pellentesque nulla. Donec quis nulla at libero laoreet tempor. Ut egestas nulla diam, sit amet varius tellus iaculis sit amet. Aenean porta, mauris quis pellentesque lobortis, elit nisl pulvinar nunc, eu pellentesque leo augue non ante. Vivamus faucibus aliquet neque, vel viverra diam pulvinar vel. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse placerat ultricies nisi id malesuada.",
        help_text="Enter the description of your about page",
    )

    def save(self, *args, **kwargs):
        if not self.pk and AboutInfo.objects.exists():
            raise ValidationError("There can be only one About Info instance")
        return super(AboutInfo, self).save(*args, **kwargs)

    def admin_photo(self):
        return '<img src="%s"/>' % self.photo

    admin_photo.allow_tags = True
