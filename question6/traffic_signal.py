"""
Question 6: Traffic Signal Management System (Multithreaded GUI)

Simulates a traffic intersection with FIFO and priority queueing for vehicles, with multithreaded signal and vehicle management.
"""
import tkinter as tk
import threading
import time
import random
from collections import deque
from queue import PriorityQueue

# --- Constants for UI Customization ---
BG_COLOR = "#2c3e50"
ROAD_COLOR = "#34495e"
LINE_COLOR = "#bdc3c7"
LIGHT_RED = "#c0392b"
LIGHT_YELLOW = "#f1c40f"
LIGHT_GREEN = "#27ae60"
BUTTON_BG = "#3498db"
BUTTON_FG = "#ecf0f1"
FONT_STYLE = ("Helvetica", 10, "bold")

class TrafficSignalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Traffic Signal Management System")
        self.master.configure(bg=BG_COLOR)
        self.running = True
        self.signal_state = "Red"
        self.vehicle_queue = deque()
        self.emergency_queue = PriorityQueue()
        self.vehicles_on_road = []
        self.continuous_add = False
        self.car_colors = ["#e74c3c", "#9b59b6", "#2ecc71", "#1abc9c", "#f39c12"]

        self.setup_gui()
        self.start_threads()

    def setup_gui(self):
        self.canvas = tk.Canvas(self.master, width=800, height=500, bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack(pady=10)
        self.draw_intersection()

        # --- Control Frame ---
        control_frame = tk.Frame(self.master, bg=BG_COLOR)
        control_frame.pack(pady=10)

        button_style = {"bg": BUTTON_BG, "fg": BUTTON_FG, "font": FONT_STYLE, "relief": tk.FLAT, "padx": 10, "pady": 5}
        tk.Button(control_frame, text="Add Car", command=self.add_vehicle, **button_style).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Add Emergency", command=self.add_emergency_vehicle, **button_style).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Toggle Auto-Add", command=self.toggle_continuous_add, **button_style).pack(side=tk.LEFT, padx=5)

        # --- Status Frame ---
        status_frame = tk.Frame(self.master, bg=BG_COLOR)
        status_frame.pack(pady=10)
        self.queue_label = tk.Label(status_frame, text="Waiting Cars: 0", font=FONT_STYLE, fg=BUTTON_FG, bg=BG_COLOR)
        self.queue_label.pack(side=tk.LEFT, padx=10)
        self.emergency_label = tk.Label(status_frame, text="Waiting Emergency: 0", font=FONT_STYLE, fg=LIGHT_RED, bg=BG_COLOR)
        self.emergency_label.pack(side=tk.LEFT, padx=10)

    def draw_intersection(self):
        # Roads
        self.canvas.create_rectangle(0, 200, 800, 300, fill=ROAD_COLOR, outline="") # Horizontal
        self.canvas.create_rectangle(350, 0, 450, 500, fill=ROAD_COLOR, outline="") # Vertical
        # Dashed lines
        for i in range(0, 800, 30):
            self.canvas.create_line(i, 250, i + 15, 250, fill=LINE_COLOR, width=2, dash=(4, 8))
        # Traffic light
        self.update_light_color()

    def add_vehicle(self, emergency=False):
        v_type = "Ambulance" if emergency else "Car"
        if emergency:
            self.emergency_queue.put((1, v_type))
        else:
            self.vehicle_queue.append(v_type)
        self.update_queue_labels()

    def add_emergency_vehicle(self):
        self.add_vehicle(emergency=True)

    def toggle_continuous_add(self):
        self.continuous_add = not self.continuous_add

    def start_threads(self):
        threading.Thread(target=self.signal_thread, daemon=True).start()
        threading.Thread(target=self.vehicle_processing_thread, daemon=True).start()
        threading.Thread(target=self.continuous_add_thread, daemon=True).start()
        self.master.after(50, self.animate_vehicles)

    def signal_thread(self):
        while self.running:
            self.signal_state = "Red"
            self.update_light_color()
            time.sleep(7)
            self.signal_state = "Green"
            self.update_light_color()
            time.sleep(5)
            self.signal_state = "Yellow"
            self.update_light_color()
            time.sleep(2)

    def continuous_add_thread(self):
        while self.running:
            if self.continuous_add:
                self.add_vehicle()
            time.sleep(random.uniform(1, 3))

    def vehicle_processing_thread(self):
        while self.running:
            if self.signal_state == "Green":
                if not self.emergency_queue.empty():
                    _, v_type = self.emergency_queue.get()
                    self.create_vehicle_animation(v_type, emergency=True)
                elif self.vehicle_queue:
                    v_type = self.vehicle_queue.popleft()
                    self.create_vehicle_animation(v_type)
                self.update_queue_labels()
            time.sleep(1)

    def create_vehicle_animation(self, v_type, emergency=False):
        color = LIGHT_RED if emergency else random.choice(self.car_colors)
        # Vehicle Body
        vehicle_id = self.canvas.create_rectangle(200, 235, 240, 265, fill=color, outline="black", width=1)
        # Vehicle Roof
        roof_id = self.canvas.create_rectangle(210, 225, 230, 235, fill=color, outline="black", width=1)
        self.vehicles_on_road.append((vehicle_id, roof_id))

    def animate_vehicles(self):
        for vehicle_id, roof_id in self.vehicles_on_road[:]:
            self.canvas.move(vehicle_id, 5, 0)
            self.canvas.move(roof_id, 5, 0)
            x1, _, _, _ = self.canvas.coords(vehicle_id)
            if x1 > 800:
                self.canvas.delete(vehicle_id)
                self.canvas.delete(roof_id)
                self.vehicles_on_road.remove((vehicle_id, roof_id))
        self.master.after(50, self.animate_vehicles)

    def update_light_color(self):
        self.canvas.delete("light")
        light_map = {"Red": LIGHT_RED, "Yellow": LIGHT_YELLOW, "Green": LIGHT_GREEN}
        self.canvas.create_oval(460, 160, 490, 190, fill=light_map[self.signal_state], tags="light", outline="white")

    def update_queue_labels(self):
        self.queue_label.config(text=f"Waiting Cars: {len(self.vehicle_queue)}")
        self.emergency_label.config(text=f"Waiting Emergency: {self.emergency_queue.qsize()}")

    def on_close(self):
        self.running = False
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficSignalGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
