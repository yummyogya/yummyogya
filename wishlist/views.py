from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.apps import apps
from .models import Wishlist

@login_required
def add_to_wishlist(request, product_id):
    Makanan = apps.get_model('wishlist', 'Makanan')  
    product = get_object_or_404(Makanan, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')  

@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def remove_from_wishlist(request, product_id):
    Makanan = apps.get_model('wishlist', 'Makanan')  
    product = get_object_or_404(Makanan, id=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product)
    if wishlist_item.exists():
        wishlist_item.delete()
    return redirect('wishlist')  
