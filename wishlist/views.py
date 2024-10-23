from django.shortcuts import render, redirect
from .models import Food, Wishlist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

@login_required
def add_to_wishlist(request, food_id):
    food = Food.objects.filter(id=food_id).first()
    
    if food is None:
        messages.error(request, "Food item not found.")
        return redirect('wishlist:view_wishlist')

    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.foods.add(food)
    
    wishlist_count = wishlist.foods.count()
    
    if request.is_ajax():
        return JsonResponse({'wishlist_count': wishlist_count}, status=200)
    
    messages.success(request, f'{food.name} has been added to your wishlist!')
    return redirect('wishlist:view_wishlist')

def view_wishlist(request):
    wishlist = Wishlist.objects.get(user=request.user)  
    context = {'wishlist': wishlist}
    return render(request, 'wishlist.html', context)

@login_required
def remove_from_wishlist(request, food_id):
    food = Food.objects.filter(id=food_id).first()
    
    if food is None:
        messages.error(request, "Food item not found.")
        return redirect('wishlist:view_wishlist')

    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.foods.remove(food)
    
    messages.success(request, f'{food.name} has been removed from your wishlist.')
    return redirect('wishlist:view_wishlist')
