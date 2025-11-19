print("=== SyntaxError Examples ===")

# Note: Most SyntaxError examples cannot be in the same file as they would prevent
# the script from running. These examples show how to catch SyntaxError when
# using exec(), eval(), compile(), and other dynamic code execution.

# 1. SyntaxError with exec()
print("1. SyntaxError with exec():")

# Missing closing parenthesis
try:
    exec("print('Hello World'")  # Missing closing parenthesis
except SyntaxError as e:
    print(f"Exec syntax error: {e}")
    print(f"Error at line {e.lineno}, position {e.offset}")
    print(f"Problematic text: {repr(e.text)}")

# Missing colon in if statement
try:
    exec("if True\n    print('Missing colon')")
except SyntaxError as e:
    print(f"If statement error: {e}")
    print(f"Error details: line {e.lineno}, pos {e.offset}")

# Invalid indentation
try:
    exec("def my_function():\nprint('Bad indentation')")
except SyntaxError as e:
    print(f"Indentation error: {e}")

# 2. SyntaxError with eval()
print("\n2. SyntaxError with eval():")

# Invalid expression syntax
try:
    result = eval("2 + * 3")  # Invalid operator placement
except SyntaxError as e:
    print(f"Eval syntax error: {e}")

# Invalid comparison
try:
    result = eval("5 < < 3")  # Invalid comparison syntax
except SyntaxError as e:
    print(f"Comparison error: {e}")

# Statement in eval (eval only accepts expressions)
try:
    result = eval("print('Hello')")  # print is a statement, not expression
except SyntaxError as e:
    print(f"Statement in eval: {e}")

# 3. SyntaxError with compile()
print("\n3. SyntaxError with compile():")

# Invalid function definition
try:
    code = compile("def (invalid):\n    pass", "<string>", "exec")
except SyntaxError as e:
    print(f"Function definition error: {e}")
    print(f"Filename: {e.filename}")

# Unmatched brackets
try:
    code = compile("my_list = [1, 2, 3", "<string>", "exec")
except SyntaxError as e:
    print(f"Bracket error: {e}")

# Invalid for loop
try:
    code = compile("for x in:\n    print(x)", "<string>", "exec")
except SyntaxError as e:
    print(f"For loop error: {e}")

# 4. Common SyntaxError patterns
print("\n4. Common SyntaxError patterns:")

def demonstrate_syntax_errors():
    """Demonstrate common syntax error patterns"""
    
    syntax_examples = [
        ("Missing quotes", "print(Hello World)"),
        ("Unmatched parentheses", "print('test'"),
        ("Invalid variable name", "2variable = 5"),
        ("Missing colon", "if x == 5\n    print('five')"),
        ("Invalid assignment", "5 = x"),
        ("Reserved keyword as variable", "def = 'function'"),
        ("Invalid string", "'unterminated string"),
        ("Wrong indentation", "def func():\nprint('bad indent')"),
    ]
    
    for description, code in syntax_examples:
        try:
            compile(code, "<string>", "exec")
            print(f"{description}: No error (unexpected)")
        except SyntaxError as e:
            print(f"{description}: {e}")

demonstrate_syntax_errors()

# 5. SyntaxError in dynamic code generation
print("\n5. SyntaxError in dynamic code generation:")

def generate_and_execute_code(template, **kwargs):
    """Generate code from template and execute it safely"""
    try:
        # Generate code from template
        code = template.format(**kwargs)
        print(f"Generated code: {repr(code)}")
        
        # Compile first to catch syntax errors
        compiled_code = compile(code, "<generated>", "exec")
        
        # Execute if compilation successful
        exec(compiled_code)
        print("Code executed successfully")
        
    except SyntaxError as e:
        print(f"Syntax error in generated code: {e}")
        print(f"Generated code was: {repr(code)}")
    except Exception as e:
        print(f"Runtime error: {e}")

# Test code generation
templates = [
    ("print('Hello {name}')", {"name": "World"}),
    ("if {condition}:\n    print('True')", {"condition": "True"}),
    ("if {condition}    print('Missing colon')", {"condition": "True"}),  # Missing colon
    ("def {func_name}():\n    return {value}", {"func_name": "test_func", "value": "42"}),
    ("def {func_name}():\nreturn {value}", {"func_name": "bad_func", "value": "42"}),  # Bad indent
]

for template, kwargs in templates:
    print(f"\nTesting template: {repr(template)}")
    generate_and_execute_code(template, **kwargs)

# 6. SyntaxError in configuration files
print("\n6. SyntaxError in configuration files:")

def parse_python_config(config_string):
    """Parse Python-syntax configuration with error handling"""
    try:
        # Create a safe namespace for config
        config_namespace = {}
        
        # Compile and execute configuration
        compiled_config = compile(config_string, "<config>", "exec")
        exec(compiled_config, {"__builtins__": {}}, config_namespace)
        
        # Remove built-ins from result
        return {k: v for k, v in config_namespace.items() if not k.startswith('__')}
        
    except SyntaxError as e:
        print(f"Config syntax error: {e}")
        print(f"Line {e.lineno}: {e.text}")
        return None

# Test configuration parsing
config_examples = [
    # Valid config
    """
DATABASE_HOST = 'localhost'
DATABASE_PORT = 5432
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
""",
    # Invalid config - missing quotes
    """
DATABASE_HOST = localhost
DATABASE_PORT = 5432
""",
    # Invalid config - syntax error
    """
DATABASE_HOST = 'localhost'
DATABASE_PORT = 
DEBUG = True
"""
]

for i, config in enumerate(config_examples, 1):
    print(f"\nTesting config {i}:")
    result = parse_python_config(config.strip())
    if result:
        print(f"Parsed config: {result}")

# 7. SyntaxError with AST parsing
print("\n7. SyntaxError with AST parsing:")

import ast

def analyze_python_code(code_string):
    """Analyze Python code using AST"""
    try:
        # Parse code into AST
        tree = ast.parse(code_string)
        
        # Analyze AST
        functions = []
        variables = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        variables.append(target.id)
        
        return {
            "valid": True,
            "functions": functions,
            "variables": variables
        }
        
    except SyntaxError as e:
        return {
            "valid": False,
            "error": str(e),
            "line": e.lineno,
            "offset": e.offset
        }

# Test AST analysis
code_examples = [
    "def hello():\n    x = 5\n    return x",
    "def hello(\n    return 'missing colon'",  # Syntax error
    "x = 5\ny = 10\ndef add():\n    return x + y",
]

for code in code_examples:
    print(f"\nAnalyzing: {repr(code)}")
    result = analyze_python_code(code)
    print(f"Result: {result}")

# 8. Custom SyntaxError for DSL
print("\n8. Custom SyntaxError for Domain Specific Language:")

class DSLSyntaxError(SyntaxError):
    """Custom syntax error for domain-specific language"""
    def __init__(self, message, line_number=None, position=None, line_text=None):
        super().__init__(message)
        self.lineno = line_number
        self.offset = position
        self.text = line_text

def parse_simple_dsl(dsl_code):
    """Parse a simple DSL with custom syntax errors"""
    lines = dsl_code.strip().split('\n')
    
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        try:
            # Simple DSL: COMMAND argument
            if ' ' not in line:
                raise DSLSyntaxError(
                    f"Missing argument for command",
                    line_num, 1, line
                )
            
            command, argument = line.split(' ', 1)
            
            if command not in ['SET', 'GET', 'PRINT']:
                raise DSLSyntaxError(
                    f"Unknown command '{command}'. Valid commands: SET, GET, PRINT",
                    line_num, 1, line
                )
            
            if command == 'SET' and '=' not in argument:
                raise DSLSyntaxError(
                    f"SET command requires '=' syntax: SET variable = value",
                    line_num, len(command) + 2, line
                )
            
            print(f"Valid DSL line: {command} {argument}")
            
        except DSLSyntaxError as e:
            print(f"DSL Syntax Error at line {e.lineno}: {e}")
            if e.text:
                print(f"  {e.text}")
                if e.offset:
                    print(f"  {' ' * (e.offset - 1)}^")

# Test DSL parsing
dsl_examples = [
    """
    SET x = 5
    GET x
    PRINT Hello World
    """,
    """
    SET x = 5
    UNKNOWN_COMMAND test
    PRINT Hello
    """,
    """
    SET x 5
    GET x
    """
]

for i, dsl in enumerate(dsl_examples, 1):
    print(f"\nParsing DSL example {i}:")
    parse_simple_dsl(dsl)

# 9. SyntaxError prevention and validation
print("\n9. SyntaxError prevention and validation:")

def safe_code_validator(code):
    """Validate Python code before execution"""
    validation_result = {
        "valid": False,
        "errors": [],
        "warnings": []
    }
    
    try:
        # Check for basic syntax
        ast.parse(code)
        validation_result["valid"] = True
        
        # Additional checks
        if "exec" in code or "eval" in code:
            validation_result["warnings"].append("Contains dynamic execution")
        
        if "import os" in code or "import sys" in code:
            validation_result["warnings"].append("Contains system imports")
        
    except SyntaxError as e:
        validation_result["errors"].append({
            "type": "SyntaxError",
            "message": str(e),
            "line": e.lineno,
            "offset": e.offset,
            "text": e.text
        })
    
    return validation_result

# Test code validation
test_codes = [
    "print('Hello World')",
    "print('Hello World'",  # Missing parenthesis
    "import os\nprint('System access')",
    "exec('print(\"Dynamic\")')",
]

for code in test_codes:
    print(f"\nValidating: {repr(code)}")
    result = safe_code_validator(code)
    print(f"Valid: {result['valid']}")
    if result['errors']:
        print(f"Errors: {result['errors']}")
    if result['warnings']:
        print(f"Warnings: {result['warnings']}")

print("\n=== SyntaxError examples completed ===")