"""
Question 5b: Online Ticket Booking System with Concurrency Control (GUI)

Simulates a ticket booking system with concurrency control and a GUI.
"""
import tkinter as tk
import threading
import random
import time
from queue import Queue

SEATS = 30

class BookingSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Ticket Booking System")
        self.seats = [False for _ in range(SEATS)]
        self.requests = Queue()
        self.locking = tk.StringVar(value="optimistic")
        self.buttons = []
        self.setup_gui()
        self.processing = False

    def setup_gui(self):
        frame = tk.Frame(self.master)
        frame.pack()
        for i in range(SEATS):
            btn = tk.Button(frame, text=str(i+1), width=3, bg="lightgreen", command=lambda i=i: self.manual_book(i))
            btn.grid(row=i//10, column=i%10)
            self.buttons.append(btn)
        tk.Button(self.master, text="Simulate Booking Requests", command=self.simulate_requests).pack()
        tk.Button(self.master, text="Process Bookings", command=self.process_bookings).pack()
        tk.Radiobutton(self.master, text="Optimistic Locking", variable=self.locking, value="optimistic").pack(anchor=tk.W)
        tk.Radiobutton(self.master, text="Pessimistic Locking", variable=self.locking, value="pessimistic").pack(anchor=tk.W)
        self.status = tk.Label(self.master, text="Status: Idle")
        self.status.pack()

    def manual_book(self, seat):
        if not self.seats[seat]:
            self.requests.put(seat)
            self.status.config(text=f"Manual booking request for seat {seat+1} queued.")
        else:
            self.status.config(text=f"Seat {seat+1} already booked.")

    def simulate_requests(self):
        for _ in range(10):
            seat = random.randint(0, SEATS-1)
            self.requests.put(seat)
        self.status.config(text="10 random booking requests queued.")

    def process_bookings(self):
        if self.processing:
            return
        self.processing = True
        threading.Thread(target=self._process_bookings_thread, daemon=True).start()

    def _process_bookings_thread(self):
        while not self.requests.empty():
            seat = self.requests.get()
            if self.locking.get() == "optimistic":
                self.optimistic_book(seat)
            else:
                self.pessimistic_book(seat)
            time.sleep(0.2)
        self.status.config(text="All bookings processed.")
        self.processing = False

    def optimistic_book(self, seat):
        # Simulate optimistic locking
        if not self.seats[seat]:
            # Simulate possible race
            time.sleep(random.uniform(0, 0.05))
            if not self.seats[seat]:
                self.seats[seat] = True
                self.buttons[seat].config(bg="red")
                self.status.config(text=f"Seat {seat+1} booked (optimistic).")
            else:
                self.status.config(text=f"Seat {seat+1} booking failed (already booked).")
        else:
            self.status.config(text=f"Seat {seat+1} already booked.")

    def pessimistic_book(self, seat):
        # Simulate pessimistic locking with a threading.Lock
        lock = threading.Lock()
        with lock:
            if not self.seats[seat]:
                self.seats[seat] = True
                self.buttons[seat].config(bg="red")
                self.status.config(text=f"Seat {seat+1} booked (pessimistic).")
            else:
                self.status.config(text=f"Seat {seat+1} already booked.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookingSystemGUI(root)
    root.mainloop()
