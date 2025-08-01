# 🧠 Pseudo-code Editor Backend

> Advanced pseudo-code parser and evaluator for the VteacH platform

## 🚀 Features

### Core Functionality

- ✅ **Real-time syntax validation** with detailed error messages
- 🪄 **Step-by-step execution** for learning and debugging
- 💡 **Learning suggestions** and improvement hints
- 📘 **Comprehensive pseudo-code support** including:
  - Variable assignments and expressions
  - Control structures (if-else, loops)
  - Functions and procedures
  - String and numeric operations
  - Boolean logic and comparisons
  - Arrays and basic data structures

### Advanced Features

- 🔍 **Syntax highlighting** and tokenization
- 🛡️ **Safe execution environment** with restricted built-ins
- 📊 **Variable tracking** and state visualization
- 🎯 **Error recovery** and graceful failure handling
- 📝 **Comment support** with `//` syntax

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- pip package manager

### Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd PseudoCodeEditor/parser_backend
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**
   ```bash
   python app.py
   ```

The server will start on `http://localhost:5001`

## 📚 API Documentation

### Base URL

```
http://localhost:5001
```

### Endpoints

#### 1. Health Check

```http
GET /
```

**Response:**

```json
{
  "message": "VteacH Pseudo-code Editor Backend is Live!"
}
```

#### 2. Evaluate Pseudo-code

```http
POST /evaluate
```

**Request Body:**

```json
{
  "code": "x = 10\ny = 20\nprint x + y",
  "step_by_step": false
}
```

**Response:**

```json
{
  "status": "success",
  "variables": {
    "x": 10,
    "y": 20
  },
  "output": "30",
  "warnings": []
}
```

#### 3. Step-by-Step Execution

```http
POST /evaluate
```

**Request Body:**

```json
{
  "code": "x = 5\ny = 10\nresult = x * y\nprint result",
  "step_by_step": true
}
```

**Response:**

```json
{
  "status": "success",
  "execution_steps": [
    {
      "line_number": 1,
      "code": "x = 5",
      "variables": { "x": 5 },
      "output": "",
      "error": null
    },
    {
      "line_number": 2,
      "code": "y = 10",
      "variables": { "x": 5, "y": 10 },
      "output": "",
      "error": null
    },
    {
      "line_number": 3,
      "code": "result = x * y",
      "variables": { "x": 5, "y": 10, "result": 50 },
      "output": "",
      "error": null
    },
    {
      "line_number": 4,
      "code": "print result",
      "variables": { "x": 5, "y": 10, "result": 50 },
      "output": "50",
      "error": null
    }
  ],
  "final_variables": {
    "x": 5,
    "y": 10,
    "result": 50
  }
}
```

#### 4. Syntax Validation

```http
POST /validate
```

**Request Body:**

```json
{
  "code": "x = 10\nif x > 5 then\n  print 'Valid'\nendif"
}
```

**Response:**

```json
{
  "status": "success",
  "valid": true,
  "message": "Code syntax is valid"
}
```

#### 5. Syntax Hints

```http
POST /syntax-hints
```

**Request Body:**

```json
{
  "code": "x = 10\nif x > 5\n  print 'Missing then keyword'\nendif"
}
```

**Response:**

```json
{
  "status": "success",
  "hints": [
    {
      "line": 2,
      "type": "warning",
      "message": "Incomplete if statement",
      "suggestion": "Add 'then' or ':' after the condition"
    }
  ]
}
```

#### 6. Learning Suggestions

```http
POST /learning-suggestions
```

**Request Body:**

```json
{
  "code": "x = 10\ny = 20\nif x > y\n  print 'x is greater'\nendif"
}
```

**Response:**

```json
{
  "status": "success",
  "suggestions": [
    "Consider adding an 'else' clause to handle the case when the condition is false"
  ]
}
```

## 📝 Pseudo-code Syntax

### Supported Constructs

#### Variables and Assignments

```pseudocode
x = 10
name = "John"
is_valid = true
result = x + y * 2
```

#### Control Structures

```pseudocode
// If-else statements
if x > y then
    print "x is greater"
else
    print "y is greater or equal"
endif

// While loops
while counter < 10 do
    print counter
    counter = counter + 1
endwhile

// For loops
for i = 1 to 5
    print "Iteration " + str(i)
endfor
```

#### Functions and Procedures

```pseudocode
function add(a, b)
    result = a + b
    return result
endfunction

procedure print_hello()
    print "Hello, World!"
endprocedure
```

#### Comments

```pseudocode
// This is a single-line comment
x = 10  // Inline comment
```

#### String Operations

```pseudocode
message = "Hello"
name = "World"
full_message = message + ", " + name
print full_message
```

#### Arrays and Lists

```pseudocode
numbers = [1, 2, 3, 4, 5]
print "Array length: " + str(len(numbers))
```

## 🧪 Testing

### Run Test Suite

```bash
python test_parser.py
```

### Manual Testing

```bash
# Start the server
python app.py

# In another terminal, test with curl
curl -X POST http://localhost:5001/evaluate \
  -H "Content-Type: application/json" \
  -d '{"code": "x = 10\nprint x"}'
```

## 🔧 Configuration

### Environment Variables

- `PORT`: Server port (default: 5001)
- `DEBUG`: Enable debug mode (default: True)
- `CORS_ORIGINS`: Allowed CORS origins (default: "\*")

### Security Features

- **Restricted execution environment** with limited built-ins
- **Input validation** and sanitization
- **Error isolation** to prevent crashes
- **Resource limits** to prevent infinite loops

## 🚀 Usage Examples

### Basic Example

```python
from parser import evaluate_pseudocode

code = """
x = 10
y = 20
result = x + y
print "Result: " + str(result)
"""

result = evaluate_pseudocode(code)
print(result)
```

### Step-by-Step Execution

```python
from parser import evaluate_pseudocode

code = """
counter = 1
while counter <= 3 do
    print "Step " + str(counter)
    counter = counter + 1
endwhile
"""

result = evaluate_pseudocode(code, step_by_step=True)
for step in result["execution_steps"]:
    print(f"Line {step['line_number']}: {step['code']}")
    print(f"Variables: {step['variables']}")
    if step['output']:
        print(f"Output: {step['output']}")
    print()
```

### Syntax Validation

```python
from parser import get_syntax_hints

code = """
x = 10
if x > 5
    print "Missing then keyword"
endif
"""

hints = get_syntax_hints(code)
for hint in hints:
    print(f"Line {hint['line']}: {hint['message']}")
    print(f"Suggestion: {hint['suggestion']}")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built for the VteacH platform by theGnaN team
- Designed for educational purposes and logic-first learning
- Inspired by the need for better programming education tools

---

**Made with ❤️ by theGnaN team**
