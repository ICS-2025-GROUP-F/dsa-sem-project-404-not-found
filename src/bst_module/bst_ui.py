import tkinter as tk
from tkinter import messagebox
from bst_module.binarysearchtree import BinarySearchTree, Passenger
from bst_module import bst_db

bst_db.create_table()

class BSTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Search Tree Management")
        self.bst = BinarySearchTree()

        # Load passengers from database
        passengers = bst_db.fetch_all_passengers()
        for row in passengers:
            p = Passenger(row["name"], row["ticket_number"])
            self.bst.insert(p)

        # UI Elements
        tk.Label(root, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Ticket #:").grid(row=1, column=0)
        self.ticket_entry = tk.Entry(root)
        self.ticket_entry.grid(row=1, column=1)

        tk.Button(root, text="Insert", command=self.insert).grid(row=2, column=0, pady=5)
        tk.Button(root, text="Search", command=self.search).grid(row=2, column=1, pady=5)
        tk.Button(root, text="Delete", command=self.delete).grid(row=3, column=0, pady=5)
        tk.Button(root, text="View Inorder", command=self.view_inorder).grid(row=3, column=1, pady=5)

        self.output = tk.Text(root, height=10, width=50)
        self.output.grid(row=4, column=0, columnspan=2, pady=10)

    def insert(self):
        name = self.name_entry.get().strip()
        ticket = self.ticket_entry.get().strip()
        if not name or not ticket:
            messagebox.showerror("Input Error", "Both fields are required.")
            return
        try:
            p = Passenger(name, ticket)
            self.bst.insert(p)
            bst_db.insert_passenger(name, ticket)
            messagebox.showinfo("Success", f"Inserted: {p}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def search(self):
        ticket = self.ticket_entry.get().strip()
        result = self.bst.search(ticket)
        self.output.delete(1.0, tk.END)
        if result:
            self.output.insert(tk.END, f"Found: {result}\n")
        else:
            self.output.insert(tk.END, "Passenger not found.\n")

    def delete(self):
        ticket = self.ticket_entry.get().strip()
        result = self.bst.search(ticket)
        if result:
            self.bst.delete(ticket)
            bst_db.delete_passenger_by_ticket(ticket)
            messagebox.showinfo("Deleted", f"Deleted: {result}")
        else:
            messagebox.showerror("Not Found", "Passenger not found.")

    def view_inorder(self):
        self.output.delete(1.0, tk.END)
        passengers = self.bst.inorder()
        if not passengers:
            self.output.insert(tk.END, "BST is empty.\n")
        else:
            for p in passengers:
                self.output.insert(tk.END, f"{p}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BSTApp(root)
    root.mainloop()
