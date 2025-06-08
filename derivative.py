from sympy import sympify, Symbol, lambdify
import numpy as np
from tkinter import messagebox

def plot_derivative(widgets):
    equation_entry = widgets["equation_entry"]
    ax = widgets["ax"]
    canvas = widgets["canvas"]

    expr_input = equation_entry.get()
    x = Symbol('x')

    try:
        # Parse original function
        expr = sympify(expr_input)
        func = lambdify(x, expr, modules=['numpy'])

        # Calculate derivative
        derivative_expr = expr.diff(x)
        derivative_func = lambdify(x, derivative_expr, modules=['numpy'])

        # X values for plot
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)
        dy_vals = derivative_func(x_vals)

        # Plot both original and derivative
        ax.clear()
        ax.plot(x_vals, y_vals, label=f"f(x) = {expr}", color="blue")
        ax.plot(x_vals, dy_vals, label=f"f'(x) = {derivative_expr}", color="red", linestyle="--")
        ax.set_title("Function and Its Derivative")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)
        ax.legend()
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Derivative Error", f"Could not plot derivative:\n{e}")
