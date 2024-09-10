# Muffin Mart
## Nama : Fadhlurohman Dzaki
## Npm : 2306202132
## Link : https://fadhlurohman-dzaki-muffinmart.pbp.cs.ui.ac.id/

## Tugas 2 Implementasi MVT pada Django
### Cara implementasi checklist
1. Membuat _Repository_ baru bernama muffinmart di Github.
2. Melakukan _clone_ pada _repository_ tersebut ke penyimpanan lokal komputer
3. Membuat _virtual environment_ baru di direktori lokal dengan command:

    ```bash
        python -m venv env
        ```
4. Menyalakan _virtual environment_ Python baru dengan command:
    ```bash
    source env/bin/activate
    ```
5. Membuat file requirements.txt dengan isi :
    ```
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
        ```
6. Meng-_install requirements_ dengan pip
    ```bash
    Python -m pip install -r requirements.txt
    ```
7. Membuat proyek Django baru dengan command:
    ```bash
    django-admin startproject muffinmart .
    ```
8. Mengubah ```ALLOWED_HOSTS``` di file ```settings.py``` dengan menambahkan url deployment pws 

9. Membuat aplikasi ```main``` dengan command:
    ```bash
    python manage.py startapp main
    ```
10. Menambahkan nama aplikasi ke ```INSTALLED_APPS``` pada file ```settings.py``` di direktori ```muffinmart```

11. Me-_routing_ url pada file ```urls.py``` di direktori ```muffinmart``` sehingga isi file ```urls.py``` menjadi:
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```
12. Mengubah ```models.py``` menjadi:
    ```python
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        quantity = models.IntegerField()
    ```
13. Melakukan migrasi dengan command:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
14. Membuat direktori template dan template ```html``` untuk laman ```main```:

    ```html
    <h1>Muffin Mart</h1>

    <h5>Nama barang: </h5>
    <p>{{ name }}</p> 
    <h5>Harga: </h5>
    <p>{{ price }}</p> 
    <h5>Description: </h5>
    <p>{{ description }}</p> 
    <h5>Quantity: </h5>
    <p>{{ quantity }}</p>
    ```
15. Menambahkan fungsi untuk me-_render_ laman main pada file ```views.py```:
    ```python
    from django.shortcuts import render

  
    def show_main(request):
        context = {
            'name' : 'monitor',
            'price': '1000000',
            'description': 'gg gimang',
            'quantity': '1',
        }

        return render(request, "main.html", context)
    ```

16. Routing pada aplikasi ```main``` pada file ```urls.py``` di direktori main:
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
17. Mengetest aplikasi pada localhost dengan command:
    ```
    python manage.py runserver
    ```
    kemudian membuka ```http://localhost:8000/``` di _browser_

18. Melakukan deploy ke situs pws

### Bagan dan penjelasan

![](images\bagannnya.jpg)

Alur proses:

1. Client mengirim HTTP request ke web server.
2. Web server meneruskan request ke Django WSGI.
3. Django menggunakan urls.py untuk mencocokkan URL request dengan pola yang telah didefinisikan.
4. URL yang cocok akan diarahkan ke fungsi view yang sesuai di views.py.
5. View dapat berinteraksi dengan models.py untuk mengakses atau memanipulasi data jika diperlukan.
6. View kemudian merender template HTML, memasukkan data yang diperlukan.
7. Respons HTML final dikirim kembali ke client melalui web server.

Kaitan antara urls.py,views.py,models.py dan berkas html (templates):

1. urls.py:

- Berperan sebagai "traffic director" dalam aplikasi Django.
- Menentukan pola URL dan menghubungkannya dengan fungsi view yang sesuai.
- Ketika request masuk, Django akan mencocokkan URL dengan pola yang didefinisikan di sini.


2. views.py:

- Berisi logika bisnis aplikasi.
- Menerima request dari urls.py dan menentukan bagaimana request tersebut harus diproses.
- Berinteraksi dengan models.py untuk mengambil atau memanipulasi data jika diperlukan.
- Merender template HTML dan mengirimkan respons kembali ke client.


3. models.py:

- Mendefinisikan struktur dan perilaku data dalam database.
- Digunakan oleh views.py untuk mengakses dan memanipulasi data.
- Menyediakan abstraksi tingkat tinggi untuk operasi database.


4. Berkas HTML (Templates):

- Berisi struktur dan layout halaman web.
- Digunakan oleh views.py untuk merender respons HTML dinamis.
- Dapat menerima data dari views.py dan menampilkannya dalam format yang sesuai.

### Fungsi git pada pengembangan perangkat lunak

git berfungsi sebagai sistem kontrol versi yaitu alat yang berfungsi untuk melacak dan mengelola perubahan file dari waktu ke waktu.Git memungkinkan kolaborasi tim untuk pengembangan suatu perangkat lunak. Git memungkinkan developer untuk bekerja secara paralel pada fitur yang berbeda, menguji perubahan tanpa mengganggu kode utama, dan dengan mudah kembali ke versi sebelumnya jika diperlukan. Selain itu, Git juga membantu dalam manajemen rilis, dokumentasi proyek, dan menjaga keamanan kode dengan kontrol akses. Singkatnya, Git membuat proses pengembangan perangkat lunak lebih terstruktur, aman, dan efisien, terutama untuk proyek berskala besar dan tim yang terdistribusi.

### Kenapa django dijadikan permulaan awal pembelajaran perangkat lunak?

Menurut saya dipilihnya django karena django menggunakan bahasa pemrogramman python yang terkenal mudah untuk dipelajari bagi pemula dan sudah kita pelajari juga di mata kuliah DDP1.Selain itu di django juga dikenal istilah "batteries included" yang bermakna bahwa django hadir dengan banyak fitur-fitur bawaan yang memungkinkan pengembang untuk langsung membangun aplikasi web tanpa perlu menginstal atau mengonfigurasi banyak alat tambahan dari luar seperti flask,Express.js dan lain sebagainya.

### Kenapa model pada django disebut ORM?

Model pada Django disebut ORM (Object-Relational Mapping) karena fungsinya adalah untuk memetakan objek-objek di dalam kode Python ke tabel-tabel yang ada di basis data relasional. ORM memungkinkan developer untuk berinteraksi dengan basis data menggunakan bahasa pemrograman, dalam hal ini Python, tanpa perlu menulis query SQL secara langsung.Contoh :

```python
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        quantity = models.IntegerField()
    ```

dalam contoh diatas kelas Product merepresntasikan tabel di database dan setiap atributnya seperti name,price dan lain-lain akan menjadi kolom pada tabel tersebut.