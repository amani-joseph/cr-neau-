from django.db import models
from django.utils import timezone
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    """
        category model acts as blueprint for all category instances
    """
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Location(models.Model):
    """
       location model acts as blueprint for all location instances
    """

    location = models.CharField(max_length=20, null=False, blank=False, default='Nairobi')

    def __str__(self):
        return self.location


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'images'

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.description

    @classmethod
    def show_all_images(cls):
        return cls.objects.order_by("pub_date")

    def save_image(self):
        return self.save()

    @classmethod
    def delete_image(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_image_by_category(cls, search_term):
        album = cls.objects.filter(category_category_name__icontains=search_term)
        return album

