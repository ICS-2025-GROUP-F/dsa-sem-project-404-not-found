import tkinter as tk
from tkinter import messagebox
from src.graph_module.graph import Graph, Passenger
from src.graph_module import graph_db

# Initialize database tables
graph_db.create_tables()

class GraphApp:
    """Graph Management UI using Tkinter"""

    def __init__(self, root):
        self.root = root
        self.root.title("Graph Management")
        self.graph = Graph()

        # Load passengers from DB
        passengers = graph_db.fetch_all_passengers()
        for row in passengers:
            p = Passenger(row["name"], row["ticket_number"])
            self.graph.add_passenger(p)

        # Load connections from DB
        connections = graph_db.fetch_all_connections()
        for from_ticket, to_ticket in connections:
            try:
                self.graph.add_connection(from_ticket, to_ticket)
            except:
                pass  # Skip if invalid

        # GUI Layout
        tk.Label(root, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Ticket #:").grid(row=1, column=0)
        self.ticket_entry = tk.Entry(root)
        self.ticket_entry.grid(row=1, column=1)

        tk.Label(root, text="Connect To Ticket #:").grid(row=2, column=0)
        self.connect_entry = tk.Entry(root)
        self.connect_entry.grid(row=2, column=1)

        tk.Button(root, text="Add Passenger", command=self.add_passenger).grid(row=3, column=0, pady=5)
        tk.Button(root, text="Add Connection", command=self.add_connection).grid(row=3, column=1, pady=5)
        tk.Button(root, text="Remove Passenger", command=self.remove_passenger).grid(row=4, column=0, pady=5)
        tk.Button(root, text="View Connections", command=self.view_connections).grid(row=4, column=1, pady=5)
        tk.Button(root, text="View All", command=self.view_all).grid(row=5, column=0, columnspan=2)

        self.output = tk.Text(root, height=10, width=50)
        self.output.grid(row=6, column=0, columnspan=2, pady=10)

    def add_passenger(self):
        """Add a new passenger to the graph and database."""
        name = self.name_entry.get().strip()
        ticket = self.ticket_entry.get().strip()
        if not name or not ticket:
            messagebox.showerror("Input Error", "Name and Ticket # required.")
            return
        try:
            p = Passenger(name, ticket)
            self.graph.add_passenger(p)
            graph_db.insert_passenger(name, ticket)
            self.output.insert(tk.END, f"Added: {p}\n")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def add_connection(self):
        """Add a connection between two passengers (by ticket number)."""
        from_ticket = self.ticket_entry.get().strip()
        to_ticket = self.connect_entry.get().strip()
        if not from_ticket or not to_ticket:
            messagebox.showerror("Input Error", "Both ticket numbers required.")
            return
        try:
            self.graph.add_connection(from_ticket, to_ticket)
            graph_db.insert_connection(from_ticket, to_ticket)
            self.output.insert(tk.END, f"Connected {from_ticket} → {to_ticket}\n")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def remove_passenger(self):
        """Remove a passenger from the graph and DB by ticket number."""
        ticket = self.ticket_entry.get().strip()
        if not ticket:
            messagebox.showerror("Input Error", "Ticket # required.")
            return
        try:
            self.graph.remove_passenger(ticket)
            graph_db.delete_passenger_by_ticket(ticket)
            self.output.insert(tk.END, f"Removed passenger with ticket {ticket}\n")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def view_connections(self):
        """Display connections for a specific passenger."""
        ticket = self.ticket_entry.get().strip()
        if not ticket:
            messagebox.showerror("Input Error", "Ticket # required.")
            return
        connections = self.graph.get_connections(ticket)
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, f"Connections for {ticket}: {connections}\n")

    def view_all(self):
        """Display all passengers and their connections."""
        self.output.delete(1.0, tk.END)
        passengers = self.graph.get_all_passengers()
        if not passengers:
            self.output.insert(tk.END, "Graph is empty.\n")
        else:
            for t in passengers:
                self.output.insert(tk.END, f"{t} → {self.graph.get_connections(t)}\n")

# Entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()