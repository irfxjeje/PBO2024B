Konstruktor dalam Object-Oriented Programming (OOP) adalah metode khusus yang digunakan untuk menginisialisasi objek dari sebuah kelas. Konstruktor dipanggil secara otomatis ketika sebuah objek baru dari kelas dibuat. Fungsi utama dari konstruktor adalah untuk menginisialisasi atribut-atribut objek tersebut sehingga objek siap digunakan.

Ciri-Ciri Konstruktor:
1. Nama Metode: Konstruktor biasanya memiliki nama khusus sesuai bahasa pemrograman yang digunakan.
> Di Python, konstruktor disebut __init__.
> Di Java, konstruktor menggunakan nama yang sama dengan nama kelas.
> Di C++ juga menggunakan nama yang sama dengan nama kelas.
2. Otomatis Dipanggil: Konstruktor dipanggil otomatis ketika objek dibuat dengan menggunakan operator new (di beberapa bahasa) atau saat instansiasi objek.
3. Tidak Mengembalikan Nilai: Konstruktor tidak mengembalikan nilai apapun, bahkan None di Python.
4. Menginisialisasi Atribut: Konstruktor digunakan untuk menginisialisasi atribut atau variabel anggota objek, memberikan nilai awal untuk atribut tersebut.

Contoh Konstruktor dalam Berbagai Bahasa:
1. Python:
Di Python, konstruktor adalah metode __init__. Ini dipanggil ketika objek dibuat dari kelas.

class Mobil:
    def __init__(self, merk, model):
        # Atribut objek
        self.merk = merk
        self.model = model
        print(f"Mobil {self.merk} {self.model} telah dibuat.")

# Membuat objek mobil baru
mobil1 = Mobil("Toyota", "Avanza")  # Konstruktor dipanggil

Penjelasan:
> __init__(self, merk, model) adalah konstruktor. Ini menginisialisasi objek dengan dua atribut: merk dan model.
> mobil1 = Mobil("Toyota", "Avanza") membuat objek baru dan secara otomatis memanggil konstruktor untuk memberikan nilai pada atribut merk dan model.

2. Java:
Di Java, konstruktor menggunakan nama yang sama dengan nama kelas dan tidak memiliki tipe pengembalian.

class Mobil {
    String merk;
    String model;

    // Konstruktor
    public Mobil(String merk, String model) {
        this.merk = merk;
        this.model = model;
        System.out.println("Mobil " + this.merk + " " + this.model + " telah dibuat.");
    }

    public static void main(String[] args) {
        // Membuat objek mobil baru
        Mobil mobil1 = new Mobil("Toyota", "Avanza");
    }
}

Penjelasan:
> public Mobil(String merk, String model) adalah konstruktor yang menginisialisasi objek Mobil dengan dua atribut: merk dan model.
> Mobil mobil1 = new Mobil("Toyota", "Avanza"); membuat objek baru dan memanggil konstruktor.

3. C++:
Di C++, konstruktor juga menggunakan nama yang sama dengan nama kelas dan tidak mengembalikan nilai.

#include <iostream>
using namespace std;

class Mobil {
    public:
        string merk;
        string model;

        // Konstruktor
        Mobil(string merk, string model) {
            this->merk = merk;
            this->model = model;
            cout << "Mobil " << this->merk << " " << this->model << " telah dibuat." << endl;
        }
};

int main() {
    // Membuat objek mobil baru
    Mobil mobil1("Toyota", "Avanza");
    return 0;
}

Penjelasan:
> Mobil(string merk, string model) adalah konstruktor yang menerima dua parameter untuk menginisialisasi objek dengan nilai atribut merk dan model.
> Mobil mobil1("Toyota", "Avanza"); membuat objek baru dan memanggil konstruktor.

Fungsi dari Konstruktor:
1. Inisialisasi Atribut: Konstruktor menginisialisasi nilai awal dari atribut atau properti objek.
2. Menentukan Status Awal: Konstruktor dapat digunakan untuk menyiapkan status awal objek sebelum objek digunakan, seperti mengalokasikan memori atau membuka file.
3. Memastikan Objek Valid: Konstruktor memastikan objek yang dibuat berada dalam kondisi yang valid sebelum digunakan.


KAITAN DENGAN TUGAS 3 :

Konstruktor dalam kelas Konoha adalah metode __init__. Konstruktor ini bertanggung jawab untuk menginisialisasi atribut-atribut yang diperlukan oleh objek yang dibuat dari kelas tersebut.

Fungsi Konstruktor dalam Kode

class Konoha:
    def __init__(self, encoded_str):
        self.encoded_str = encoded_str
        self.sum_digits = 0
        self.letters = []

1. Parameter encoded_str:
> Konstruktor menerima parameter encoded_str, yaitu string yang berisi kombinasi huruf dan angka yang akan diproses.
> Nilai ini diberikan saat objek dibuat (contohnya, decoder = Konoha(input_str)).
2. Inisialisasi Atribut:
> self.encoded_str: Menyimpan string yang akan diproses, sehingga metode lain di kelas dapat mengaksesnya.
> self.sum_digits: Diinisialisasi dengan nilai 0, digunakan untuk menyimpan jumlah digit yang ditemukan dalam string.
> self.letters: Diinisialisasi sebagai daftar kosong, digunakan untuk mengumpulkan huruf dari string.


KAITAN DENGAN TUGAS 4 :

Pada kelas IOException, konstruktor (__init__) memainkan peran yang sangat penting untuk menginisialisasi atribut dan langsung menjalankan logika pemrosesan file. 

