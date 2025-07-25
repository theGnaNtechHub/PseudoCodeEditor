# parser.py
"""
    Evaluates pseudo-code with variable assignments, print statements, and simple if-else blocks.

    Supports:
    - Assignments: x = 10
    - Expressions: +, -, *, /, string concat, boolean logic
    - Strings and Booleans: name = "John", flag = True
    - Print: print x
    - If-Else (4-space indentation, no nesting)
"""

import sys
import io

def evaluate_pseudocode(code: str):
    lines = code.strip().split('\n')
    variables = {}
    output_buffer = io.StringIO()

    # Fix print statements: make print x ➝ print(x)
    fixed_lines = []
    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(stripped)

        if stripped.startswith("print ") and not stripped.startswith("print("):
            expr = stripped[6:]  # Remove 'print '
            fixed_line = " " * indent + f"print({expr})"
        else:
            fixed_line = line
        fixed_lines.append(fixed_line)

    final_code = "\n".join(fixed_lines)

    try:
        # Redirect stdout to capture prints
        original_stdout = sys.stdout
        sys.stdout = output_buffer

        # Execute the code in a restricted scope
        exec(final_code, {}, variables)

        sys.stdout = original_stdout  # Restore stdout
        output_text = output_buffer.getvalue().strip()

    except Exception as e:
        sys.stdout = original_stdout  # Ensure stdout is always restored
        return {
            "status": "error",
            "message": f"{type(e).__name__}: {str(e)}"
        }

    return {
        "status": "success",
        "variables": {k: v for k, v in variables.items() if not k.startswith('__')},
        "output": output_text
    }
