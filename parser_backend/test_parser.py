#!/usr/bin/env python3
"""
Test file for the Pseudo-code Parser and Evaluator
Demonstrates all features and capabilities
"""

import json
from parser import (
    evaluate_pseudocode, 
    get_syntax_hints, 
    get_learning_suggestions,
    PseudoCodeParser,
    PseudoCodeEvaluator
)

def test_basic_operations():
    """Test basic variable assignments and operations."""
    print("=== Testing Basic Operations ===")
    
    code = """
    // Basic variable assignments
    x = 10
    y = 20
    z = x + y
    name = "John"
    is_valid = true
    
    print "x = " + str(x)
    print "y = " + str(y)
    print "z = " + str(z)
    print "name = " + name
    print "is_valid = " + str(is_valid)
    """
    
    result = evaluate_pseudocode(code)
    print("Result:", json.dumps(result, indent=2))
    print()

def test_control_structures():
    """Test if-else statements and loops."""
    print("=== Testing Control Structures ===")
    
    code = """
    // If-else statement
    x = 15
    y = 10
    
    if x > y then
        print "x is greater than y"
    else
        print "x is less than or equal to y"
    endif
    
    // While loop
    counter = 1
    while counter <= 3 do
        print "Counter: " + str(counter)
        counter = counter + 1
    endwhile
    
    // For loop
    for i = 1 to 3
        print "For loop iteration: " + str(i)
    endfor
    """
    
    result = evaluate_pseudocode(code)
    print("Result:", json.dumps(result, indent=2))
    print()

def test_step_by_step_execution():
    """Test step-by-step execution."""
    print("=== Testing Step-by-Step Execution ===")
    
    code = """
    // Step-by-step execution test
    x = 5
    y = 10
    result = x * y
    print "Result: " + str(result)
    """
    
    result = evaluate_pseudocode(code, step_by_step=True)
    print("Step-by-step result:", json.dumps(result, indent=2))
    print()

def test_syntax_validation():
    """Test syntax validation and error detection."""
    print("=== Testing Syntax Validation ===")
    
    # Valid code
    valid_code = """
    x = 10
    if x > 5 then
        print "Valid code"
    endif
    """
    
    # Invalid code with syntax errors
    invalid_code = """
    x = 10
    if x > 5
        print "Missing 'then' keyword"
    endif
    """
    
    print("Valid code validation:")
    hints = get_syntax_hints(valid_code)
    print("Hints:", json.dumps(hints, indent=2))
    
    print("\nInvalid code validation:")
    hints = get_syntax_hints(invalid_code)
    print("Hints:", json.dumps(hints, indent=2))
    print()

def test_learning_suggestions():
    """Test learning suggestions."""
    print("=== Testing Learning Suggestions ===")
    
    code = """
    // Code with potential improvements
    x = 10
    y = 20
    z = 30
    a = 40
    b = 50
    c = 60
    
    if x > y
        print "x is greater"
    
    while counter < 10
        print "Looping"
    endwhile
    """
    
    suggestions = get_learning_suggestions(code)
    print("Learning suggestions:", json.dumps(suggestions, indent=2))
    print()

def test_advanced_features():
    """Test advanced features like functions and arrays."""
    print("=== Testing Advanced Features ===")
    
    code = """
    // Function definition
    function calculate_sum(a, b)
        result = a + b
        return result
    endfunction
    
    // Using the function
    x = 10
    y = 20
    sum_result = calculate_sum(x, y)
    print "Sum: " + str(sum_result)
    
    // Array operations
    numbers = [1, 2, 3, 4, 5]
    print "Array length: " + str(len(numbers))
    
    // String operations
    message = "Hello, World!"
    print "Message: " + message
    print "Message length: " + str(len(message))
    """
    
    result = evaluate_pseudocode(code)
    print("Advanced features result:", json.dumps(result, indent=2))
    print()

def test_error_handling():
    """Test error handling and recovery."""
    print("=== Testing Error Handling ===")
    
    # Code with runtime error
    error_code = """
    x = 10
    y = 0
    result = x / y  // Division by zero
    print "This won't execute"
    """
    
    result = evaluate_pseudocode(error_code)
    print("Error handling result:", json.dumps(result, indent=2))
    print()

def test_complex_example():
    """Test a complex pseudo-code example."""
    print("=== Testing Complex Example ===")
    
    code = """
    // Complex pseudo-code example: Simple calculator
    function add(a, b)
        return a + b
    endfunction
    
    function subtract(a, b)
        return a - b
    endfunction
    
    function multiply(a, b)
        return a * b
    endfunction
    
    function divide(a, b)
        if b != 0 then
            return a / b
        else
            print "Error: Division by zero"
            return 0
        endif
    endfunction
    
    // Main program
    num1 = 20
    num2 = 5
    
    print "Calculator Demo"
    print "Numbers: " + str(num1) + " and " + str(num2)
    
    sum_result = add(num1, num2)
    print "Addition: " + str(sum_result)
    
    diff_result = subtract(num1, num2)
    print "Subtraction: " + str(diff_result)
    
    product_result = multiply(num1, num2)
    print "Multiplication: " + str(product_result)
    
    quotient_result = divide(num1, num2)
    print "Division: " + str(quotient_result)
    
    // Test division by zero
    zero_result = divide(num1, 0)
    print "Division by zero result: " + str(zero_result)
    """
    
    result = evaluate_pseudocode(code)
    print("Complex example result:", json.dumps(result, indent=2))
    print()

def run_all_tests():
    """Run all test functions."""
    print("🧠 Pseudo-code Parser Test Suite")
    print("=" * 50)
    
    try:
        test_basic_operations()
        test_control_structures()
        test_step_by_step_execution()
        test_syntax_validation()
        test_learning_suggestions()
        test_advanced_features()
        test_error_handling()
        test_complex_example()
        
        print("✅ All tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {str(e)}")

if __name__ == "__main__":
    run_all_tests() 