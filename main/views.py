from django.http import HttpResponse
from django.core import serializers# main/views.py
# main/views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Makanan
from dashboard.models import Food

def show_main(request):
    query = request.GET.get('q')
    
    # Ambil makanan dari model Makanan dan Food (dashboard)
    semua_makanan = Makanan.objects.filter(nama__icontains=query) if query else Makanan.objects.all()
    user_makanan = Food.objects.filter(name__icontains=query) if query else Food.objects.all()

    # Gabungkan hasil dari dua model
    combined_makanan = list(semua_makanan) + list(user_makanan)

    # Pagination
    paginator = Paginator(combined_makanan, 10)  # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'nama_web': "yummyogya",
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, "main.html", context)

# Fungsi untuk handling request AJAX
def search_ajax(request):
    query = request.GET.get('q', '')
    makanan_list = Makanan.objects.filter(nama__icontains=query) if query else Makanan.objects.all()
    user_makanan_list = Food.objects.filter(name__icontains=query) if query else Food.objects.all()

    combined_makanan = list(makanan_list) + list(user_makanan_list)
    
    # Mengemas hasil pencarian menjadi format JSON yang dapat di-render
    makanan_data = []
    for makanan in combined_makanan:
        if isinstance(makanan, Makanan):  # Jika dari model Makanan
            makanan_data.append({
                'id': makanan.id,
                'nama': makanan.nama,
                'deskripsi': makanan.deskripsi,
                'harga': makanan.harga,
                'rating': makanan.rating,
                'gambar': makanan.gambar,
                'restoran': makanan.restoran
            })
        elif isinstance(makanan, Food):  # Jika dari model Food
            makanan_data.append({
                'id': makanan.id,
                'nama': makanan.name,
                'deskripsi': makanan.description,
                'harga': makanan.price,
                'rating': makanan.rating,
                'gambar': makanan.image_url,
                'restoran': makanan.restaurant
            })

    return JsonResponse({'makanan_list': makanan_data})


def show_xml(request):
    data = Makanan.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Makanan.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Makanan.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Makanan.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")