from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile

# Create your tests here.

class ProfileTest(TestCase):
    def setUp(self):
        # Buat user dan profile untuk testing
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        Profile.objects.create(user=self.user)

    def test_show_profile_url_is_exist(self):
        # Test untuk mengecek apakah halaman profil bisa diakses
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profilepage:show_profile'))
        self.assertEqual(response.status_code, 200)

    def test_show_profile_using_correct_template(self):
        # Test untuk mengecek apakah halaman profil menggunakan template yang benar
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profilepage:show_profile'))
        self.assertTemplateUsed(response, 'profile.html')

    def test_update_profile_functionality(self):
        # Test untuk mengecek apakah update profile berfungsi dengan benar
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('profilepage:update_profile'), {
            'bio': 'Updated bio',
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})

    def test_change_password_functionality(self):
        # Test untuk mengecek apakah ganti password berfungsi dengan benar
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('profilepage:change_password'), {
            'old_password': 'testpassword',
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123',
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})

    def test_nonexistent_page(self):
        # Test untuk mengecek apakah halaman yang tidak ada memberikan respons 404
        response = self.client.get('/halaman-tidak-ada/')
        self.assertEqual(response.status_code, 404)