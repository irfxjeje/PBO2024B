Class dan Object dalam OOP (Object-Oriented Programming)
Class dan Object adalah dua konsep fundamental dalam Object-Oriented Programming (OOP). Keduanya memiliki hubungan yang sangat erat, di mana class berfungsi sebagai template atau blueprint untuk membuat objek. Berikut penjelasan lebih mendalam mengenai class dan object:

1. Class
Definisi: Class adalah template atau kerangka kerja untuk mendefinisikan objek dalam pemrograman OOP. Class menyatakan apa yang akan dimiliki oleh objek dan apa yang bisa dilakukan oleh objek tersebut. Sebuah class dapat memiliki atribut (data/variabel) dan metode (fungsi/operasi).
Fungsi:
Menyediakan struktur untuk objek.
Menyatakan jenis data dan perilaku yang dimiliki oleh objek.
Contoh Class

class Car:
    # Atribut atau property
    def __init__(self, make, model, year):
        self.make = make  # Merek mobil
        self.model = model  # Model mobil
        self.year = year  # Tahun pembuatan

    # Metode atau perilaku
    def start_engine(self):
        print(f"Mesin mobil {self.make} {self.model} tahun {self.year} dinyalakan!")

Pada contoh di atas, Car adalah sebuah class yang mendefinisikan dua hal utama:

Atribut: make, model, dan year yang menyimpan informasi tentang mobil.
Metode: start_engine() yang mendefinisikan perilaku mobil untuk menyalakan mesinnya.

2. Object
Definisi: Object adalah instansiasi atau contoh konkret dari sebuah class. Objek adalah representasi nyata dari class, yang memiliki nilai-nilai tertentu untuk atribut dan dapat melakukan tindakan berdasarkan metode yang ada di class.
Fungsi:
Objek adalah entitas nyata yang berinteraksi dengan objek lain di dalam program.
Objek memiliki status (nilai-nilai atribut) dan perilaku (metode) yang ditentukan oleh class.
Contoh Object

# Membuat objek dari class Car
my_car = Car("Toyota", "Corolla", 2022)

# Mengakses atribut objek
print(my_car.make)  # Output: Toyota
print(my_car.year)  # Output: 2022

# Memanggil metode objek
my_car.start_engine()  # Output: Mesin mobil Toyota Corolla tahun 2022 dinyalakan!

Pada contoh di atas:
my_car adalah object yang merupakan instansiasi dari class Car.
my_car memiliki atribut yang diatur melalui konstruktor __init__() dan dapat menjalankan metode start_engine().


KAITAN DENGAN TUGAS 5 :

Class:
1. Keranjang adalah sebuah class yang mendefinisikan struktur dan perilaku dari objek keranjang. Class ini memiliki dua atribut:

- nama: Nama keranjang.
- kapasitas: Kapasitas keranjang.

Metode dalam class ini adalah konstruktor __init__ yang digunakan untuk menginisialisasi objek keranjang dengan nama dan kapasitas.

class Keranjang:
    def __init__(self, nama, kapasitas):
        self.nama = nama  # Atribut untuk nama keranjang
        self.kapasitas = kapasitas  # Atribut untuk kapasitas keranjang

2. DekDepe adalah class yang mengelola daftar objek-objek Keranjang. Class ini memiliki beberapa metode untuk menambah, mengubah, dan menghapus objek Keranjang dalam daftar daftar_keranjang.

class DekDepe:
    def __init__(self):
        self.daftar_keranjang = []  # Atribut untuk menyimpan objek-objek Keranjang


Object:
1. dek_depe adalah objek dari class DekDepe. Objek ini berfungsi untuk mengelola daftar keranjang. dek_depe akan memanggil metode-metode seperti beli(), jual(), ubah_kapasitas(), dan lainnya untuk mengelola objek Keranjang.

2. Keranjang: Ketika metode beli() dipanggil, objek Keranjang baru dibuat dan ditambahkan ke dalam daftar daftar_keranjang dalam objek dek_depe.

Misalnya, ketika dek_depe.beli("Keranjang A", 15) dipanggil, objek Keranjang baru dengan nama "Keranjang A" dan kapasitas 15 akan dibuat, dan ditambahkan ke dalam daftar daftar_keranjang.

Penjelasan:
- Class: Keranjang dan DekDepe adalah class. Class adalah cetak biru yang mendefinisikan atribut dan metode yang akan dimiliki oleh objek.
- Object: Ketika kita membuat dek_depe dari class DekDepe, atau ketika kita memanggil beli() yang membuat objek Keranjang, maka dek_depe dan setiap objek Keranjang yang ditambahkan ke dalamnya adalah object yang dihasilkan dari class tersebut. Object adalah instance nyata dari class yang memiliki data dan perilaku sesuai dengan definisi class.





