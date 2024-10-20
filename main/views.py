from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.core import serializers
from .models import Makanan

def show_main(request):
    query = request.GET.get('q')  # Ambil query dari search bar
    if query:
        semua_makanan = Makanan.objects.filter(nama__icontains=query)  # Filter berdasarkan nama makanan
    else:
        semua_makanan = Makanan.objects.all()  # Ambil semua data makanan jika tidak ada pencarian

    semua_makanan = Makanan.objects.all()
    paginator = Paginator(semua_makanan, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'nama_web' : "yummyogya",
        'makanan': semua_makanan,
        'page_obj': page_obj,
        'query': query 
    }

    return render(request, "main.html", context)

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