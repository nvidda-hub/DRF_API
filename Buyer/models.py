from django.db import models
from apiDev.models import Product, Store, Customer



# Create your models here.
class Cart(models.Model):
    cart_id = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    store = models.ManyToManyField(Store)

    class Meta:
        ordering = ["cart_id", "-created_at"]
    
    def __str__(self):
        return str(self.cart_id)