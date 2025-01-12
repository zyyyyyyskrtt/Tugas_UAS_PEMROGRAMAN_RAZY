
class TicketProcess:
    def __init__(self, data, view):
        self.data = data
        self.view = view

    def add_ticket(self):
        ticket = self.view.input_ticket()
        if ticket:
            self.data.add_ticket(ticket)

    def show_tickets(self):
        tickets = self.data.get_tickets()
        self.view.display_tickets(tickets)
