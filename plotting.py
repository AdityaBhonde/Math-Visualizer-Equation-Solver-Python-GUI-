from sympy import Symbol, lambdify, sympify
import numpy as np

def plot_equation(widgets):
    expr_input = widgets["equation_entry"].get()
    x = Symbol('x')
    try:
        expr = sympify(expr_input)
        func = lambdify(x, expr, modules=["numpy"])
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)

        ax = widgets["ax"]
        ax.clear()
        ax.plot(x_vals, y_vals, label=f"y = {expr}")
        ax.set_title("Graph of the Equation")
        ax.grid(True)
        ax.legend()
        widgets["canvas"].draw()
    except Exception as e:
        from tkinter import messagebox
        messagebox.showerror("Invalid Input", f"Error: {e}")
