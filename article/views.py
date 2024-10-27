from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse

# Data artikel statis
ARTICLESLIST = [
    {'id': 1, 'title': 'Sejarah Kuliner Jogja', 'content': 'Kuliner Yogyakarta memiliki akar sejarah...', 'published_date': '2022-01-01 12:00:00'},
    {'id': 2, 'title': 'Menikmati Kelezatan Mangut Lele Legendaris di Yogyakarta', 'content': 'Mangut lele merupakan salah satu makanan yang wajib...', 'published_date': '2023-01-02 12:00:00'},
    {'id': 3, 'title': 'Kulineran Makanan Khas Jogja di Teras Malioboro', 'content': 'Kuliner Jogja telah lama menjadi ikon...', 'published_date': '2024-01-03 12:00:00'},
    {'id': 4, 'title': 'Keistimewaan dan Sejarah Gudeg ', 'content': 'Hidangan gudeg pasti sudah tak asing...', 'published_date': '2024-01-03 12:00:00'},
    {'id': 5, 'title': 'Kuliner Yogyakarta di Masa Modern: Inovasi dengan Sentuhan Sejarah', 'content': 'Kota Yogyakarta merupakan kota yang banyak daya tariknya...', 'published_date': '2024-01-03 12:00:00'},
    {'id': 6, 'title': 'Dari Pasar Tradisional ke Restoran Mewah: Evolusi Kuliner Jogja', 'content': 'Kuliner Jogja kini tidak lagi terbatas di...', 'published_date': '2024-01-03 12:00:00'},
    {'id': 7, 'title': 'Kuliner Modern di Jogja', 'content': 'Yogyakarta, yang dikenal dengan kekayaan...', 'published_date': '2024-01-03 12:00:00'},
]

ARTICLESDETAIL = [
    {'id': 1, 'title': 'Sejarah Kuliner Jogja', 'content': '<p>Kuliner Yogyakarta memiliki akar sejarah panjang yang membentang dari masa kerajaan Mataram Kuno hingga zaman modern. Pada masa kerajaan, makanan tidak hanya berfungsi sebagai kebutuhan pokok, tetapi juga sebagai simbol kemakmuran dan status sosial. Hidangan-hidangan yang diracik dalam keraton dibuat dengan bahan pilihan dan disajikan dalam upacara-upacara adat yang sakral. Dengan dominasi bumbu lokal seperti kelapa, gula merah, dan rempah-rempah khas, makanan kerajaan ini berkembang menjadi hidangan yang lekat dengan nilai budaya dan tradisi masyarakat Jawa.</p><p> Seiring berjalannya waktu, kuliner Jogja terus berkembang tanpa kehilangan jati dirinya. Banyak hidangan seperti Gudeg, Kipo, dan Nasi Liwet yang pada mulanya hanya dikenal di lingkungan keraton, kini bisa dinikmati oleh masyarakat umum dan menjadi ikon kuliner kota ini. Resep-resep tradisional yang diwariskan dari generasi ke generasi ini masih dipertahankan hingga kini, meskipun mengalami penyesuaian sesuai dengan selera masyarakat modern. Kuliner Yogyakarta dengan cita rasa khas manis dan gurih menjadi daya tarik tersendiri bagi wisatawan lokal maupun mancanegara yang ingin merasakan kekayaan budaya melalui makanan. </p>', 'published_date': '2022-01-01 12:00:00'},
    {'id': 2, 'title': 'Menikmati Kelezatan Mangut Lele Legendaris di Yogyakarta', 'content': '<p>Mangut lele merupakan salah satu makanan yang wajib dikunjungi apabila ketika berkunjung ke yogyakarta. Bagi pecinta pedas makanan ini sangat recommended untuk dicoba, karena rasanya akan menggoyang lidah dan membuat bibir memerah karena kepedasan dan kenikmatannya yang beradu menjadi satu. Saya mengunjungi salah satu kedai mangut lele dikawasan jalan Parangtritis, kedai ini bernama "Mangut Lele Mbah Marto" Warung yang berada di tengah desa dan cukup sulit mencari lokasinya karena terlalu tersembunyi, akan tetapi warung ini selalu ramai dan tak pernah sepi pengunjung.</p><p> Di warung makan Mbah Marto, ikan lele dimasak dalam masakan mangut lele diasap bukan digoreng, citarasa lele asap yang pedas ini sangat berbeda dengan olahan lele pada umumnya. Apabila anda berkunjung ke yogyakarta, apabila anda pecinta pedas, anda harus mencoba kuliner satu ini di Yogyakarta.</p>', 'published_date': '2023-01-02 12:00:00'},
    {'id': 3, 'title': 'Kulineran Makanan Khas Jogja di Teras Malioboro', 'content': '<p>Kuliner Jogja telah lama menjadi ikon dan daya tarik utama bagi wisatawan yang datang ke kota ini. Ragam hidangan yang menggugah selera dan cita rasa yang tak tertandingi, Jogja menjadi surga bagi para pecinta dan para pelaku sosmed di bidang makanan. Nah bagi anda melalui artikel ini, kami akan membawa Anda dalam perjalanan kuliner yang mendalam, menjelajahi warisan kulinernya yang kaya dan merasakan kenikmatan makanan khas Jogja yang tak bisa Anda lewatkan.</p><p>Kuliner khas Jogja tersebut akan sangat mudah anda dapatkan di Malioboro  yang tak hanya sebagai tempat menikmati jantung kotanya Jogja tapi benar benar menjadi pusat oleh - oleh dan kulinernya Jogja, yuk kenali Malioboro lebih jauh, yang sekarang semakin rapi dan instagramable, Malioboro sendiri merupakan salah satu tempat yang selalu membuat setiap orang yang kesana merasa rindu akan romantisme dan suasana ramainya. Selain berada di pusat kota, Malioboro menjadi cukup dikenal karena cerita sejarah yang menyertainya. Keberadaan Malioboro sering pula dikaitkan dengan tiga tempat sakral di Yogya yakni Gunung Merapi, Kraton dan Pantai Selatan yang kini telah sah menjadi salah satu warisan kebudayaan dunia yang diakui UNESCO.<p>', 'published_date': '2024-01-03 12:00:00'},
    {'id': 4, 'title': 'Pengaruh Budaya Jawa dalam Kuliner Yogyakarta', 'content': '<p>Hidangan gudeg pasti sudah tak asing lagi di telinga masyarakat. Makanan yang satu ini sudah terkenal hingga mancanegara dan banyak digemari oleh pencinta kuliner karena cita rasanya yang lezat. Gudeg merupakan makanan asal Jogja yang bahan baku utamanya berasal dari nangka muda dan kemudian dimasak dengan santan. Umumnya, gudeg disajikan bersama nasi, areh, ayam, telur, tahu, dan juga sambal krecek. Karena dimasak dalam waktu yang lama bersama dengan daun jati, alhasil gudeg memiliki warna cokelat yang khas.</p><p> Nama gudeg berasal dari istilah dalam bahasa Jawa, yaitu hangudeg atau ngudheg yang berarti mengaduk. Ini merujuk pada proses pembuatannya yang sesekali diaduk dengan menggunakan centong agar tidak gosong. Istilah hangudeg juga dapat bermakna memasak nangka dengan santan dan daun melinjo di dalam kuali besar. Berkat dimasak dalam kurun waktu yang lama atau sekitar 5 jam, gudeg memiliki cita rasa istimewa yang cenderung manis. Namun jangan khawatir bagi pencinta pedas karena tingkat kepedasan dapat disesuaikan dengan menambahkan sambal krecek. Gudeg pun dapat disantap sebagai menu sarapan, makan siang atau makan malam. </p>', 'published_date': '2024-01-03 12:00:00'},
    {'id': 5, 'title': 'Kuliner Yogyakarta di Masa Modern: Inovasi dengan Sentuhan Sejarah', 'content': '<p>Kota Yogyakarta merupakan kota yang banyak daya tariknya sejak kota ini dibentuk dari masyarakatnya sampai dengan kulinernya, Kota Yogyakarta merupakan kota pariwisata kedua di Indonesia setelah Pulau Bali. Kuliner di Yogyakarta khas terkait dengan keberadaan Keraton Yogyakarta. Menurut Murdijati Gardjito dkk dalam buku : Kuliner Yogyakarta pantas dikenang sepanjang masa, PT Gramedia Pustaka Utama, 2017 salah satunya menyebutkan bahwa tradisi di lingkungan keraton, keluarga keraton di luar pagar keraton, maupun masyarakat umum mempunyai kebiasaan menu yang berbeda-beda. Sehingga ragam kuliner rumahan, lauk pauk maupun kudapannya lebih banyak macamnya. Keragaman kuliner ini didukung banyaknya pasar tradisional yang tetap ramai di tengah marak hadirnya pasar modern. Keberadaan pasar adalah pembelajaran kuliner yang baku.</p><p> Namun demikian permasalahan tetaplah ada, seperti pelaku kegiatan kuliner kudapan tradisional sekarang ini sulit diketemukan karena pelaku nya adalah generasi tua yang sulit untuk menemukan generasi penerusnya. Anak cucunya lebih senang membuka toko roti dibanding membuat makanan tradisional yang repot, dibuat satu persatu tidak bisa masinal. Sebagai kota pariwisata hal ini perlu dipertimbangkan regenerasi tersebut.</p>', 'published_date': '2024-01-03 12:00:00'},
    {'id': 6, 'title': 'Dari Pasar Tradisional ke Restoran Mewah: Evolusi Kuliner Jogja', 'content': '<p>Kuliner Jogja kini tidak lagi terbatas di pasar-pasar tradisional atau angkringan, tetapi juga dapat dinikmati di restoran-restoran mewah. Di pasar tradisional, makanan khas seperti pecel, sate klathak, dan wedang ronde dijual dengan harga terjangkau dan disajikan dalam suasana yang sederhana. Sementara itu, restoran-restoran modern di Jogja kini mulai mengusung konsep penyajian kuliner lokal dengan sentuhan mewah, menawarkan pengalaman bersantap yang berbeda tetapi tetap mempertahankan cita rasa asli.</p><p>Transformasi ini mencerminkan fleksibilitas kuliner Jogja dalam menyesuaikan diri dengan perkembangan zaman. Wisatawan kini memiliki banyak pilihan untuk menikmati kuliner khas Jogja, mulai dari suasana tradisional yang penuh nostalgia hingga restoran modern yang menawarkan kenyamanan dan kemewahan. Dengan berbagai pilihan tempat, kuliner Yogyakarta tetap menjadi daya tarik utama yang membawa cerita sejarah dan budaya bagi siapa saja yang berkunjung ke kota ini.</p>', 'published_date': '2024-01-03 12:00:00'},
    {'id': 7, 'title': 'Kuliner Modern di Jogja', 'content': '<p>Yogyakarta, yang dikenal dengan kekayaan budaya dan kuliner tradisionalnya, kini juga menjadi kota yang penuh inovasi kuliner modern. Di berbagai sudut kota, bermunculan kafe dan restoran yang menawarkan berbagai hidangan dari masakan fusion hingga western dengan sentuhan lokal. Banyak restoran yang menyajikan makanan seperti pizza gudeg, ramen Jawa, dan burger rendang, memadukan rasa tradisional dengan konsep modern yang menarik. Keunikan ini disambut baik oleh generasi muda yang menggemari cita rasa baru tetapi tetap ingin terhubung dengan akar budaya lokal.</p><p>Kuliner modern ini tidak hanya menarik dari segi rasa, tetapi juga dalam konsep tempat dan penyajian yang instagramable, menjadikannya daya tarik tersendiri bagi wisatawan. Selain menawarkan menu kreatif, beberapa tempat juga menghadirkan pengalaman makan dengan konsep unik, seperti rooftop cafe dengan pemandangan alam Yogyakarta atau restoran dengan tema keraton modern. Perpaduan antara elemen tradisional dan modern ini berhasil menciptakan atmosfer yang berbeda di Jogja, membuat kuliner modern menjadi bagian penting dari daya tarik wisata kuliner di kota ini.</p>', 'published_date': '2024-01-03 12:00:00'},
]

# Artikel diperoleh dari:
# chatgpt.com
# https://www.kompasiana.com/imroahqurotulaini6554/66f6b95734777c74b776fc54/menikmati-kelezatan-mangut-lele-legendaris-di-yogyakarta
# https://www.kompasiana.com/oktavianiayu/65195de1ae1f0766206071f2/kulineran-makanan-khas-jogja-di-teras-malioboro?page=2&page_images=1
# https://www.detik.com/jogja/kuliner/d-7068653/gudeg-berasal-dari-ini-sejarah-keistimewaan-dan-resep-cara-membuatnya
# https://jogjaheritagesociety.org/kegiatan/keunggulan/7-nilai-mahakarya-seni-tradisi-dan-kontemporer/kuliner-kota-yogyakarta/

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

def article_detail(request, id):
    article = next((item for item in ARTICLESDETAIL if item["id"] == id), None)
    return render(request, 'article_detail.html', {'article': article})