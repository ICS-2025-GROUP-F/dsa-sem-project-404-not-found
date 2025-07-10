import tkinter as tk
from tkinter import messagebox
from src.Linkedlist_module.linked_list import LinkedList, Passenger
from src.Linkedlist_module import linkedlist_db

linkedlist_db.create_table()


class LinkedListApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Linked List Management")
        self.llist = LinkedList()

        passengers = linkedlist_db.fetch_all_passengers()
        for row in passengers:
            p = Passenger(row["name"], row["ticket_number"])
            self.llist.insert(p)

        tk.Label(root, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Ticket #:").grid(row=1, column=0)
        self.ticket_entry = tk.Entry(root)
        self.ticket_entry.grid(row=1, column=1)

        tk.Button(root, text="Insert", command=self.insert).grid(row=2, column=0, pady=5)
        tk.Button(root, text="Delete", command=self.delete).grid(row=2, column=1, pady=5)
        tk.Button(root, text="Search", command=self.search).grid(row=3, column=0, pady=5)
        tk.Button(root, text="View All", command=self.view_all).grid(row=3, column=1, pady=5)

        self.output = tk.Text(root, height=10, width=40)
        self.output.grid(row=4, column=0, columnspan=2, pady=10)

    def insert(self):
        name = self.name_entry.get().strip()
        ticket = self.ticket_entry.get().strip()
        if not name or not ticket:
            messagebox.showerror("Input Error", "Both fields are required.")
            return
        p = Passenger(name, ticket)
        self.llist.insert(p)
        linkedlist_db.insert_passenger(name, ticket)
        messagebox.showinfo("Success", f"Inserted: {p}")

    def delete(self):
        ticket = self.ticket_entry.get().strip()
        if not ticket:
            messagebox.showerror("Input Error", "Ticket # required.")
            return
        try:
            deleted = self.llist.delete_by_ticket(ticket)
            linkedlist_db.delete_passenger_by_ticket(ticket)
            messagebox.showinfo("Deleted", f"Deleted: {deleted}")
        except ValueError as e:
            messagebox.showerror("Not Found", str(e))

    def search(self):
        ticket = self.ticket_entry.get().strip()
        if not ticket:
            messagebox.showerror("Input Error", "Ticket # required.")
            return
        found = self.llist.search(ticket)
        if found:
            messagebox.showinfo("Found", f"Found: {found}")
        else:
            messagebox.showinfo("Not Found", "Passenger not found.")

    def view_all(self):
        self.output.delete(1.0, tk.END)
        if self.llist.is_empty():
            self.output.insert(tk.END, "Linked List is empty.\n")
        else:
            for p in self.llist.get_all():
                self.output.insert(tk.END, f"{p}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListApp(root)
    root.mainloop()