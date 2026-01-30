# Tes Junior Programmer Fast Print-Kenneth

## Tech Stack
- **Backend**: Django 5.x, Django REST Framework.
- **Database**: MySQL.
- **Frontend**: Django Template + Bootstrap.
- **Tools**: Python 3.12, pip, virtualenv.

---

## Struktur Proyek
```
fastprint_test/
├── fastprint_test/        # Settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── produk/                # Aplikasi
│   ├── models.py
│   ├── views.py           # HTML views
│   ├── views_api.py       # API views (DRF)
│   ├── serializers.py     # DRF serializers
│   ├── forms.py           # Django forms
│   ├── urls.py
│   └── templates/produk/  # HTML templates
└── manage.py
```

## Mulai Aplikasi

### 1. Clone Repository
```
git clone https://github.com/yourusername/fastprint-product.git
cd fastprint-product
```

### 2. Setup Environtment
Membuat Virtual Environment dan Install Dependensi
```
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 3. Konfigurasi Database
1. Buat database menggunakan MySQL
```
CREATE DATABASE fastprint_db;
```
2. Edit fastprint_test/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fastprint_db',
        'USER': 'root',
        'PASSWORD': '[Password Anda]',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Notes : Ganti [Password Anda] dengan Password MySQL server anda
### 4. Menjalankan migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Start server
```
python manage.py runserver
```

## Akses
- HTML CRUD: http://127.0.0.1:8000/ 
- API JSON: http://127.0.0.1:8000/api/produk/

## API Endpoint
•	GET /api/produk/ untuk menampilkan daftar produk.
•	GET /api/produk/{id}/ untuk menampilkan detail produk berdasarkan ID.
•	POST /api/produk/ untuk menambahkan produk baru.
•	PUT /api/produk/{id}/ untuk memperbarui data produk.
•	DELETE /api/produk/{id}/ untuk menghapus produk.

