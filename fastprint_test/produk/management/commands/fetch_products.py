import requests
from hashlib import md5
from datetime import datetime
from django.core.management.base import BaseCommand
from produk.models import Produk, Kategori, Status

class Command(BaseCommand):
    help = "Fetch products from Fastprint API and save to DB"

    def handle(self, *args, **options):
        # ---Password---
        today = datetime.now()
        raw_password = f"bisacoding-{today.day}-01-{str(today.year)[-2:]}"
        password_md5 = md5(raw_password.encode()).hexdigest()

        # ---Username---
        username = "tesprogrammer290126C23"
        # ---API Request---
        url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
        response = requests.post(url, data={ "username": username, "password": password_md5 })
        data = response.json()
        # Debug respons
        print("username:", username) 
        print("raw password:", raw_password) 
        print("md5 password:", password_md5) 
        print("API response:", data)
        
        # ---Save to DB---
        for item in data['data']:
            kategori, _ = Kategori.objects.get_or_create(nama_kategori=item['kategori'])
            status, _ = Status.objects.get_or_create(nama_status=item['status'])

            Produk.objects.update_or_create(
                id_produk=int(item['id_produk']),
                defaults={
                    'nama_produk': item['nama_produk'],
                    'harga': int(item['harga']),
                    'kategori': kategori,
                    'status': status
                }
            )
        self.stdout.write(self.style.SUCCESS("Products imported successfully!"))

        