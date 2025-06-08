from sympy import Symbol, sympify, lambdify, integrate
import numpy as np
from tkinter import messagebox

def plot_integral_area(widgets):
    expr_input = widgets["equation_entry"].get()
    x = Symbol("x")

    try:
        a = float(widgets["lower_bound_entry"].get())
        b = float(widgets["upper_bound_entry"].get())
        if a >= b:
            raise ValueError("Lower bound must be less than upper bound")

        expr = sympify(expr_input)
        func = lambdify(x, expr, "numpy")
        x_vals = np.linspace(a - 1, b + 1, 400)
        y_vals = func(x_vals)

        x_fill = np.linspace(a, b, 300)
        y_fill = func(x_fill)
        area = integrate(expr, (x, a, b))

        ax = widgets["ax"]
        ax.clear()
        ax.plot(x_vals, y_vals, label=f"y = {expr}", color="blue")
        ax.fill_between(x_fill, y_fill, color="green", alpha=0.3, label=f"Area ≈ {area.evalf():.4f}")
        ax.set_title("Integral Area")
        ax.grid(True)
        ax.legend()
        widgets["canvas"].draw()
    except Exception as e:
        messagebox.showerror("Error", str(e))
