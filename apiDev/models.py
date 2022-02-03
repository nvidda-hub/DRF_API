from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
import random, string


def random_link_generator():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"title : {self.title}"


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def _str_(self):
        return self.title

class Store(models.Model):
    store_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.TextField(max_length=5000, null=False, blank=False)
    store_link = models.SlugField(blank=True, unique=True)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
def pre_save_store_receiver(sender, instance, *args, **kwargs):
    if not instance.store_link:
        instance.store_link = slugify(random_link_generator() + "-" + instance.store_name)

pre_save.connect(pre_save_store_receiver, sender=Store)