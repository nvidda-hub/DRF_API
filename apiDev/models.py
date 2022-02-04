from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
import random, string


def random_link_generator():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def _str_(self):
        return f"{self.title} New Category added."

class Store(models.Model):
    store_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.TextField(max_length=5000, null=False, blank=False)
    store_link = models.SlugField(blank=True, unique=True)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
def pre_save_store_receiver(sender, instance, *args, **kwargs):
    if not instance.store_link:
        instance.store_link = slugify(random_link_generator() + "-" + instance.store_name)

pre_save.connect(pre_save_store_receiver, sender=Store)




class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=5000, null=False, blank=False)
    MRP = models.IntegerField()
    sale_price = models.IntegerField()
    # image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name} added to {self.store}"


class Customer(models.Model):
    customer_mobile_num  = models.CharField(max_length=17, unique=True)
    customer_name = models.CharField(max_length=50, blank=True)
    customer_address = models.TextField(max_length=5000, null=False, blank=False)


class Order(models.Model):
    ordered_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)