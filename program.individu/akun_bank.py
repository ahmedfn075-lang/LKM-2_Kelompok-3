Ba = 2500

class AkunBank:
   def __init__(self, nomor, pemilik, saldo_awal):
      self.nomor = nomor 
      self.saldo = saldo_awal
      self.pemilik = pemilik
      self.riwayat = []
      
   def cek_saldo1(self):
    print(f"Saldo {self.pemilik}: Rp{self.saldo - Ba}")

   def tarik_tunai(self, jumlah):
    if jumlah <= 0:
      print(f"jumlah tidak boleh kosong")
      return
    if jumlah <= self.saldo:
      self.saldo -= jumlah
      
      print(f"{self.pemilik} menarik Rp{jumlah}")
      self.riwayat.append(f"riwayat transaksi, tarik tunai Rp {jumlah}")
    else:
      print("Saldo tidak cukup!")

   def transfer(self, tujuan, jumlah, ):
    if self.saldo >= jumlah:
      self.saldo -= jumlah
      tujuan.saldo += jumlah
      print(f"Transfer Rp{jumlah - Ba} ke {tujuan.pemilik} Berhasil!")
      self.riwayat.append(f"riwayat transaksi, transfer Rp {jumlah}")
    else:
      print("Transfer Gagal: Saldo tidak cukup.")
     
    
   def cek_saldo2(self):
     print(f"saldo {self.pemilik}: Rp{self.saldo}")
   
   def cetak_riwayat(self):
    data = self.riwayat
    print(f"\n Riwayat transaksi {self.pemilik}")
    for r in data:
      print("-" + r)
    