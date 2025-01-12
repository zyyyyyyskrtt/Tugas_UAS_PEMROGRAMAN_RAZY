
class TicketData:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def get_tickets(self):
        return self.tickets
