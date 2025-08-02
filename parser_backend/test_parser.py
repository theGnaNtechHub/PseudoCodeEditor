#!/usr/bin/env python3

from parser import PseudoCodeParser, evaluate_pseudocode

# Test the for loop conversion
test_code = """
for i = 1 to 5 do
    print "Iteration:"
    print i
endfor
"""

parser = PseudoCodeParser()
converted = parser.preprocess_code(test_code)

print("Original pseudo-code:")
print(test_code)
print("\nConverted Python code:")
print(converted)
print("\n---")

# Test with a simpler version
test_code2 = """
for i = 1 to 5
    print "Iteration:"
    print i
endfor
"""

converted2 = parser.preprocess_code(test_code2)
print("Original pseudo-code (without 'do'):")
print(test_code2)
print("\nConverted Python code:")
print(converted2)

print("\n--- Testing Evaluation ---")
result = evaluate_pseudocode(test_code)
print("Evaluation result:")
print(result) 