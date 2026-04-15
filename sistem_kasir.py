class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Keranjang:
    def __init__(self):
        self.isi = {} 

    def tambah_produk(self, produk, jumlah):
        if jumlah <= 0:
            print("Jumlah minimal 1")
            return
        if produk.stok < jumlah:
            print(f"Stok {produk.nama} kurang. Sisa: {produk.stok}")
            return

        if produk.nama in self.isi:
            self.isi[produk.nama][1] += jumlah
        else:
            self.isi[produk.nama] = [produk, jumlah]
        print(f"Berhasil menambah: {produk.nama} x{jumlah}")

    def hapus_produk(self, produk, jumlah):
        if produk.nama not in self.isi:
            print("Produk tidak ada di keranjang!")
            return 
        if jumlah > self.isi[produk.nama][1]:
            print("Jumlah melebihi isi keranjang!")
            return

        self.isi[produk.nama][1] -= jumlah
        if self.isi[produk.nama][1] == 0:
            del self.isi[produk.nama]
        print(f"{produk.nama} dihapus sebanyak {jumlah}")

    def _rincian_harga(self, member=False):
        subtotal = sum(p.harga * j for p, j in self.isi.values())
        diskon = 0
        if subtotal > 100000:
            diskon = subtotal * 0.15 if member else subtotal * 0.10
        setelah_diskon = subtotal - diskon
        ppn = setelah_diskon * 0.11
        total = setelah_diskon + ppn
        return subtotal, diskon, ppn, total

    def cetak_struk(self, member=False):
        if not self.isi:
            print("Keranjang kosong")
            return

        print("\n=== STRUK BELANJA ===")
        for produk, jumlah in self.isi.values():
            print(f"- {produk.nama} x{jumlah} : Rp{produk.harga * jumlah}")

        sub, diskon, ppn, total = self._rincian_harga(member)
        print(f"\nSubtotal : Rp{sub}")
        if diskon > 0:
            ket = "Diskon member 15%" if member else "Diskon 10%"
            print(f"{ket}: -Rp{diskon}")
        print(f"PPN 11% : Rp{ppn}")
        print(f"TOTAL : Rp{total}")
        print("====================")

    def bayar(self, uang, member=False):
        if not self.isi:
            print("Keranjang kosong")
            return

        *_, total = self._rincian_harga(member)
        print(f"Total bayar: Rp{total}")

        if uang < total:
            print("Uang tidak cukup!")
            return

        for produk, jumlah in self.isi.values():
            produk.stok -= jumlah

        print(f"Kembalian: Rp{uang - total}")
        self.isi.clear()