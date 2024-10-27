# article/views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse

# Data artikel statis
ARTICLESLIST = [
    {'id': 1, 'title': 'Sejarah Kuliner Jogja', 'content': 'Yogyakarta memiliki sejarah kuliner yang kaya...', 'published_date': '2022-01-01 12:00:00'},
    {'id': 2, 'title': 'Jejak Kolonial dalam Kuliner Yogyakarta: Adaptasi dan Inovasi Rasa', 'content': 'Makanan tradisional seperti Gudeg...', 'published_date': '2023-01-02 12:00:00'},
    {'id': 3, 'title': 'Gudeg: Simbol Kuliner Jogja dari Masa ke Masa', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...', 'published_date': '2024-01-03 12:00:00'},
    {'id': 4, 'title': 'Pengaruh Budaya Jawa dalam Kuliner Yogyakarta', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...', 'published_date': '2024-01-03 12:00:00'},
    {'id': 5, 'title': 'Kuliner Yogyakarta di Masa Modern: Inovasi dengan Sentuhan Sejarah', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...', 'published_date': '2024-01-03 12:00:00'},
    {'id': 6, 'title': 'Dari Pasar Tradisional ke Restoran Mewah: Evolusi Kuliner Jogja', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...', 'published_date': '2024-01-03 12:00:00'},
    {'id': 7, 'title': 'Kuliner Modern di Jogja', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...', 'published_date': '2024-01-03 12:00:00'},
]

ARTICLESDETAIL = [
    {'id': 1, 'title': 'Sejarah Kuliner Jogja', 'content': 'Yogyakarta memiliki sejarah kuliner yang kaya...', 'published_date': '2022-01-01 12:00:00'},
    {'id': 2, 'title': 'Makanan Tradisional Yogyakarta', 'content': 'Makanan tradisional seperti Gudeg...', 'published_date': '2023-01-02 12:00:00'},
    {'id': 3, 'title': 'Kuliner Modern di Jogja', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...', 'published_date': '2024-01-03 12:00:00'},
    {'id': 4, 'title': 'Kuliner Modern di Jogja', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...', 'published_date': '2024-01-03 12:00:00'},
    {'id': 5, 'title': 'Kuliner Modern di Jogja', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...', 'published_date': '2024-01-03 12:00:00'},
    {'id': 6, 'title': 'Kuliner Modern di Jogja', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...', 'published_date': '2024-01-03 12:00:00'},
    {'id': 7, 'title': 'Kuliner Modern di Jogja', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...', 'published_date': '2024-01-03 12:00:00'},
]

# View untuk menampilkan daftar artikel
def article_list(request):
    paginator = Paginator(ARTICLESLIST, 3)  # 3 artikel per halaman
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        articles_data = []
        for article in page_obj:
            articles_data.append({
                'id': article['id'],
                'title': article['title'],
                'content': article['content'],
                'published_date': article['published_date'],
            })
        return JsonResponse({
            'articles': articles_data,
            'has_next': page_obj.has_next()
        })

    return render(request, 'article_list.html', {'page_obj': page_obj})

# View untuk menampilkan detail artikel
def article_detail(request, id):
    article = next((item for item in ARTICLESDETAIL if item["id"] == id), None)
    return render(request, 'article_detail.html', {'article': article})