Dalam pemrograman berorientasi objek (OOP), metode adalah fungsi atau prosedur yang didefinisikan dalam sebuah kelas dan digunakan untuk menggambarkan perilaku objek yang diciptakan dari kelas tersebut. Metode adalah bagian integral dari OOP karena memungkinkan objek untuk "melakukan" tindakan atau berinteraksi dengan data yang ada di dalamnya.

Berikut adalah beberapa jenis metode dalam OOP:

1. Metode Instans
Definisi: Metode yang beroperasi pada instance atau objek yang dibuat dari kelas. Metode ini bisa mengakses dan mengubah data spesifik yang dimiliki oleh objek.
Contoh:

class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def deskripsi(self):
        return f"Mobil {self.merk} berwarna {self.warna}."

2. Metode Kelas
Definisi: Metode yang beroperasi pada kelas itu sendiri, bukan objek tertentu. Metode ini didefinisikan dengan menggunakan @classmethod. Metode ini memiliki parameter pertama cls, yang merujuk pada kelas, bukan objek.
Contoh:

class Mobil:
    jumlah_mobil = 0

    @classmethod
    def tambah_mobil(cls):
        cls.jumlah_mobil += 1
        return cls.jumlah_mobil

3. Metode Statis
Definisi: Metode yang tidak tergantung pada objek atau kelas, dan tidak memiliki akses ke self atau cls. Didefinisikan menggunakan @staticmethod. Metode ini berfungsi untuk melakukan tugas tertentu yang tidak bergantung pada data objek atau kelas.
Contoh:

class Mobil:
    @staticmethod
    def hitung_jarak(waktu, kecepatan):
        return waktu * kecepatan

4. Metode Konstruktor
Definisi: Metode khusus yang dipanggil secara otomatis ketika objek dari kelas tersebut dibuat. Dalam Python, metode konstruktor adalah __init__. Metode ini digunakan untuk menginisialisasi atribut objek.
Contoh:

class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

5. Metode Destruktor
Definisi: Metode khusus yang dipanggil saat objek dihapus atau dihancurkan. Dalam Python, destruktor menggunakan __del__. Metode ini jarang digunakan, kecuali untuk membersihkan sumber daya yang dialokasikan oleh objek.
Contoh:

class Mobil:
    def __del__(self):
        print(f"Mobil {self.merk} dihancurkan.")

6. Metode Akses (Getter dan Setter)
Definisi: Metode yang digunakan untuk mengakses atau mengubah nilai atribut yang biasanya bersifat privat atau terlindungi dalam objek. Biasanya dinamakan dengan awalan get_ untuk getter dan set_ untuk setter.
Contoh:

class Mobil:
    def __init__(self, merk):
        self._merk = merk

    def get_merk(self):
        return self._merk

    def set_merk(self, merk):
        self._merk = merk


KAITAN DENGAN TUGAS 3 :       

1. Konstruktor (__init__)
> Deskripsi: Metode ini adalah konstruktor dari kelas Konoha. Metode ini dipanggil ketika objek baru dari kelas ini dibuat.
> Fungsi: Konstruktor menerima sebuah string yang dienkode (encoded_str) sebagai parameter dan menginisialisasi dua atribut:
- self.encoded_str: Menyimpan string yang diterima.
- self.sum_digits: Menyimpan jumlah digit yang ditemukan dalam string (diinisialisasi dengan 0).
- self.letters: Menyimpan daftar huruf yang diambil dari string (diinisialisasi sebagai list kosong).

2. Metode Instans: calculate_sum_of_digits()
> Deskripsi: Metode ini digunakan untuk menghitung jumlah total digit dalam encoded_str.
> Fungsi: Setiap karakter dalam encoded_str diperiksa menggunakan char.isdigit(). Jika karakter tersebut adalah digit, nilai digit tersebut diubah menjadi integer dan ditambahkan ke self.sum_digits.

3. Metode Instans: collect_letters()
> Deskripsi: Metode ini digunakan untuk mengumpulkan hanya huruf-huruf dari string yang dienkode.
> Fungsi: Setiap karakter dalam encoded_str diperiksa menggunakan char.isalpha(). Jika karakter tersebut adalah huruf, maka huruf tersebut akan ditambahkan ke list self.letters.


KAITKAN DENGAN TUGAS 4 :

1. Metode Instans: read_file()
> Deskripsi: Metode ini digunakan untuk membuka file yang ditentukan dan membaca isinya, lalu menyimpan setiap baris dalam list self.lines. Selain itu, jumlah karakter per baris juga dihitung dan disimpan dalam list self.char_counts.
> Fungsi:
Membuka file dalam mode baca dan membaca setiap baris menggunakan readlines().
Menggunakan list comprehension untuk menghitung jumlah karakter per baris dan menyimpannya dalam self.char_counts.

2. Metode Instans: calculate_stats()
> Deskripsi: Metode ini menghitung statistik terkait jumlah karakter per baris, yaitu nilai minimum, maksimum, dan rentang dari jumlah karakter per baris.
> Fungsi:
Menggunakan fungsi built-in min() untuk mencari nilai terkecil (minimum) dan max() untuk mencari nilai terbesar (maksimum) dari list self.char_counts.
Rentang dihitung dengan mengurangi nilai maksimum dan minimum.

3. Metode Instans: write_output()
> Deskripsi: Metode ini menulis hasil perhitungan statistik (minimum, maksimum, dan rentang jumlah karakter per baris) ke dalam file yang sama setelah dihitung.
> Fungsi:
Membuka file dalam mode append ("a") agar hasil statistik ditambahkan tanpa menghapus isi file yang ada.
Menulis hasil statistik berupa min, max, dan range ke file setelah informasi file asli (jika ada).

4. Metode Instans: write_null()
> Deskripsi: Metode ini digunakan untuk menangani kasus ketika file yang dibaca kosong. Dalam hal ini, metode ini menulis kata 'NULL' ke dalam file sebagai indikator bahwa file tidak berisi teks.
> Fungsi:
Membuka file dalam mode tulis ("w") untuk menulis ulang isi file dengan teks 'NULL\n'.
Menampilkan pesan ke layar bahwa file kosong dan 'NULL' telah ditulis ke dalam file.


KAITKAN DENGAN TUGAS 5 :

1. Kelas Keranjang
Metode __init__ (Konstruktor)
> Deskripsi: Konstruktor kelas Keranjang dipanggil saat sebuah objek Keranjang dibuat. Metode ini menerima dua parameter, yaitu nama dan kapasitas, yang digunakan untuk menginisialisasi atribut objek tersebut.
> Fungsi:
self.nama menyimpan nama keranjang.
self.kapasitas menyimpan kapasitas keranjang.

2. Kelas DekDepe
Metode __init__ (Konstruktor)
> Deskripsi: Konstruktor dari kelas DekDepe bertugas untuk menginisialisasi atribut self.daftar_keranjang, yang merupakan list kosong yang akan digunakan untuk menyimpan objek-objek Keranjang.
> Fungsi:
self.daftar_keranjang adalah list yang menampung semua keranjang yang ditambahkan.

> Metode beli
Deskripsi: Metode ini digunakan untuk menambahkan objek Keranjang baru ke dalam self.daftar_keranjang dengan parameter nama dan kapasitas yang diberikan.
Fungsi:
Menambahkan objek Keranjang baru ke dalam list self.daftar_keranjang dan menampilkan pesan konfirmasi.

> Metode jual
Deskripsi: Metode ini digunakan untuk menghapus objek Keranjang dari self.daftar_keranjang berdasarkan indeks yang diberikan.
Fungsi:
Menghapus objek keranjang dari daftar dengan menggunakan pop() dan menampilkan pesan konfirmasi.
Jika indeks tidak valid, menampilkan pesan error.

> Metode ubah_kapasitas
Deskripsi: Metode ini digunakan untuk mengubah kapasitas dari keranjang yang berada pada indeks tertentu dalam daftar.
Fungsi:
Mengubah atribut kapasitas dari objek Keranjang yang ada pada indeks tertentu dan menampilkan pesan konfirmasi.
Jika indeks tidak valid, menampilkan pesan error.

> Metode ubah_nama
Deskripsi: Metode ini digunakan untuk mengubah nama dari keranjang yang ada pada indeks tertentu.
Fungsi:
Mengubah atribut nama dari objek Keranjang yang ada pada indeks tertentu dan menampilkan pesan konfirmasi.
Jika indeks tidak valid, menampilkan pesan error.

> Metode lihat
Deskripsi: Metode ini digunakan untuk melihat informasi tentang keranjang pada indeks tertentu dalam daftar.
Fungsi:
Menampilkan nama dan kapasitas dari objek Keranjang pada indeks yang diberikan.
Jika indeks tidak valid, menampilkan pesan error.

> Metode lihat_semua
Deskripsi: Metode ini digunakan untuk menampilkan semua keranjang yang ada dalam daftar self.daftar_keranjang beserta kapasitasnya dalam format tabel.
Fungsi:
Menampilkan semua objek Keranjang yang ada di dalam daftar beserta nama dan kapasitasnya.

> Metode total_kapasitas
Deskripsi: Metode ini digunakan untuk menghitung total kapasitas dari semua keranjang yang ada dalam daftar.
Fungsi:
Menggunakan fungsi sum() untuk menghitung total kapasitas dari setiap objek Keranjang yang ada dalam daftar dan menampilkan hasilnya.