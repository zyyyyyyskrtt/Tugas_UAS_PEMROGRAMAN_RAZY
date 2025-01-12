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

3. Kelas TicketProcess
   Metode __init__

            def __init__(self, data, view):
                self.data = data
                self.view = view
   - Metode __init__ adalah konstruktor yang dipanggil saat objek dari kelas TicketProcess dibuat.
   - data: Parameter ini diharapkan menjadi objek yang memiliki metode untuk mengelola data tiket, seperti menambahkan tiket dan mendapatkan daftar tiket.
   - view: Parameter ini diharapkan menjadi objek yang memiliki metode untuk menangani input dan output tiket, seperti meminta input dari pengguna dan menampilkan tiket.
   - self.data: Menyimpan referensi ke objek data yang diberikan.
   - self.view: Menyimpan referensi ke objek tampilan yang diberikan.

   Metode add_ticket

            def add_ticket(self):
                ticket = self.view.input_ticket()
                if ticket:
                    self.data.add_ticket(ticket)
   - Metode ini digunakan untuk menambahkan tiket baru ke dalam sistem.
   - Memanggil self.view.input_ticket() untuk meminta pengguna memasukkan informasi tiket (seperti nama penumpang dan tujuan).
   - Jika input tiket valid (tidak None), maka tiket tersebut ditambahkan ke dalam data dengan memanggil self.data.add_ticket(ticket).

    Metode show_tickets

            def show_tickets(self):
                tickets = self.data.get_tickets()
                self.view.display_tickets(tickets)
   - Metode ini digunakan untuk menampilkan semua tiket yang ada.
   - Mengambil daftar tiket dari objek data dengan memanggil self.data.get_tickets().
   - Menampilkan tiket yang diambil dengan memanggil self.view.display_tickets(tickets).

4. Kelas TicketView

            def input_ticket(self):
                try:
                   passenger_name = input("Masukkan nama penumpang: ")
                   if not passenger_name:
                       raise ValueError("Nama penumpang tidak boleh kosong")
            
                   destination = input("Masukkan tujuan: ")
                   if not destination:
                       raise ValueError("Tujuan tidak boleh kosong")
            
                   return {"passenger_name": passenger_name, "destination": destination}
            except ValueError as e:
                print(f"Input tidak valid: {e}")
                return None
     - Fungsi: Metode ini bertujuan untuk meminta input dari pengguna mengenai nama penumpang dan tujuan perjalanan.
     - Validasi Input: Nama penumpang tidak boleh kosong. Jika kosong, akan mengangkat ValueError dan Tujuan perjalanan tidak boleh kosong. Jika kosong, akan mengangkat            ValueError.
     - Pengembalian Data: Jika input valid, metode ini mengembalikan sebuah dictionary yang berisi passenger_name dan destination. Jika input tidak valid, mengembalikan            None.

   Metode display_tickets

            def display_tickets(self, tickets):
                print(f"{'Nama Penumpang':<20}{'Tujuan':<20}")
                print("-" * 40)
                for ticket in tickets:
                    print(f"{ticket['passenger_name']:<20}{ticket['destination']:<20}")
      - Fungsi: Metode ini bertujuan untuk menampilkan data tiket yang disimpan dalam format tabel.
      - Parameter: Menerima tickets, yang merupakan daftar tiket dalam bentuk dictionary.
      - Tampilan: Menampilkan header tabel dengan kolom "Nama Penumpang" dan "Tujuan", Menampilkan garis pemisah untuk memperjelas tampilan tabel, Melalui loop, menampilkan         setiap tiket dalam daftar tickets dalam format yang rapi.

## Hasil Program 
<img width="826" alt="gambar1" src="https://github.com/user-attachments/assets/ce8f86c7-4515-4eca-bc6f-ec13b0cd1eb7" />


     

   

