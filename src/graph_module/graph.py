class Passenger:
    def __init__(self, name, ticket_number):
        self.name = name
        self.ticket_number = ticket_number


    def __rep__(self):
        return f"<Passenger: {self.name}, Ticket: {self.ticket_number}>"

class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_passenger(self, passenger: Passenger):
        if passenger.ticket_number in self.adjacency:
            raise ValueError(f"Passenger with ticket {passenger.ticket_number} already exists.")
        self.adjacency[passenger.ticket_number] = []

    def add_connection(self, from_ticket: str, to_ticket: str):
        if from_ticket not in self.adjacency or to_ticket not in self.adjacency:
            raise ValueError("Both passengers must exist to create a connection.")
        if to_ticket not in self.adjacency[from_ticket]:
            self.adjacency[from_ticket].append(to_ticket)

    def remove_passenger(self, ticket_number: str):
        if ticket_number not in self.adjacency:
            raise ValueError(f"Passenger with ticket {ticket_number} does not exist.")
        self.adjacency.pop(ticket_number)
        for connections in self.adjacency.values():
            if ticket_number in connections:
                connections.remove(ticket_number)

    def get_connections(self, ticket_number: str):
        return self.adjacency.get(ticket_number, [])

    def get_all_passengers(self):
        return list(self.adjacency.keys())

    def has_passenger(self, ticket_number: str) -> bool:
        return ticket_number in self.adjacency
