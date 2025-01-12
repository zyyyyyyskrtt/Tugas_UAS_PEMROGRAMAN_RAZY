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
   a. Import Kelas

            from data import TicketData
            from process import TicketProcess
            from view import TicketView
   - TicketData: Kelas untuk mengelola data tiket.
   - TicketProcess: Kelas untuk mengelola logika bisnis terkait tiket.
   - TicketView: Kelas untuk menangani interaksi dengan pengguna.

   

