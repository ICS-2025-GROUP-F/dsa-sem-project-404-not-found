from typing import Union

class Passenger:
    def __init__(self, name, ticket_number):
        self.name = name
        self.ticket_number = ticket_number

    def __repr__(self):
        return f"<Passenger: {self.name}, Ticket: {self.ticket_number}>"

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: Passenger) -> None:
        self.items.append(item)

    def pop(self) -> Passenger:
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop.")
        return self.items.pop()


    def peek(self) -> Union[Passenger, None]:
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def get_all(self):
        return self.items.copy()