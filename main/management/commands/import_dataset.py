import csv
from django.core.management.base import BaseCommand
from main.models import Makanan

class Command(BaseCommand):
    help = 'Import data makanan dari CSV'

    def handle(self, *args, **kwargs):
        with open('C:/Users/denma/Desktop/Farrell/UI/SI/SMT 3/PBP/yummyogya/Dataset yummyogya.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Buat objek Makanan berdasarkan data di CSV
                Makanan.objects.create(
                    nama=row['Nama'],
                    deskripsi=row['Deskripsi'],
                    kategori=row['Kategori'],
                    restoran=row['Restoran'],
                    harga=row['Harga'],
                    rating=row['Rating'],
                    gambar=row.get('Foto', '')  # Kosongkan jika tidak ada gambar
                )
            self.stdout.write(self.style.SUCCESS('Data makanan berhasil diimport!'))
