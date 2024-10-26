# details/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Review  # Pastikan Anda memiliki model Review
from main.models import Makanan
from dashboard.models import Food
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def add_review(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        rating = data.get('rating')
        review_text = data.get('review')
        food_id = data.get('food_id')
        
        # Ambil objek food dan simpan ulasan
        food = Makanan.objects.get(id=food_id) if food_id else None
        if food and request.user.is_authenticated:
            review = Review.objects.create(
                user=request.user,
                food=food,
                review=review_text,
                rating=rating
            )
            return JsonResponse({'message': 'Review added successfully!', 'status': 'success'})
        return JsonResponse({'message': 'Failed to add review', 'status': 'error'})
    return JsonResponse({'message': 'Invalid request method', 'status': 'error'})

def food_detail(request, item_id):
    # Coba dapatkan item dari model Makanan terlebih dahulu
    item = Makanan.objects.filter(pk=item_id).first()
    if not item:
        # Jika tidak ada di Makanan, coba cari di model Food
        item = Food.objects.filter(pk=item_id).first()
        if not item:
            # Jika tidak ada di kedua model, kembalikan halaman 404
            return render(request, '404.html')  # Pastikan '404.html' ada di templates folder

    # Struktur konteks yang mendukung kedua model
    item_context = {
        'id': item.id,
        'nama': getattr(item, 'nama', item.name),
        'deskripsi': getattr(item, 'deskripsi', item.description),
        'harga': getattr(item, 'harga', item.price),
        'rating': item.rating,
        'gambar': getattr(item, 'gambar', item.image_url),
        'restoran': getattr(item, 'restoran', item.restaurant)
    }

    return render(request, 'details/food_detail.html', {'item': item_context})

