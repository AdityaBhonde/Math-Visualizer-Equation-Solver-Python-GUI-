def validate_expression(expr):
    if not expr or not isinstance(expr, str):
        raise ValueError("Expression must be a valid string.")
