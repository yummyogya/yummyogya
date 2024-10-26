from django.shortcuts import render


# View untuk menampilkan daftar artikel
def article_list(request):
    # Daftar artikel dengan data disimpan dalam dictionary
    articles = [
        {'id': 1, 'title': 'Sejarah Kuliner Jogja', 'content': 'Yogyakarta memiliki sejarah kuliner yang kaya...', 'published_date': '2022-01-01 12:00:00'},
        {'id': 2, 'title': 'Makanan Tradisional Yogyakarta', 'content': 'Makanan tradisional seperti Gudeg...', 'published_date': '2023-01-02 12:00:00'},
        {'id': 3, 'title': 'Kuliner Modern di Jogja', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...', 'published_date': '2024-01-03 12:00:00'},
    ]
    return render(request, 'article_list.html', {'articles': articles})

# View untuk menampilkan detail artikel
def article_detail(request, id):
    # Mencari artikel berdasarkan ID dari dictionary
    articles = [
        {'id': 1, 'title': 
         'Sejarah Kuliner Jogja', 
         'content': 'Yogyakarta memiliki sejarah kuliner yang kaya, dipengaruhi oleh perpaduan tradisi Jawa, budaya keraton, dan pengaruh dari berbagai daerah di Indonesia maupun mancanegara. Kuliner di Yogyakarta tidak hanya sekadar makanan; ia mencerminkan sejarah panjang dan kearifan lokal yang diwariskan dari generasi ke generasi. Banyak hidangan di Yogyakarta yang lahir dari dapur keraton, diolah dengan teknik khusus dan menggunakan bahan-bahan alami yang berasal dari tanah Jawa. Hidangan seperti gudeg, brongkos, dan nasi kucing bukan hanya populer di kalangan masyarakat lokal, tetapi juga menjadi incaran wisatawan yang ingin merasakan kelezatan kuliner khas Jogja. \n\
            Salah satu kuliner ikonik Yogyakarta adalah gudeg, yang sering disebut sebagai "The Taste of Jogja". Gudeg merupakan olahan nangka muda yang dimasak dengan santan dan gula kelapa dalam waktu yang cukup lama hingga menghasilkan cita rasa manis dan warna kecokelatan yang khas. Hidangan ini biasanya disajikan dengan ayam kampung, telur, tahu, dan krecek, memberikan keseimbangan rasa yang memanjakan lidah. Sejarahnya, gudeg pertama kali dikenal di kalangan masyarakat keraton sebagai makanan yang disajikan dalam acara-acara penting, namun seiring waktu menjadi populer di seluruh lapisan masyarakat Yogyakarta. \n\
            Tidak hanya rasa yang menjadi keistimewaan kuliner Yogyakarta, tetapi juga filosofi yang terkandung di dalamnya. Banyak makanan tradisional yang melambangkan nilai-nilai kehidupan seperti kesederhanaan, kesabaran, dan rasa syukur. Misalnya, gudeg yang dimasak dalam waktu lama mencerminkan filosofi Jawa tentang ketekunan dan kesabaran dalam mencapai sesuatu. Demikian pula dengan hidangan-hidangan lain yang mengutamakan penggunaan bahan-bahan lokal dan cara masak alami. Kuliner di Yogyakarta menjadi sarana untuk memahami lebih dalam tentang budaya dan nilai-nilai masyarakatnya yang ramah dan bersahaja.'},
        {'id': 2, 'title': 'Makanan Tradisional Yogyakarta', 'content': 'Makanan tradisional seperti Gudeg...'},
        {'id': 3, 'title': 'Kuliner Modern di Jogja', 'content': 'Selain makanan tradisional, Jogja juga menawarkan kuliner modern...'},
    ]
    
    article = next((item for item in articles if item["id"] == id), None)
    return render(request, 'article_detail.html', {'article': article})
