from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=256)
    price = models.DecimalField(max_digits=14, decimal_places=0)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)