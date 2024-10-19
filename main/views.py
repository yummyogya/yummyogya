from django.shortcuts import render, redirect
from .models import Makanan

def show_main(request):
    semua_makanan = Makanan.objects.all()
    context = {
        'nama_web' : "yummyogya",
        'makanan': semua_makanan,

    }

    return render(request, "main.html", context)