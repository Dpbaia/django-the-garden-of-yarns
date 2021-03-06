# Generated by Django 4.0 on 2022-01-10 17:01

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amigurumis', '0002_alter_amigurumi_options_alter_amigurumi_authorship_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='photo')),
                ('description', models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ut pellentesque nulla. Donec quis nulla at libero laoreet tempor. Ut egestas nulla diam, sit amet varius tellus iaculis sit amet. Aenean porta, mauris quis pellentesque lobortis, elit nisl pulvinar nunc, eu pellentesque leo augue non ante. Vivamus faucibus aliquet neque, vel viverra diam pulvinar vel. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse placerat ultricies nisi id malesuada.', help_text='Enter the description of your about page')),
            ],
        ),
    ]
