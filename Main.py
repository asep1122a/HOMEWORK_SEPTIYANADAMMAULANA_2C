import Modul as db

while True :
   print('='*5,' Toko Elektronik ','='*5)
   print('Masukan Pilihan: ')
   print('1. Tambah Data Barang ')
   print('2. Edit Data ')
   print('3. Hapus Data Barang ')
   print('4. Cari Data ')
   print('5  Tampilkan Data Barang ')
   print('6  Tampilkan Jumlah Data ')
   print('7  keluar')
   pilihan = int(input('masukan plihan :')) 
   if pilihan == 1:
      db.insert()
   elif pilihan == 2:
      db.edit_data()
   elif pilihan == 3:
      db.hapus_data()
   elif pilihan == 4:
      db.cari_data()
   elif pilihan == 5:
      db.view_data()
   elif pilihan == 6:
      db.jumlah_data()
   elif pilihan == 7:
     print('terima kasih telah datang')
     break