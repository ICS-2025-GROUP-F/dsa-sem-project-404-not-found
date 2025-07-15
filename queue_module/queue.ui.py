import tkinter as tk
from tkinter import messagebox
from queue_module.queue import Queue,Passenger
from queue_module import queue_db
queue_db.create_table()

class QueueApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Queue Management")
        self.queue = Queue()
        queue_db.create_table()
        passengers =queue_db.fetch_all_passengers()
        for row in passengers:
            p=Passenger(row["name"],row["ticket_number"])
            self.queue.enqueue(p)

        tk.Label(root,text="Name:").grid(row=0,column=0)
        self.name_entry=tk.Entry(root)
        self.name_entry.grid(row=0,column=1)

        tk.Label(root, text="Ticket #: ").grid(row=1,column=0)
        self.ticket_entry =tk.Entry(root)
        self.ticket_entry.grid(row=1,column=1)

        tk.Button(root,text="Enqueue",command=self.enqueue).grid(row=2,column=0,pady=5)
        tk.Button(root,text="Dequeue", command=self.dequeue).grid(row=2,column=1,pady=5)
        tk.Button(root,text="View Queue",command=self.view_queue).grid(row=3,column=0,columnspan=2)
        tk.Button(root,text="peek",command=self.peek).grid(row=3,column=1)
        self.output = tk.Text(root,height =10,width=40)
        self.output.grid(row=4,column=0, columnspan=2,pady=10)

    def enqueue(self):
        name = self.name_entry.get().strip()
        ticket = self.ticket_entry.get().strip()
        if not name or not ticket:
            messagebox.showerror("Input Error","Both fields are required.")
            return
        p = Passenger(name,ticket)
        self.queue.enqueue(p)
        queue_db.insert_passenger(name,ticket)
        messagebox.showinfo("Success",f"Enqueued:{p}")

    def dequeue(self):
        try:
            p=self.queue.dequeue()
            queue_db.delete_passenger_by_ticket(p.ticket_number)
            messagebox.showinfo("Dequeued",f"Dequeued:{p}")
        except IndexError as e:
            messagebox.showerror("Queue Empty",str(e))

    def view_queue(self):
        self.output.delete(1.0,tk.END)
        if self.queue.is_empty():
            self.output.insert(tk.END,"Queue is empty.\n")
        else:
            for p in self.queue.get_all():
                self.output.insert(tk.END,f"{p}\n")
    def peek(self):
        p=self.queue.peek()
        self.output.delete(1.0,tk.END)
        if p is None:
            self.output.insert(tk.END,"Queue is Empty.\n")
        else:
            self.output.insert(tk.END,f"Next Passenger:{p}\n")

if __name__== "__main__":
    root=tk.Tk()
    app=QueueApp(root)
    root.mainloop()

