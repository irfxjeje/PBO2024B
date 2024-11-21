Acces Modifikation Python digunakan untuk membatasi akses ke anggota kelas (yaitu, variabel dan metode) dari luar kelas. Tujuan utama access modifier adalah untuk melindungi data dan memastikan kontrol penuh atas bagaimana atribut atau metode diakses atau dimodifikasi.

Tipe Access Modifier
1. Public (public):
> Dapat diakses dari mana saja, baik dalam kelas, luar kelas, maupun subclass.
> Secara default, semua atribut dan metode di Python adalah public.
Contoh:

class Contoh:
    def __init__(self):
        self.nama = "Public Attribute"  # Public
    
    def tampilkan_nama(self):
        print(self.nama)  # Public method

2. Protected (protected):
> Hanya dapat diakses dalam kelas itu sendiri dan subclass (kelas turunan).
> Di Python, ini diimplementasikan dengan menambahkan satu underscore (_) sebelum nama atribut atau metode.
Contoh:

class Contoh:
    def __init__(self):
        self._data = "Protected Attribute"
    
    def _protected_method(self):
        print("This is a protected method")

3. Private (private):
> Hanya dapat diakses dalam kelas itu sendiri.
> Di Python, ini diimplementasikan dengan menambahkan dua underscore (__) sebelum nama atribut atau metode.
Contoh:

class Contoh:
    def __init__(self):
        self.__data = "Private Attribute"
    
    def __private_method(self):
        print("This is a private method")


KAITAN DENGAN TUGAS 3 : 

1. self.encoded_str (Public)
> Deskripsi: Atribut ini menyimpan string terenkripsi yang diberikan sebagai input ke konstruktor.
> Access Modifier: Atribut ini bersifat public, sehingga dapat diakses langsung dari luar kelas.
> Saran Peningkatan: Jika atribut ini hanya digunakan dalam internal proses kelas, maka sebaiknya dijadikan protected atau private untuk mencegah manipulasi langsung.

self._encoded_str = encoded_str  # Protected

2. self.sum_digits (Public)
>Deskripsi: Atribut ini menyimpan total dari semua digit numerik yang terdapat dalam encoded_str.
>Access Modifier: Bersifat public, sehingga bisa dimodifikasi dari luar kelas, meskipun ini seharusnya dikelola hanya oleh metode kelas.
>Potensi Risiko: Pengguna dapat mengubah nilai atribut ini secara langsung, yang dapat menyebabkan hasil dekripsi menjadi tidak akurat.
>Saran Peningkatan: Ganti menjadi private:

self.__sum_digits = 0  # Private

Untuk mendapatkan nilainya, tambahkan getter:

def get_sum_digits(self):
    return self.__sum_digits

3. self.letters (Public)
> Deskripsi: Atribut ini menyimpan daftar huruf yang diekstraksi dari encoded_str.
> Access Modifier: Bersifat public, sehingga dapat dimodifikasi secara langsung.
> Saran Peningkatan: Gunakan private untuk melindunginya:

self.__letters = []


Perubahan yang Direkomendasikan

class Konoha:
    def __init__(self, encoded_str):
        self._encoded_str = encoded_str  # Protected
        self.__sum_digits = 0  # Private
        self.__letters = []  # Private

    def _calculate_sum_of_digits(self):
        """Menghitung jumlah digit dalam encoded_str."""
        for char in self._encoded_str:
            if char.isdigit():
                self.__sum_digits += int(char)

    def _collect_letters(self):
        """Mengumpulkan huruf dari encoded_str."""
        for char in self._encoded_str:
            if char.isalpha():
                self.__letters.append(char)

    def decrypt(self):
        """Metode utama untuk mendekripsi encoded_str."""
        self._calculate_sum_of_digits()

        if self.__sum_digits == 0:
            print("Tidak memiliki angka")
            return ""  

        self._collect_letters()

        shift = self.__sum_digits % 26  # Menghindari pergeseran lebih dari 26
        decrypted_letters = []

        for letter in self.__letters:
            if letter.islower():
                new_char = chr((ord(letter) - ord('a') - shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(letter) - ord('A') - shift) % 26 + ord('A'))
            decrypted_letters.append(new_char)

        return ''.join(decrypted_letters)



KAITAN DENGAN TUGAS 4 :   

1. self.filename (Public)
> Deskripsi: Menyimpan nama file yang akan diproses.
> Access Modifier: Bersifat public, sehingga bisa diakses langsung dari luar kelas.
> Saran Peningkatan: Jadikan atribut ini protected agar hanya digunakan di dalam kelas atau turunannya:

self._filename = filename  # Protected

2. self.lines (Public)
> Deskripsi: Menyimpan daftar baris teks yang dibaca dari file.
> Access Modifier: Bersifat public, sehingga bisa dimanipulasi langsung dari luar kelas.
> Saran Peningkatan: Jadikan private dan tambahkan getter jika perlu akses dari luar:

self.__lines = []

def get_lines(self):
    return self.__lines

3. self.char_counts (Public)
> Deskripsi: Menyimpan jumlah karakter pada setiap baris file.
> Access Modifier: Sama seperti self.lines, atribut ini hanya digunakan dalam proses internal.
> Saran Peningkatan: Jadikan private:

self.__char_counts = []
self.min_chars, self.max_chars, self.

4. char_range (Public)
> Deskripsi: Menyimpan statistik karakter (minimum, maksimum, rentang) dari file.
> Access Modifier: Bersifat public, tetapi seharusnya hanya dimanipulasi oleh metode internal.
> Saran Peningkatan: Jadikan private:

self.__min_chars = None
self.__max_chars = None
self.__char_range = None

5. read_file (Public)
> Deskripsi: Membaca isi file dan menghitung jumlah karakter per baris.
> Access Modifier: Bersifat public, tetapi hanya digunakan secara internal dalam kelas.
> Saran Peningkatan: Jadikan protected untuk menunjukkan bahwa metode ini tidak untuk diakses dari luar:

def _read_file(self):
    ...
6. calculate_stats (Public)
> Deskripsi: Menghitung statistik karakter pada file.
> Access Modifier: Sama seperti read_file, seharusnya protected:

def _calculate_stats(self):
    ...

7. write_output (Public)
> Deskripsi: Menulis hasil perhitungan statistik ke dalam file.
> Access Modifier: Bersifat public, tetapi jika hanya digunakan secara internal, sebaiknya dijadikan protected:

def _write_output(self):
    ...
8. write_null (Public)
> Deskripsi: Menulis "NULL" ke dalam file jika file kosong.
> Access Modifier: Sama seperti write_output, sebaiknya protected:

def _write_null(self):
    ...


Perubahan yang Direkomendasikan

class IOException:
    def __init__(self, filename):
        self._filename = filename  # Protected
        self.__lines = []  # Private
        self.__char_counts = []  # Private
        self.__min_chars = None  # Private
        self.__max_chars = None  # Private
        self.__char_range = None  # Private

        try:
            self._read_file()
            if not self.__lines:
                self._write_null()
            else:
                self._calculate_stats()
                self._write_output()
        except FileNotFoundError:
            print("File tidak ditemukan :(")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
        else:
            print(f"Output berhasil ditulis pada {self._filename}")
        finally:
            input("Program selesai. Tekan enter untuk keluar...")

    def _read_file(self):
        with open(self._filename, "r") as in_file:
            self.__lines = in_file.readlines()
            self.__char_counts = [len(line.rstrip('\n')) for line in self.__lines]

    def _calculate_stats(self):
        self.__min_chars = min(self.__char_counts)
        self.__max_chars = max(self.__char_counts)
        self.__char_range = self.__max_chars - self.__min_chars

    def _write_output(self):
        with open(self._filename, "a") as out_file:
            out_file.write("###########\n")
            out_file.write(f"Min: {self.__min_chars} karakter\n")
            out_file.write(f"Max: {self.__max_chars} karakter\n")
            out_file.write(f"Range: {self.__char_range} karakter\n")

    def _write_null(self):
        with open(self._filename, "w") as out_file:
            out_file.write("NULL\n")
        print("File tidak berisi teks. Ditulis 'NULL' ke dalam file.")


KAITAN DENGAN TUGAS 5 :        

1. Access Modifier dalam Keranjang
> Atribut Publik:
  - self.nama dan self.kapasitas saat ini bersifat publik, artinya dapat diakses dan diubah langsung dari luar kelas.

keranjang = Keranjang("Buah", 50)
print(keranjang.nama)  # Akses langsung
keranjang.nama = "Sayur"  # Modifikasi langsung

> Rekomendasi:
  - Jadikan atribut ini privat atau protected menggunakan tanda _ atau __ untuk mencegah akses langsung. Akses dan modifikasi dilakukan melalui getter dan setter.

class Keranjang:
    def __init__(self, nama, kapasitas):
        self.__nama = nama
        self.__kapasitas = kapasitas

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    def get_kapasitas(self):
        return self.__kapasitas

    def set_kapasitas(self, kapasitas_baru):
        self.__kapasitas = kapasitas_baru

2. Access Modifier dalam DekDepe
> Atribut Internal:
  - self.daftar_keranjang saat ini bersifat publik, sehingga data internal dapat diakses dan dimodifikasi secara langsung, yang melanggar prinsip encapsulation.

dek_depe = DekDepe()
dek_depe.daftar_keranjang.append(Keranjang("Buah", 50))  # Tidak aman

> Rekomendasi: Ubah menjadi protected dengan _daftar_keranjang.

class DekDepe:
    def __init__(self):
        self._daftar_keranjang = []


Implementasi Final (Dengan Access Modifier)

class Keranjang:
    def __init__(self, nama, kapasitas):
        self.__nama = nama
        self.__kapasitas = kapasitas

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    def get_kapasitas(self):
        return self.__kapasitas

    def set_kapasitas(self, kapasitas_baru):
        self.__kapasitas = kapasitas_baru


class DekDepe:
    def __init__(self):
        self._daftar_keranjang = []

    def beli(self, nama, kapasitas):
        """Menambahkan keranjang baru ke daftar."""
        self._daftar_keranjang.append(Keranjang(nama, kapasitas))
        print(f"Berhasil menambahkan {nama} dengan kapasitas {kapasitas}")

    def jual(self, indeks):
        """Menghapus keranjang dari daftar berdasarkan indeks."""
        if 0 <= indeks < len(self._daftar_keranjang):
            keranjang = self._daftar_keranjang.pop(indeks)
            print(f"Berhasil menjual {keranjang.get_nama()} yang memiliki kapasitas sebesar {keranjang.get_kapasitas()}")
        else:
            print("Indeks tidak valid")