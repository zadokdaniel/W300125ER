# ----------  Pattern 1: Simple Module  ----------
# A single .py file IS a module. Any file can be imported by name.

PI = 3.14159

def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# _private by convention — not exported by "from helpers import *"
def _secret():
    return "you found me"


