class Passenger:
    def __init__(self, name, ticket_number):
        self.name = name
        self.ticket_number = ticket_number

    def __repr__(self):
        return f"{self.name} ({self.ticket_number})"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def is_empty(self) -> bool:
        return self.head is None

    def insert(self, passenger: Passenger):
        new_node = Node(passenger)
        if self.head is None:
            self.head = new_node
        else:
            # Insert at end
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_by_ticket(self, ticket_number: str):
        current = self.head
        prev = None
        while current:
            if current.data.ticket_number == ticket_number:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return current.data  # Return deleted passenger
            prev = current
            current = current.next
        raise ValueError(f"Passenger with Ticket {ticket_number} not found.")

    def search(self, ticket_number: str):
        current = self.head
        while current:
            if current.data.ticket_number == ticket_number:
                return current.data
            current = current.next
        return None

    def get_all(self):
        passengers = []
        current = self.head
        while current:
            passengers.append(current.data)
            current = current.next
        return passengers