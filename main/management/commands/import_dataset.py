import csv
from django.core.management.base import BaseCommand
from main.models import Makanan

class Command(BaseCommand):
    help = 'Import data makanan dari CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):

        csv_file_path = kwargs['csv_file']
        
        with open(csv_file_path, mode='r') as file:
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
