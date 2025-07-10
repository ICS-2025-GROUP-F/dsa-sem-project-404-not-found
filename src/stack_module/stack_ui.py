import tkinter as tk
from tkinter import messagebox
from src.stack_module import stack_db
from src.stack_module.stack import Stack, Passenger


stack_db.create_table()


class StackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack Management System")
        self.stack = Stack()

        passengers = stack_db.fetch_all_passengers()
        for row in reversed(passengers):
            p = Passenger(row["name"], row["ticket_number"])
            self.stack.push(p)

        tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Ticket #:").grid(row=1, column=0, sticky="e")
        self.ticket_entry = tk.Entry(root)
        self.ticket_entry.grid(row=1, column=1)

        tk.Button(root, text="Push", command=self.push).grid(row=2, column=0, pady=5)
        tk.Button(root, text="Pop", command=self.pop).grid(row=2, column=1, pady=5)
        tk.Button(root, text="View Stack", command=self.view_stack).grid(row=3, column=0, columnspan=2)

        self.output = tk.Text(root, height=10, width=40)
        self.output.grid(row=4, column=0, columnspan=2, pady=10)

    def push(self):
        name = self.name_entry.get().strip()
        ticket = self.ticket_entry.get().strip()
        if not name or not ticket:
            messagebox.showerror("Input Error", "Both name and ticket number are required.")
            return
        try:
            p = Passenger(name, ticket)
            self.stack.push(p)
            stack_db.insert_passenger(name, ticket)
            messagebox.showinfo("Success", f"Pushed: {p}")
        except ValueError as e:
            messagebox.showerror("Database Error", str(e))

    def pop(self):
        try:
            p = self.stack.pop()
            stack_db.delete_passenger_by_ticket(p.ticket_number)
            messagebox.showinfo("Popped", f"Popped: {p}")
        except IndexError as e:
            messagebox.showerror("Stack Empty", str(e))

    def view_stack(self):
        self.output.delete(1.0, tk.END)
        if self.stack.is_empty():
            self.output.insert(tk.END, "Stack is empty.\n")
        else:
            for p in reversed(self.stack.get_all()):
                self.output.insert(tk.END, f"{p}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = StackApp(root)
    root.mainloop()
