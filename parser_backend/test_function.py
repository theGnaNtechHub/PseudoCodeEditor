#!/usr/bin/env python3

from parser import PseudoCodeParser

# Test the function conversion
test_code = """
function calculateArea(length, width)
    area = length * width
    return area
endfunction

// Test function
result = calculateArea(5, 3)
print "Area of rectangle:"
print result
"""

parser = PseudoCodeParser()
converted = parser.preprocess_code(test_code)

print("Original pseudo-code:")
print(test_code)
print("\nConverted Python code:")
print(converted)
print("\n---") 