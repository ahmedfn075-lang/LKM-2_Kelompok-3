from sistem_kasir import Produk, Keranjang

p1 = Produk("Kopi Kenangan", 25000,20)
p2 = Produk("Susu UHT", 18000,20)
p3 = Produk("Keyboard Gaming", 250000,20)


# del p3

keranjang_saya = Keranjang()
keranjang_saya.tambah_produk(p1,5)
keranjang_saya.tambah_produk(p2,34)
keranjang_saya.tambah_produk(p3,2)

keranjang_saya.hapus_produk(p2, 1)
keranjang_saya.cetak_struk(member = True)
keranjang_saya.bayar(500000, member = True)