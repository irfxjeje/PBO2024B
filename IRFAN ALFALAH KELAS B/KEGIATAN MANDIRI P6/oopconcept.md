Konsep OOP (Object-Oriented Programming) adalah pendekatan pemrograman yang menggunakan object dan class sebagai dasar pengorganisasian kode. OOP digunakan untuk membuat program yang modular, lebih mudah dipahami, dan lebih mudah dikelola.

Berikut adalah konsep dasar OOP:

1. Class: Blueprint atau template untuk membuat objek. Class mendefinisikan atribut (data) dan metode (fungsi) yang dimiliki oleh objek.
2. Object: Instansiasi dari sebuah class. Objek adalah entitas nyata yang diciptakan berdasarkan class.
3. Encapsulation: Membungkus data dan metode dalam sebuah objek, dengan akses terbatas melalui getter dan setter.
4. Inheritance: Kemampuan suatu class untuk mewarisi properti dan metode dari class lain.
5. Polymorphism: Kemampuan untuk menggunakan satu antarmuka untuk berbagai tipe data.
6. Abstraction: Menyembunyikan detail implementasi dan hanya menunjukkan fitur penting kepada pengguna.


Perbedaan Object-Oriented Programming (OOP) dengan paradigma pemrograman lainnya, seperti procedural programming atau functional programming, terletak pada cara pendekatan desain program, pengelolaan data, dan struktur kode. Berikut adalah penjelasan rinci:

1. Pendekatan Desain
OOP: Berbasis objek. Program dibangun dengan mendefinisikan class (template) dan membuat object (instansiasi dari class). Fokusnya adalah pada data dan perilaku yang dimiliki objek.
Contoh: Class Keranjang merepresentasikan objek dengan atribut nama dan kapasitas.
Procedural Programming: Berbasis prosedur atau fungsi. Program dibangun sebagai serangkaian instruksi yang dieksekusi langkah demi langkah.
Contoh: Fungsi meong_bross() adalah kumpulan logika tanpa struktur berbasis objek.
2. Struktur dan Organisasi
OOP:
Program dibagi menjadi class dan object.
Data dan perilaku disatukan dalam class, sehingga mudah dikelola.
Encapsulation memungkinkan pembatasan akses ke atribut dan metode tertentu.
Kode lebih modular dan reusable.
Procedural Programming:
Program dibagi menjadi fungsi. Data dikelola secara global atau sebagai parameter fungsi.
Tidak ada encapsulation—semua data biasanya tersedia untuk semua fungsi.
Sulit untuk memodifikasi program besar tanpa memengaruhi fungsi lain.
3. Fokus Utama
OOP:
Fokus pada objek, yaitu representasi dunia nyata.
Memanfaatkan hubungan antarobjek untuk menyelesaikan masalah.
Contoh: Dalam sistem penjualan keranjang, setiap keranjang menjadi objek dengan atribut tertentu, seperti nama dan kapasitas.
Procedural Programming:
Fokus pada langkah-langkah algoritma.
Data diproses secara langsung melalui fungsi atau prosedur.


Prinsip-prinsip Object-Oriented Programming (OOP) terdiri dari empat konsep dasar yang membantu dalam merancang perangkat lunak yang lebih modular, fleksibel, dan mudah dikelola. Keempat prinsip utama ini adalah Encapsulation, Inheritance, Polymorphism, dan Abstraction. Berikut penjelasan masing-masing prinsip OOP:

1. Encapsulation (Enkapsulasi)
Definisi: Encapsulation adalah konsep membungkus data (atribut) dan metode (fungsi) dalam satu unit yang disebut class. Hal ini juga melibatkan pengendalian akses terhadap data tersebut dengan cara menyembunyikan detail implementasi dan hanya memberikan akses melalui metode tertentu.
Tujuan:
Melindungi data dari akses langsung.
Mengontrol bagaimana data diakses dan dimodifikasi.
Ciri Khas:
Menyembunyikan detail implementasi dari pengguna class.
Menggunakan getter dan setter untuk mengakses atau memodifikasi data.
2. Inheritance (Pewarisan)
Definisi: Inheritance adalah konsep di mana sebuah class dapat mewarisi atribut dan metode dari class lain. Class yang mewarisi disebut child class atau derived class, sementara class yang diwarisi disebut parent class atau base class.
Tujuan:
Menghindari duplikasi kode (reuse).
Membuat hierarki class yang lebih alami dan terstruktur.
Child class dapat menambahkan atau memodifikasi fungsionalitas yang ada.
3. Polymorphism (Polimorfisme)
Definisi: Polymorphism adalah konsep yang memungkinkan objek-objek dari class yang berbeda dapat diperlakukan sebagai objek dari type yang sama, tetapi dengan perilaku yang berbeda. Ini sering terjadi ketika metode yang sama digunakan di banyak class yang berbeda.
Tujuan:
Memungkinkan objek dengan tipe yang berbeda merespons dengan cara yang sesuai ketika metode yang sama dipanggil.
Menyederhanakan kode karena tidak perlu membuat metode dengan nama yang berbeda untuk setiap tipe objek.
4. Abstraction (Abstraksi)
Definisi: Abstraksi adalah konsep untuk menyembunyikan detail implementasi dan hanya menampilkan fungsionalitas yang penting bagi pengguna objek. Class abstrak atau metode abstrak digunakan untuk menentukan antarmuka yang harus diikuti oleh class turunannya.
Tujuan:
Menyederhanakan interaksi dengan objek.
Fokus pada apa yang dilakukan objek, bukan bagaimana objek itu melakukannya.


Kaitan dengan tugas 3 :

1. Class (Blueprint)
Class Konoha adalah blueprint yang mendefinisikan atribut (encoded_str, sum_digits, dan letters) serta metode (calculate_sum_of_digits, collect_letters, dan decrypt) untuk menangani proses dekripsi.
Class ini digunakan untuk memproses string terenkripsi dengan logika tertentu.
2. Object (Instance)
Instansiasi objek dilakukan melalui:
decoder = Konoha(input_str)
Objek decoder adalah representasi spesifik dari class Konoha, di mana properti dan metode class dapat diakses dan dimanipulasi sesuai kebutuhan.
3. Encapsulation
Data (encoded_str, sum_digits, dan letters) dibungkus di dalam objek dan diakses atau dimodifikasi hanya melalui metode class, seperti calculate_sum_of_digits, collect_letters, dan decrypt.
Encapsulation memastikan bahwa logika pengolahan data terlindungi dari akses langsung yang tidak diinginkan.
4. Abstraction
Metode seperti calculate_sum_of_digits, collect_letters, dan decrypt menyembunyikan detail implementasi dari pengguna.
Misalnya, pengguna hanya memanggil decrypt untuk mendekripsi string, tanpa perlu mengetahui bagaimana angka dihitung atau huruf digeser.


Kaitan dengan tugas 4 :

1. Encapsulation
Atribut seperti lines, char_counts, min_chars, max_chars, dan char_range adalah bagian dari class dan tidak diakses langsung dari luar.
Semua manipulasi data dilakukan melalui metode seperti read_file, calculate_stats, write_output, dan write_null. Hal ini melindungi data internal dan memastikan bahwa hanya metode class yang dapat mengubah atau mengaksesnya.
2. Abstraction
Detail implementasi seperti membaca file (read_file), menghitung statistik (calculate_stats), dan menulis ke file (write_output) disembunyikan dari pengguna.
Dari perspektif pengguna, mereka hanya perlu memberikan nama file, dan semua proses dilakukan di balik layar tanpa mereka perlu mengetahui detailnya.


Kaitan dengan tugas 5 :

1. Encapsulation
Atribut nama dan kapasitas pada class Keranjang dienkapsulasi, hanya dapat diakses melalui objek.
Data keranjang dikelola melalui metode-metode dalam class DekDepe (beli, jual, ubah_kapasitas, ubah_nama, dll.), sehingga akses terhadap daftar keranjang diatur dengan baik.
2. Abstraction
Pengguna cukup memanggil metode seperti beli atau lihat tanpa perlu memahami detail implementasi bagaimana data keranjang dikelola atau disimpan.
Operasi terhadap keranjang dilakukan melalui perintah yang jelas seperti "BELI", "LIHAT", dll.
