from django.test import TestCase, Client
from django.urls import reverse
from .models import Artikel, Makanan
from django.contrib.auth.models import User

class ArtikelModelTest(TestCase):
    def setUp(self):
        self.artikel = Artikel.objects.create(judul="Kuliner Jogja", konten="Isi artikel tentang kuliner Jogja")

    def test_artikel_str(self):
        self.assertEqual(str(self.artikel), self.artikel.judul)

    def test_artikel_tanggal_publikasi(self):
        self.assertIsNotNone(self.artikel.tanggal_publikasi)

class MakananModelTest(TestCase):
    def setUp(self):
        self.makanan = Makanan.objects.create(
            nama="Gudeg", deskripsi="Gudeg khas Jogja", kategori="Makanan Berat", 
            restoran="Gudeg Yu Djum", harga=25000, rating=4.5
        )

    def test_makanan_str(self):
        self.assertEqual(str(self.makanan), self.makanan.nama)

    def test_makanan_harga(self):
        self.assertGreaterEqual(self.makanan.harga, 0)

# class LandingPageTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.artikel = Artikel.objects.create(judul="Kuliner Jogja", konten="Isi artikel tentang kuliner Jogja")
#         self.makanan = Makanan.objects.create(
#             nama="Bakpia", deskripsi="Bakpia khas Jogja", kategori="Oleh-oleh", 
#             restoran="Bakpia Pathok 25", harga=50000, rating=4.7
#         )

#     def test_landing_page_status_code(self):
#         response = self.client.get(reverse('show_main'))
#         self.assertEqual(response.status_code, 200)

#     def test_landing_page_contains_makanan(self):
#         response = self.client.get(reverse('show_main'))
#         self.assertContains(response, self.makanan.nama)
#         self.assertContains(response, self.makanan.deskripsi)

#     def test_landing_page_contains_artikel(self):
#         response = self.client.get(reverse('show_main'))
#         self.assertContains(response, self.artikel.judul)
#         self.assertContains(response, self.artikel.konten)

# class UlasanTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(username='testuser', password='12345')
#         self.makanan = Makanan.objects.create(
#             nama="Oseng Mercon", deskripsi="Pedas luar biasa", kategori="Makanan Pedas", 
#             restoran="Oseng Mercon Bu Narti", harga=30000, rating=4.6
#         )

#     def test_unauthenticated_user_cannot_review(self):
#         response = self.client.get(reverse('add_review', kwargs={'makanan_id': self.makanan.id}))
#         self.assertEqual(response.status_code, 302)  # Redirect to login

#     def test_authenticated_user_can_review(self):
#         self.client.login(username='testuser', password='12345')
#         response = self.client.post(reverse('add_review', kwargs={'makanan_id': self.makanan.id}), {
#             'review': 'Ini sangat enak!', 'rating': 5
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Ini sangat enak!')

# class ProfilPenggunaTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(username='testuser', password='12345')

#     def test_profil_page_requires_login(self):
#         response = self.client.get(reverse('profil'))
#         self.assertEqual(response.status_code, 302)  # Redirect to login

#     def test_profil_page_loads_for_logged_in_user(self):
#         self.client.login(username='testuser', password='12345')
#         response = self.client.get(reverse('profil'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, self.user.username)

# class WishlistTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(username='testuser', password='12345')
#         self.makanan = Makanan.objects.create(
#             nama="Bakpia", deskripsi="Bakpia khas Jogja", kategori="Oleh-oleh", 
#             restoran="Bakpia Pathok 25", harga=50000, rating=4.7
#         )

#     def test_add_to_wishlist_requires_login(self):
#         response = self.client.post(reverse('add_to_wishlist', kwargs={'makanan_id': self.makanan.id}))
#         self.assertEqual(response.status_code, 302)  # Redirect to login

#     def test_logged_in_user_can_add_to_wishlist(self):
#         self.client.login(username='testuser', password='12345')
#         response = self.client.post(reverse('add_to_wishlist', kwargs={'makanan_id': self.makanan.id}))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "added to your wishlist")

#     def test_wishlist_shows_makanan(self):
#         self.client.login(username='testuser', password='12345')
#         self.client.post(reverse('add_to_wishlist', kwargs={'makanan_id': self.makanan.id}))
#         response = self.client.get(reverse('profil'))
#         self.assertContains(response, self.makanan.nama)
