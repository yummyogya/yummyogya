from django.shortcuts import render
from main.models import Makanan
from django.core.paginator import Paginator

def search_makanan_view(request):
    query = request.GET.get('q', '')
    makanan_list = Makanan.objects.filter(nama__icontains=query) if query else Makanan.objects.all()

    paginator = Paginator(makanan_list, 9)  # 9 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'page_obj': page_obj
    }
    return render(request, 'searchpage/search.html', context)
