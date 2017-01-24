from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from ..login_register .models import User

# Create your models here.
class ProductManager(models.Manager):
    def validate_product(self, request):
        product = request.POST['product']
        is_valid = True
        print "*"*50
        print product
        if len(product) == 0:
            msg = "Must type in a product"
            messages.error(request, msg)
            is_valid = False
        if len(product) < 4:
            msg = "Product name must be at least 4 characters"
            messages.error(request, msg)
            is_valid = False
        if is_valid:
            user = User.objects.get(id=request.session['user'])
            prod = Product(name=product, creator=user.id)
            prod.save()
            prod.users.add(user)
            return True
        else:
            return False

class Product(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    creator = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()
