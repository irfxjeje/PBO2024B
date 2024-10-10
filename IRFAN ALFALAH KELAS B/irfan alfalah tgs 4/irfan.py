class CharacterCounter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.char_counts = []
        self.lines = []

    def read_file(self):
        """Membaca isi file dan menyimpan jumlah karakter per baris."""
        try:
            with open(self.file_name, "r") as in_file:
                self.lines = in_file.readlines()
            if not self.lines:
                self.write_null()
                return False
            self.char_counts = [len(line.rstrip('\n')) for line in self.lines]
            return True
        except FileNotFoundError:
            print("File tidak ditemukan :(")
            return False

    def write_null(self):
        """Menulis 'NULL' ke dalam file jika file kosong."""
        with open(self.file_name, "w") as out_file:
            out_file.write("NULL")
        print("Output berhasil ditulis pada", self.file_name)

    def calculate_stats(self):
        """Menghitung statistik karakter: min, max, dan range."""
        min_chars = min(self.char_counts)
        max_chars = max(self.char_counts)
        range_chars = max_chars - min_chars
        return min_chars, max_chars, range_chars

    def write_output(self):
        """Menulis output statistik ke dalam file."""
        min_chars, max_chars, range_chars = self.calculate_stats()
        with open(self.file_name, "w") as out_file:
            out_file.write("".join(self.lines))  # Menambahkan isi file sebelumnya
            out_file.write("\n... Isi dari berkas " + self.file_name + " sebelumnya ...\n")
            out_file.write("###########\n")
            out_file.write(f"Min: {min_chars} karakter\n")
            out_file.write(f"Max: {max_chars} karakter\n")
            out_file.write(f"Range: {range_chars} karakter\n")
        print("Output berhasil ditulis pada", self.file_name)

def main():
    # Meminta nama file input dari user
    file_name = input("Masukkan nama file input: ")
    counter = CharacterCounter(file_name)

    if counter.read_file():
        counter.write_output()
    print("Program selesai. Tekan enter untuk keluar...")
    input()

if __name__ == "__main__":
    main()