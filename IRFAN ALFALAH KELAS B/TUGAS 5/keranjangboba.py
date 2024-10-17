class Keranjang:
    def __init__(self, nama, kapasitas):
        self.nama = nama
        self.kapasitas = kapasitas

class DekDepe:
    def __init__(self):
        self.daftar_keranjang = []

    def beli(self, nama, kapasitas):
        """Menambahkan keranjang baru ke daftar."""
        self.daftar_keranjang.append(Keranjang(nama, kapasitas))
        print(f"Berhasil menambahkan {nama} dengan kapasitas {kapasitas}")

    def jual(self, indeks):
        """Menghapus keranjang dari daftar berdasarkan indeks."""
        if 0 <= indeks < len(self.daftar_keranjang):
            keranjang = self.daftar_keranjang.pop(indeks)
            print(f"Berhasil menjual {keranjang.nama} yang memiliki kapasitas sebesar {keranjang.kapasitas}")
        else:
            print("Indeks tidak valid")

    def ubah_kapasitas(self, indeks, kapasitas_baru):
        """Mengubah kapasitas keranjang berdasarkan indeks."""
        if 0 <= indeks < len(self.daftar_keranjang):
            self.daftar_keranjang[indeks].kapasitas = kapasitas_baru
            print(f"Berhasil mengubah kapasitas {self.daftar_keranjang[indeks].nama} menjadi {kapasitas_baru}")
        else:
            print("Indeks tidak valid")

    def ubah_nama(self, indeks, nama_baru):
        """Mengubah nama keranjang berdasarkan indeks."""
        if 0 <= indeks < len(self.daftar_keranjang):
            self.daftar_keranjang[indeks].nama = nama_baru
            print(f"Berhasil mengubah nama {self.daftar_keranjang[indeks].nama} menjadi {nama_baru}")
        else:
            print("Indeks tidak valid")

    def lihat(self, indeks):
        """Melihat informasi keranjang berdasarkan indeks."""
        if 0 <= indeks < len(self.daftar_keranjang):
            keranjang = self.daftar_keranjang[indeks]
            print(f"Keranjang {keranjang.nama} memiliki kapasitas sebesar {keranjang.kapasitas}")
        else:
            print("Indeks tidak valid")

    def lihat_semua(self):
        """Menampilkan semua keranjang dalam format tabel."""
        print("Keranjang Dek Depe")
        print("---------------------------")
        for keranjang in self.daftar_keranjang:
            print(f"{keranjang.nama:<20} | {keranjang.kapasitas:<10}")

    def total_kapasitas(self):
        """Menghitung total kapasitas dari semua keranjang."""
        total = sum(keranjang.kapasitas for keranjang in self.daftar_keranjang)
        print(f"Total kapasitas keranjang Dek Depe adalah {total}")

def main():
    dek_depe = DekDepe()
    n = int(input("Masukkan banyak operasi: "))
    
    for i in range(n):
        operasi = input(f"Operasi {i+1}: ").split()
        if operasi[0] == "BELI":
            dek_depe.beli(operasi[1], int(operasi[2]))
        elif operasi[0] == "JUAL":
            dek_depe.jual(int(operasi[1]))
        elif operasi[0] == "UBAH_KAPASITAS":
            dek_depe.ubah_kapasitas(int(operasi[1]), int(operasi[2]))
        elif operasi[0] == "UBAH_NAMA":
            dek_depe.ubah_nama(int(operasi[1]), operasi[2])
        elif operasi[0] == "LIHAT":
            dek_depe.lihat(int(operasi[1]))
        elif operasi[0] == "LIHAT_SEMUA":
            dek_depe.lihat_semua()
        elif operasi[0] == "TOTAL_KAPASITAS":
            dek_depe.total_kapasitas()

if __name__ == "__main__":
    main()