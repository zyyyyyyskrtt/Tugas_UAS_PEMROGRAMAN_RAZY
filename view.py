
class TicketView:
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

    def display_tickets(self, tickets):
        print(f"{'Nama Penumpang':<20}{'Tujuan':<20}")
        print("-" * 40)
        for ticket in tickets:
            print(f"{ticket['passenger_name']:<20}{ticket['destination']:<20}")
