import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from plotting import plot_equation
from derivative import plot_derivative
from integral import plot_integral_area
from solver import solve_equation_steps

# Create main window
root = tk.Tk()
root.title("Math Visualizer")
root.geometry("1100x700")
root.configure(bg="white")

# ========== Top Input Row ==========
top_frame = tk.Frame(root, bg="white")
top_frame.pack(pady=10)

tk.Label(top_frame, text="Enter Equation (in terms of x):", bg="white").pack(side=tk.LEFT, padx=5)
equation_entry = tk.Entry(top_frame, width=35, font=("Arial", 12))
equation_entry.pack(side=tk.LEFT, padx=5)

tk.Button(top_frame, text="Plot", bg="#bde0fe", command=lambda: plot_equation(widgets)).pack(side=tk.LEFT, padx=5)
tk.Button(top_frame, text="Plot Derivative", bg="#ffb703", command=lambda: plot_derivative(widgets)).pack(side=tk.LEFT, padx=5)

# ========== Bounds Input Row ==========
bounds_frame = tk.Frame(root, bg="white")
bounds_frame.pack(pady=5)

tk.Label(bounds_frame, text="Lower Bound (a):", bg="white").pack(side=tk.LEFT, padx=5)
lower_bound_entry = tk.Entry(bounds_frame, width=10)
lower_bound_entry.pack(side=tk.LEFT)

tk.Label(bounds_frame, text="Upper Bound (b):", bg="white").pack(side=tk.LEFT, padx=5)
upper_bound_entry = tk.Entry(bounds_frame, width=10)
upper_bound_entry.pack(side=tk.LEFT)

tk.Button(bounds_frame, text="Plot Area", bg="#e0fbfc", command=lambda: plot_integral_area(widgets)).pack(side=tk.LEFT, padx=10)

# ========== Graph Area ==========
figure = plt.Figure(figsize=(7, 4), dpi=100)
ax = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(pady=10)

# ========== Step-by-Step Solver ==========
solver_frame = tk.Frame(root, bg="white", pady=10)
solver_frame.pack(fill=tk.X)

tk.Label(solver_frame, text="Step-by-Step Equation Solver", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", padx=10)

entry_frame = tk.Frame(solver_frame, bg="white")
entry_frame.pack(fill=tk.X, padx=10, pady=5)

tk.Label(entry_frame, text="Equation (e.g., x**2 + 2*x + 1 = 0):", bg="white").pack(side=tk.LEFT)
eq_entry = tk.Entry(entry_frame, width=40)
eq_entry.pack(side=tk.LEFT, padx=5)

tk.Button(entry_frame, text="Solve", bg="#90ee90", command=lambda: solve_equation_steps(widgets)).pack(side=tk.LEFT)

# ========== Scrollable Output Box ==========
output_frame = tk.Frame(root)
output_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(output_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_box = tk.Text(output_frame, height=8, font=("Courier", 10), yscrollcommand=scrollbar.set, wrap=tk.WORD)
output_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=output_box.yview)

# ========== Widgets Dictionary ==========
widgets = {
    "root": root,
    "ax": ax,
    "canvas": canvas,
    "equation_entry": equation_entry,
    "lower_bound_entry": lower_bound_entry,
    "upper_bound_entry": upper_bound_entry,
    "eq_entry": eq_entry,
    "output_box": output_box,
}

# Run the application
root.mainloop()
