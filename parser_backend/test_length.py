#!/usr/bin/env python3

from parser import PseudoCodeParser, evaluate_pseudocode

# Test the length() function conversion
test_code = """
// Test length() function
numbers = [1, 2, 3, 4, 5]
arrayLength = length(numbers)
print "Array length:"
print arrayLength

// Test with string
message = "Hello World"
stringLength = length(message)
print "String length:"
print stringLength
"""

parser = PseudoCodeParser()
converted = parser.preprocess_code(test_code)

print("Original pseudo-code:")
print(test_code)
print("\nConverted Python code:")
print(converted)
print("\n---")

# Test the evaluation
result = evaluate_pseudocode(test_code)
print("Evaluation result:")
print(result) 