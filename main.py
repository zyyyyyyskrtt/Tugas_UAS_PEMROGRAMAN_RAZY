
from data import TicketData
from process import TicketProcess
from view import TicketView


def main():
    data = TicketData()
    view = TicketView()
    process = TicketProcess(data, view)

    while True:
        print("\n1. Tambah Tiket")
        print("2. Tampilkan Tiket")
        print("3. Keluar")

        choice = input("Pilih opsi: ")

        if choice == "1":
            process.add_ticket()
        elif choice == "2":
            process.show_tickets()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
