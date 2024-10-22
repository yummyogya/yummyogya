from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist, Food
from django.contrib.auth.decorators import login_required

@login_required
def add_to_wishlist(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.food.add(food)
    return redirect('landing_page')  

@login_required
def view_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': wishlist})

@login_required
def remove_from_wishlist(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist.food.remove(food)
    return redirect('view_wishlist')  # Redirect back to the wishlist page