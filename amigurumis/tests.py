from django.test import TestCase

from amigurumis.models import *

class AmigurumiModelTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        Amigurumi.objects.create(name="Mud", authorship="True", url="#")
        Amigurumi.objects.create(name="NoURL", authorship="True")
    
    def test_can_create_without_url(self):
        ami = Amigurumi.objects.get(id=2)
        self.assertTrue(ami.name, "NoURL")
        print("Method: Test if you can create an amigurumi with no url")

    def test_get_absolute_url(self):
        ami = Amigurumi.objects.get(id=1)
        self.assertEqual(ami.get_absolute_url(), '/amigurumis/1/')
        print("Method: Test if you the absolute url is giving the expected path")


# Create your tests here.
