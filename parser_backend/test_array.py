#!/usr/bin/env python3

from parser import PseudoCodeParser

# Test the array loop conversion
test_code = """
// Test 10: Array operations
numbers = [1, 2, 3, 4, 5]
sum = 0
for i = 0 to 4 do
    sum = sum + numbers[i]
endfor
print "Sum of array:"
print sum
"""

parser = PseudoCodeParser()
converted = parser.preprocess_code(test_code)

print("Original pseudo-code:")
print(test_code)
print("\nConverted Python code:")
print(converted)
print("\n---") 