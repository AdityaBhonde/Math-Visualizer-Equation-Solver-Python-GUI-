from sympy import Symbol, Eq, sympify, simplify, solve

def solve_equation_steps(widgets):
    output_box = widgets["output_box"]
    eq_input = widgets["eq_entry"].get()
    output_box.delete("1.0", "end")

    try:
        if '=' not in eq_input:
            raise ValueError("Missing '=' in equation.")
        x = Symbol("x")
        left, right = eq_input.split("=")
        left_expr = simplify(sympify(left))
        right_expr = simplify(sympify(right))

        output_box.insert("end", f"Step 1: Simplify both sides\n")
        output_box.insert("end", f"        {left_expr} = {right_expr}\n\n")

        diff = left_expr - right_expr
        factors = diff.factor()
        output_box.insert("end", f"Step 2: Factor expression\n")
        output_box.insert("end", f"        {factors} = 0\n\n")

        output_box.insert("end", f"Step 3: Solve\n")
        sols = solve(factors, x)
        if sols:
            for i, sol in enumerate(sols, 1):
                output_box.insert("end", f"        Solution {i}: x = {sol}\n")
        else:
            output_box.insert("end", f"        No real solution found.\n")
    except Exception as e:
        output_box.insert("end", f"Error: {e}")
