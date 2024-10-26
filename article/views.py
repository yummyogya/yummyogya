from django.shortcuts import render

# View untuk menampilkan daftar artikel
def article_list(request):
    # Daftar artikel dengan data disimpan dalam dictionary
    articles = [
        {'id': 1, 'title': 'Sejarah Kuliner Jogja', 'content': 'Yogyakarta memiliki sejarah kuliner yang kaya...'},
        {'id': 2, 'title': 'Makanan Tradisional Yogyakarta', 'content': 'Makanan tradisional seperti Gudeg...'},
        {'id': 3, 'title': 'Kuliner Modern di Jogja', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...'},
    ]
    return render(request, 'article_list.html', {'articles': articles})

# View untuk menampilkan detail artikel
def article_detail(request, id):
    # Mencari artikel berdasarkan ID dari dictionary
    articles = [
        {'id': 1, 'title': 'Sejarah Kuliner Jogja', 'content': 'Yogyakarta memiliki sejarah kuliner yang kaya...'},
        {'id': 2, 'title': 'Makanan Tradisional Yogyakarta', 'content': 'Makanan tradisional seperti Gudeg...'},
        {'id': 3, 'title': 'Kuliner Modern di Jogja', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...'},
    ]
    
    article = next((item for item in articles if item["id"] == id), None)
    return render(request, 'article_detail.html', {'article': article})
