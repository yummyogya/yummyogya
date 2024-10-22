# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from django.contrib.auth.decorators import login_required
from .forms import FoodForm

# ini di main.views apa di file ini ya?

# def landing_page(request): 
#     foods = Food.objects.all()
#     return render(request, 'landing_page.html', {'foods': foods})

@login_required
def dashboard(request):
    foods = Food.objects.filter(created_by=request.user)
    return render(request, 'dashboard.html', {'foods': foods})

@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.created_by = request.user
            food.save()
            return redirect('dashboard')
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
            return redirect('dashboard')
    else:
        form = FoodForm(instance=food)
    return render(request, 'edit_food.html', {'form': form})

@login_required
def delete_food(request, pk):
    food = get_object_or_404(Food, pk=pk, created_by=request.user)
    if request.method == 'POST':
        food.delete()
        return redirect('dashboard')
    return render(request, 'delete_food.html', {'food': food})