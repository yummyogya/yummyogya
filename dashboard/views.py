# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from django.contrib.auth.decorators import login_required
from .forms import FoodForm
from django.http import JsonResponse


@login_required
def dashboard(request):
    sort_by = request.GET.get('sort_by', 'price')  # Default ke 'price'
    sort_order = request.GET.get('sort_order', 'asc')  # Default ke 'asc' (urutan naik)

    # Tentukan urutan berdasarkan sort_by dan sort_order
    if sort_by == 'name':
        foods = Food.objects.filter(created_by=request.user).order_by('name' if sort_order == 'asc' else '-name')
    else:  # Default ke pengurutan berdasarkan harga
        foods = Food.objects.filter(created_by=request.user).order_by('price' if sort_order == 'asc' else '-price')

    return render(request, 'dashboard.html', {'foods': foods, 'sort_by': sort_by, 'sort_order': sort_order})


# Add Food AJAX
@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.created_by = request.user
            food.save()
            
            
            # Cek apakah request berasal dari AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'food_name': food.name,
                    'message': 'Food added successfully!',
                })
            return redirect('dashboard:dashboard')
            
            # Redirect ke dashboard setelah makanan ditambah
    else:
        form = FoodForm()
    
    return render(request, 'add_food.html', {'form': form})


@login_required
def edit_food(request, pk):
    food = get_object_or_404(Food, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            
            # Cek apakah request berasal dari AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'food_name': food.name,
                    'message': 'Food updated successfully!',
                })
            return redirect('dashboard:dashboard')
    else:
        form = FoodForm(instance=food)

    return render(request, 'edit_food.html', {'form': form, 'food': food})


@login_required
def delete_food(request, pk):
    food = get_object_or_404(Food, pk=pk)  # Ini akan mengembalikan 404 jika tidak ada
    food.delete()
    return redirect('dashboard:dashboard')  