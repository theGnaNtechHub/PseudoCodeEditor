# Complete corrected parser.py with proper indentation handling
"""
Advanced Pseudo-code Parser and Evaluator for VteacH Platform - FIXED VERSION

Supports:
- Variable assignments and expressions
- Control structures (if-else, loops)
- Functions and procedures with proper parameter handling
- String and numeric operations
- Boolean logic
- Arrays and basic data structures
- Syntax validation and error detection
- Learning hints and suggestions
"""

import sys
import io
import re
import ast
import json
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    KEYWORD = "keyword"
    IDENTIFIER = "identifier"
    NUMBER = "number"
    STRING = "string"
    OPERATOR = "operator"
    DELIMITER = "delimiter"
    COMMENT = "comment"



@dataclass
class ParserError:
    line: int
    message: str
    suggestion: str = ""
    severity: str = "error"  # error, warning, info

class PseudoCodeParser:
    def __init__(self):
        self.keywords = {
            'if', 'else', 'endif', 'while', 'endwhile', 'for', 'endfor',
            'function', 'endfunction', 'procedure', 'endprocedure',
            'return', 'print', 'input', 'true', 'false', 'null'
        }
        self.operators = {
            '+', '-', '*', '/', '//', '%', '**', '==', '!=', '<=', '>=', '<', '>',
            'and', 'or', 'not', '=', '+=', '-=', '*=', '/='
        }
        self.delimiters = {',', ';', '(', ')', '[', ']', '{', '}'}
        
    def tokenize(self, code: str) -> List[Tuple[str, TokenType, int]]:
        """Tokenize the pseudo-code into tokens with line numbers."""
        tokens = []
        lines = code.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # Skip empty lines
            if not line.strip():
                continue
                
            # Handle comments
            if line.strip().startswith('//'):
                tokens.append((line.strip(), TokenType.COMMENT, line_num))
                continue
                
            # Split line into tokens
            current_token = ""
            in_string = False
            string_delimiter = None
            
            for char in line:
                if char in ['"', "'"] and not in_string:
                    in_string = True
                    string_delimiter = char
                    if current_token:
                        tokens.extend(self._process_token(current_token, line_num))
                        current_token = ""
                    current_token = char
                elif char == string_delimiter and in_string:
                    in_string = False
                    current_token += char
                    tokens.append((current_token, TokenType.STRING, line_num))
                    current_token = ""
                    string_delimiter = None
                elif in_string:
                    current_token += char
                elif char.isspace():
                    if current_token:
                        tokens.extend(self._process_token(current_token, line_num))
                        current_token = ""
                elif char in self.delimiters or char in self.operators:
                    if current_token:
                        tokens.extend(self._process_token(current_token, line_num))
                        current_token = ""
                    tokens.append((char, TokenType.DELIMITER if char in self.delimiters else TokenType.OPERATOR, line_num))
                else:
                    current_token += char
                    
            if current_token:
                tokens.extend(self._process_token(current_token, line_num))
                
        return tokens
    
    def _process_token(self, token: str, line_num: int) -> List[Tuple[str, TokenType, int]]:
        """Process a single token and determine its type."""
        if not token:
            return []
            
        # Check if it's a keyword
        if token.lower() in self.keywords:
            return [(token, TokenType.KEYWORD, line_num)]
            
        # Check if it's a number
        if token.replace('.', '').replace('-', '').isdigit() or token.replace('.', '').replace('-', '').replace('e', '').replace('E', '').isdigit():
            return [(token, TokenType.NUMBER, line_num)]
            
        # Check if it's an operator
        if token in self.operators:
            return [(token, TokenType.OPERATOR, line_num)]
            
        # Must be an identifier
        return [(token, TokenType.IDENTIFIER, line_num)]
    
    def validate_syntax(self, code: str) -> List[ParserError]:
        """Validate pseudo-code syntax and return errors/warnings."""
        errors = []
        lines = code.split('\n')
        
        # Check for basic syntax issues
        for line_num, line in enumerate(lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith('//'):
                continue
                
            # Check for unmatched delimiters
            if stripped.count('(') != stripped.count(')'):
                errors.append(ParserError(
                    line_num, 
                    "Unmatched parentheses",
                    "Make sure all opening parentheses have matching closing parentheses",
                    "error"
                ))
                
            if stripped.count('[') != stripped.count(']'):
                errors.append(ParserError(
                    line_num, 
                    "Unmatched brackets",
                    "Make sure all opening brackets have matching closing brackets",
                    "error"
                ))
                
            # Check for common pseudo-code patterns
            if stripped.startswith('if ') and not any(keyword in stripped for keyword in ['then', ':', '{']):
                errors.append(ParserError(
                    line_num,
                    "Incomplete if statement",
                    "Add 'then' or ':' after the condition",
                    "warning"
                ))
                
            if stripped.startswith('while ') and not any(keyword in stripped for keyword in ['do', ':', '{']):
                errors.append(ParserError(
                    line_num,
                    "Incomplete while statement",
                    "Add 'do' or ':' after the condition",
                    "warning"
                ))
                
        return errors
    
    def preprocess_code(self, code: str) -> str:
        """Convert pseudo-code to valid Python code with proper indentation."""
        lines = code.split('\n')
        processed_lines = []
        
        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith('//'):
                continue
                
            # Calculate original indentation
            original_indent = len(line) - len(line.lstrip())
            indent_level = original_indent // 4
            
            # Convert the line
            processed_line = self._convert_pseudo_to_python(stripped)
            
            if not processed_line:
                continue
                
            # Determine final indentation
            if processed_line.startswith('def '):
                # Function definition - use original indentation
                final_indent = indent_level
            elif processed_line.startswith(('if ', 'elif ', 'else:', 'while ', 'for ')):
                # Control structure - use original indentation
                final_indent = indent_level
            elif stripped.startswith('end'):
                # End statement - reduce indentation
                final_indent = max(0, indent_level - 1)
            else:
                # Regular line - add one level if we have indentation
                if indent_level > 0:
                    final_indent = indent_level + 1
                else:
                    final_indent = indent_level
            
            # Add the line with proper indentation
            indent = "    " * final_indent
            processed_lines.append(indent + processed_line)
            
        return "\n".join(processed_lines)
    
    def _convert_pseudo_to_python(self, line: str) -> str:
        """Convert a single line of pseudo-code to Python."""
        # Handle print statements
        if line.startswith('print '):
            expr = line[6:].strip()
            return f"print({expr})"
            
        # Handle input statements
        if line.startswith('input '):
            var_name = line[6:].strip()
            return f"{var_name} = input()"
            
        # Handle if statements
        if line.startswith('if ') and 'then' in line:
            condition = line[3:line.find('then')].strip()
            return f"if {condition}:"
            
        # Handle else if statements
        if line.startswith('else if ') and 'then' in line:
            condition = line[8:line.find('then')].strip()
            return f"elif {condition}:"
            
        # Handle else statements
        if line.startswith('else'):
            return "else:"
            
        # Handle while statements
        if line.startswith('while ') and 'do' in line:
            condition = line[6:line.find('do')].strip()
            return f"while {condition}:"
            
        # Handle for loops
        if line.startswith('for '):
            # Simple for loop conversion
            parts = line[4:].split(' to ')
            if len(parts) == 2:
                var = parts[0].strip()
                end = parts[1].strip()
                return f"for {var} in range({end}):"
                
        # Handle function definitions
        if line.startswith('function '):
            # Extract function name and parameters
            func_part = line[9:].strip()  # Remove 'function '
            if '(' in func_part and ')' in func_part:
                func_name = func_part[:func_part.find('(')].strip()
                params_part = func_part[func_part.find('(')+1:func_part.find(')')].strip()
                return f"def {func_name}({params_part}):"
            else:
                # Fallback for function without parameters
                func_name = func_part.strip()
                return f"def {func_name}():"
            
        # Handle procedure definitions
        if line.startswith('procedure '):
            # Extract procedure name and parameters
            proc_part = line[10:].strip()  # Remove 'procedure '
            if '(' in proc_part and ')' in proc_part:
                proc_name = proc_part[:proc_part.find('(')].strip()
                params_part = proc_part[proc_part.find('(')+1:proc_part.find(')')].strip()
                return f"def {proc_name}({params_part}):"
            else:
                # Fallback for procedure without parameters
                proc_name = proc_part.strip()
                return f"def {proc_name}():"
            
        # Handle end statements
        if line.startswith('end'):
            return ""
            
        # Handle boolean values
        if line == 'true':
            return 'True'
        elif line == 'false':
            return 'False'
            
        # Handle return statements
        if line.startswith('return '):
            return line
            
        return line

class PseudoCodeEvaluator:
    def __init__(self):
        self.parser = PseudoCodeParser()
        self.variables = {}
        self.output_buffer = io.StringIO()
        
    def _filter_serializable_variables(self, variables: Dict[str, Any]) -> Dict[str, Any]:
        """Filter variables to only include JSON serializable objects."""
        serializable_vars = {}
        for key, value in variables.items():
            if key.startswith('__'):
                continue
            try:
                # Test if the value is JSON serializable
                json.dumps(value)
                serializable_vars[key] = value
            except (TypeError, ValueError):
                # Skip non-serializable objects like functions
                continue
        return serializable_vars
        
    def evaluate(self, code: str) -> Dict[str, Any]:
        """Evaluate pseudo-code and return results."""
        try:
            # Validate syntax first
            syntax_errors = self.parser.validate_syntax(code)
            if any(error.severity == "error" for error in syntax_errors):
                return {
                    "status": "error",
                    "message": "Syntax errors found",
                    "errors": [{"line": e.line, "message": e.message, "suggestion": e.suggestion} for e in syntax_errors]
                }
            
            # Preprocess code
            processed_code = self.parser.preprocess_code(code)
            
            # Execute code
            return self._execute_normal(processed_code)
                
        except Exception as e:
            return {
                "status": "error",
                "message": f"Execution error: {str(e)}",
                "suggestion": "Check your code for syntax errors or logical issues"
            }
    
    def _execute_normal(self, code: str) -> Dict[str, Any]:
        """Execute code normally and return results."""
        # Redirect stdout to capture prints
        original_stdout = sys.stdout
        sys.stdout = self.output_buffer
        
        try:
            # Create execution environment
            exec_globals = {
                '__builtins__': {
                    'print': print,
                    'input': input,
                    'len': len,
                    'range': range,
                    'str': str,
                    'int': int,
                    'float': float,
                    'bool': bool,
                    'list': list,
                    'dict': dict,
                    'True': True,
                    'False': False,
                    'None': None
                }
            }
            
            # Execute the code
            exec(code, exec_globals, self.variables)
            
            # Get output
            output = self.output_buffer.getvalue().strip()
            
            return {
                "status": "success",
                "variables": self._filter_serializable_variables(self.variables),
                "output": output,
                "warnings": [{"line": e.line, "message": e.message} for e in self.parser.validate_syntax(code) if e.severity == "warning"]
            }
            
        finally:
            sys.stdout = original_stdout
            self.output_buffer.truncate(0)
            self.output_buffer.seek(0)
    


def evaluate_pseudocode(code: str) -> Dict[str, Any]:
    """
    Main function to evaluate pseudo-code.
    
    Args:
        code: The pseudo-code to evaluate
        
    Returns:
        Dictionary with evaluation results
    """
    evaluator = PseudoCodeEvaluator()
    return evaluator.evaluate(code)

def get_syntax_hints(code: str) -> List[Dict[str, str]]:
    """Get syntax hints and suggestions for the given code."""
    parser = PseudoCodeParser()
    errors = parser.validate_syntax(code)
    
    hints = []
    for error in errors:
        hints.append({
            "line": error.line,
            "type": error.severity,
            "message": error.message,
            "suggestion": error.suggestion
        })
    
    return hints

def get_learning_suggestions(code: str) -> List[str]:
    """Get learning suggestions based on the code content."""
    suggestions = []
    
    if 'if' in code.lower() and 'else' not in code.lower():
        suggestions.append("Consider adding an 'else' clause to handle the case when the condition is false")
    
    if 'while' in code.lower() and 'break' not in code.lower():
        suggestions.append("Make sure your while loop has a proper termination condition to avoid infinite loops")
    
    if 'print' in code.lower() and 'input' not in code.lower():
        suggestions.append("Consider adding user input to make your program interactive")
    
    if code.count('=') > 5:
        suggestions.append("Consider using more descriptive variable names to improve code readability")
    
    return suggestions

# Example usage and testing
if __name__ == "__main__":
    # Test the parser with sample pseudo-code
    sample_code = """
    // Simple pseudo-code example
    x = 10
    y = 20
    if x < y then
        print "x is less than y"
    else
        print "x is greater than or equal to y"
    endif
    """
    
    result = evaluate_pseudocode(sample_code)
    print("Evaluation Result:", json.dumps(result, indent=2))