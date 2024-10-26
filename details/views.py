# details/views.py
from django.shortcuts import render, get_object_or_404
from main.models import Makanan
from dashboard.models import Food

def food_detail(request, item_id):
    # Coba dapatkan item dari model Makanan terlebih dahulu
    item = Makanan.objects.filter(pk=item_id).first()
    if not item:
        # Jika tidak ada di Makanan, coba cari di model Food
        item = Food.objects.filter(pk=item_id).first()
        if not item:
            # Jika tidak ada di kedua model, kembalikan halaman 404
            return render(request, '404.html')

    # Sesuaikan struktur konteks agar item bisa digunakan baik dari model Makanan atau Food
    item_context = {
        'id': item.id,
        'nama': getattr(item, 'nama', item.name),
        'deskripsi': getattr(item, 'deskripsi', item.description),
        'harga': item.harga if isinstance(item, Makanan) else item.price,
        'rating': item.rating,
        'gambar': getattr(item, 'gambar', item.image_url),
        'restoran': getattr(item, 'restoran', item.restaurant)
    }

    return render(request, 'details/food_detail.html', {'item': item_context})

