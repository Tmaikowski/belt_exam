from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Product
from ..login_register .models import User
# Create your views here.
def index(request):
    user = User.objects.get(id=request.session['user'])
    other_lists = User.objects.exclude(id=request.session['user'])
    context = {
        'user': user,
        'other_lists': other_lists
    }
    return render(request, 'wishlist/index.html', context)

def new(request):
    return render(request, 'wishlist/new.html')

def create_item(request):
    if request.method == "POST":
        did_create = Product.objects.validate_product(request)
        if did_create:
            return redirect(reverse("wishlist:index"))
        else:
            return redirect(reverse("wishlist:new"))

def add_to_list(request, id):
    product = Product.objects.get(id=id)
    user = User.objects.get(id=request.session['user'])
    product.users.add(user)
    return redirect(reverse("wishlist:index"))

def show(request, id):
    product = Product.objects.get(id=id)
    context = {'product':product}
    return render(request, 'wishlist/show.html', context)

def remove_from_list(request, id):
    user = User.objects.get(id=request.session['user'])
    Product.objects.get(id=id).users.remove(user)
    print "*"*50

    print "*"*50

    return redirect(reverse('wishlist:index'))

def delete(request, id):
    Product.objects.get(id=id).delete()
    return redirect(reverse('wishlist:index'))
