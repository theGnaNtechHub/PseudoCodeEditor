# parser.py

def evaluate_pseudocode(code: str):
    """
    Evaluates simple pseudo-code with variable assignments and print statements.
    
    Supported syntax:
    - Variable assignments: x = 10
    - Expressions with +, -, *, /: print x + y
    - Only one statement per line
    """
    
    lines = code.strip().split('\n')
    variables = {}   # To hold variable names and values
    output = []      # To collect printed outputs

    for i, line in enumerate(lines, start=1):
        line = line.strip()

        if not line:
            continue  # skip empty lines

        try:
            if line.startswith("print"):
                # Handle print statement
                expr = line[5:].strip()  # Remove 'print'
                result = eval(expr, {}, variables)
                output.append(str(result))

            elif "=" in line:
                # Handle assignment: var = expr
                var, expr = line.split("=", 1)
                var = var.strip()
                expr = expr.strip()
                value = eval(expr, {}, variables)
                variables[var] = value

            else:
                return {
                    "status": "error",
                    "line": i,
                    "message": f"Invalid statement: '{line}'"
                }

        except Exception as e:
            return {
                "status": "error",
                "line": i,
                "message": f"{type(e).__name__} at line {i}: {str(e)}"
            }

    return {
        "status": "success",
        "variables": variables,
        "output": "\n".join(output)
    }
