# Programming For Developers Assignment

This repository contains solutions for all questions in the Programming For Developers (ST5008CEM) coursework. Each question is implemented in its own module, with clear comments, docstrings, and test cases.

## Structure
- `question1/`: Solutions for Question 1 (a and b)
- `question2/`: Solutions for Question 2 (a and b)
- `question3/`: Solutions for Question 3 (a and b)
- `question4/`: Solutions for Question 4 (a and b)
- `question5/`: Solutions for Question 5 (a and b, with GUIs)
- `question6/`: Solution for Question 6 (traffic signal management GUI)
- `tests/`: Unit tests for algorithmic questions

## How to Run

### 1. Requirements
- Python 3.8+
- No external packages required for core algorithms. For GUI questions, standard `tkinter` is used (comes with most Python installations).

### 2. Running Algorithmic Solutions
Each question can be run directly:
```bash
python question1/maximize_revenue.py
python question1/pin_policy.py
python question2/weather_anomaly.py
python question2/alphametic_solver.py
python question3/pattern_sequence.py
python question3/magical_words.py
python question4/secure_transmission.py
python question4/treasure_hunt.py
```

### 3. Running GUI Solutions
- **Maze Solver:**
  ```bash
  python question5/maze_solver.py
  ```
  - Choose DFS/BFS or generate a new maze. Start and end points are green and red.
- **Ticket Booking System:**
  ```bash
  python question5/ticket_booking.py
  ```
  - Simulate bookings, choose locking mechanism, and process bookings.
- **Traffic Signal Management:**
  ```bash
  python question6/traffic_signal.py
  ```
  - Add vehicles, toggle signals, and enable emergency mode.

### 4. Running Tests
Run all tests using:
```bash
python -m unittest discover tests
```
Or run a specific test file:
```bash
python tests/test_question1.py
```

## Author
- Name: BalKrishna Yadav


---

Replace the placeholders above with your actual details before submission. For full marks, ensure you understand and can explain each solution during your VIVA.
