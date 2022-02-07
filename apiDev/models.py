from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
import random, string
from django.db import models
from apiDev.managers import MyAccountManager
from django.contrib.auth.models import AbstractBaseUser

from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token




def pre_save_store_receiver(sender, instance, *args, **kwargs):
    if not instance.store_link:
        instance.store_link = slugify(random_link_generator() + "-" + instance.store_name)



def upload_location(instance, filename):
    print("\n\n instance.store_name : ", instance.store_name, "\n\n")
    print("\n\n instance.store_name.owner : ", instance.store_name.owner, "\n\n")
    file_path = f'store/{str(instance.store_name.owner)}/{str(instance.store_name)}-{filename}'
    return file_path

def random_link_generator():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


# Create your models here.


class Account(AbstractBaseUser):
    username  = models.CharField(max_length=17, unique=True)
    first_name  = models.CharField(max_length=30, blank=True)
    last_name   = models.CharField(max_length=30, blank=True)
    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login	= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin	= models.BooleanField(default=False)
    is_active	= models.BooleanField(default=True)
    is_staff	= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class Store(models.Model):
    store_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.TextField(max_length=5000, null=False, blank=False)
    store_link = models.SlugField(blank=True, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.store_name


pre_save.connect(pre_save_store_receiver, sender=Store)


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title





class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=5000, null=False, blank=False)
    MRP = models.IntegerField()
    sale_price = models.IntegerField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    store_name = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Customer(AbstractBaseUser):
    customer_email  = models.EmailField(max_length=30, unique=True)
    customer_name = models.CharField(max_length=50, blank=True)
    customer_address = models.TextField(max_length=5000, null=False, blank=False)

    USERNAME_FIELD = 'customer_email'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        return self.customer_email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Order(models.Model):
    ordered_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer