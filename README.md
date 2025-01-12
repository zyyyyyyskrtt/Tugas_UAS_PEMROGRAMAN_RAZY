## Tugas_UAS_PEMROGRAMAN_RAZY
Program Pengelolaan tiket bus <p>
Nama: Razy Al Farisi <p>
Nim: 312410524 <p>
Kelas: TI.24.A5 <p>
Jurusan: Teknik Informatika <p> 
Mata Kuliah: Bahasa Pemrograman <p> 

## Penjelasan Program 
1. Kelas TiketData

         class TicketData:
   - Di sini, kita mendefinisikan sebuah kelas bernama TicketData. Kelas ini akan berfungsi sebagai wadah untuk menyimpan informasi tentang tiket.

         def __init__(self):
             self.tickets = []
   - Metode ini adalah konstruktor yang dipanggil saat kita membuat instance baru dari kelas TicketData. Di dalam metode ini, kita menginisialisasi atribut tickets sebagai        list kosong. Atribut ini akan digunakan untuk menyimpan tiket yang ditambahkan ke dalam objek TicketData.

          def add_ticket(self, ticket):
              self.tickets.append(ticket)
   - Metode ini menerima satu parameter, yaitu ticket, dan menambahkannya ke dalam list tickets. Dengan kata lain, metode ini digunakan untuk menambahkan tiket baru ke dalam      objek TicketData.

           def get_tickets(self):
               return self.tickets
   - Metode ini mengembalikan list tickets yang berisi semua tiket yang telah ditambahkan. Ini memungkinkan pengguna untuk mengakses semua tiket yang disimpan dalam objek         TicketData.

2. main
   Import Kelas
   
            from data import TicketData
            from process import TicketProcess
            from view import TicketView
   - TicketData: Kelas untuk mengelola data tiket.
   - TicketProcess: Kelas untuk mengelola logika bisnis terkait tiket.
   - TicketView: Kelas untuk menangani interaksi dengan pengguna.
  
   Inisialisasi Objek

            data = TicketData()
            view = TicketView()
            process = TicketProcess(data, view)
   - Membuat instance dari TicketData, TicketView, dan TicketProcess.
   - data akan digunakan untuk menyimpan dan mengelola tiket.
   - view akan digunakan untuk menangani input dan output.
   - process akan mengelola interaksi antara data dan tampilan.

   Loop Utama
   
            while True:
                print("\n1. Tambah Tiket")
                print("2. Tampilkan Tiket")
                print("3. Keluar")
   - Program memasuki loop tak terbatas yang akan terus berjalan sampai pengguna memilih untuk keluar.
   - Menampilkan menu pilihan kepada pengguna.

   Meminta Pilihan Pengguna

            choice = input("Pilih opsi: ")
   - Menggunakan input() untuk meminta pengguna memilih opsi dari menu.

   Menangani Pilihan Pengguna

            if choice == "1":
                process.add_ticket()
            elif choice == "2":
                process.show_tickets()
            elif choice == "3":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
   - Jika pengguna memilih "1", metode add_ticket() dari process dipanggil untuk menambahkan tiket baru.
   - Jika pengguna memilih "2", metode show_tickets() dari process dipanggil untuk menampilkan semua tiket yang ada.
   - Jika pengguna memilih "3", loop akan dihentikan dengan break, dan program akan keluar.
   - Jika pilihan tidak valid, program akan mencetak pesan kesalahan dan meminta pengguna untuk mencoba lagi.

   Menjalankan Fungsi main()

            if __name__ == "__main__":
                main()
   - Kode ini memastikan bahwa fungsi main() hanya akan dijalankan jika file ini dieksekusi sebagai program utama, bukan jika diimpor sebagai modul di file lain.

   

