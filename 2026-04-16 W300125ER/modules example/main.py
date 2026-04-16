"""
Python Modules & Packages — Learning Guide
============================================
Run this file:  python main.py

Project structure:
    main.py                  ← you are here
    helpers.py               ← Pattern 1: simple module (single file)
    converters/              ← Pattern 2: regular package (__init__.py)
        __init__.py
        temperature.py
        distance.py
    validators/              ← Pattern 3: namespace package (NO __init__.py)
        email_validator.py
        number_validator.py
    shapes/                  ← Pattern 4: __all__, relative imports, re-exports
        __init__.py
        circle.py
        rectangle.py
        utils.py             ← internal helper, not re-exported
"""

# ============================================================
# PATTERN 1 — Simple Module (helpers.py)
# ============================================================
print("=" * 60)
print("PATTERN 1: Simple Module")
print("=" * 60)

# 1a. import the whole module — access via module.name
import helpers

print(f"helpers.PI        = {helpers.PI}")
print(f"helpers.greet('Daniel') = {helpers.greet('Daniel')}")
print(f"helpers.add(2, 3) = {helpers.add(2, 3)}")

# 1b. import specific names into local namespace
from helpers import greet, PI 

print(f"greet('World')    = {greet('World')}")  # no prefix needed
print(f"PI                = {PI}")

# 1c. import with alias
from helpers import add as plus

print(f"plus(10, 20)      = {plus(10, 20)}")

# 1d. "_private" by convention — still accessible, just discouraged
print(f"helpers._secret() = {helpers._secret()}")

print()

# ============================================================
# PATTERN 2 — Regular Package (converters/)
# ============================================================
print("=" * 60)
print("PATTERN 2: Regular Package (has __init__.py)")
print("=" * 60)

# 2a. import the package — __init__.py runs and re-exports functions
import converters

print(f"converters.celsius_to_fahrenheit(100) = {converters.celsius_to_fahrenheit(100)}")
print(f"converters.km_to_miles(10)            = {converters.km_to_miles(10):.2f}")

# 2b. import a specific sub-module directly
from converters.temperature import fahrenheit_to_celsius

print(f"fahrenheit_to_celsius(212) = {fahrenheit_to_celsius(212)}")

# 2c. import from package (works because __init__.py re-exports)
from converters import miles_to_km

print(f"miles_to_km(5) = {miles_to_km(5):.2f}")

print()

# ============================================================
# PATTERN 3 — Namespace Package (validators/ — NO __init__.py)
# ============================================================
print("=" * 60)
print("PATTERN 3: Namespace Package (no __init__.py)")
print("=" * 60)

# 3a. You MUST import the sub-module explicitly
from validators.email_validator import is_valid_email
from validators.number_validator import is_positive, is_even

print(f"is_valid_email('a@b.com')  = {is_valid_email('a@b.com')}")
print(f"is_valid_email('invalid')  = {is_valid_email('invalid')}")
print(f"is_positive(5)             = {is_positive(5)}")
print(f"is_even(4)                 = {is_even(4)}")

# 3b. Importing just "validators" gives an empty namespace — nothing is defined
import validators

print(f"dir(validators) has sub-modules? = {bool(set(dir(validators)) & {'is_valid_email', 'is_positive'})}")
print("  ^ False! Without __init__.py there are no re-exports.")

print()

# ============================================================
# PATTERN 4 — __all__, Relative Imports, Re-exports (shapes/)
# ============================================================
print("=" * 60)
print("PATTERN 4: __all__ and Relative Imports (shapes/)")
print("=" * 60)

# 4a. import from package — gets re-exported classes
from shapes import Circle, Rectangle

c = Circle(5)
r = Rectangle(3, 4)
print(f"Circle(5)         = {c},  area = {c.area():.2f}")
print(f"Rectangle(3, 4)   = {r},  area = {r.area()}")

# 4b. utils is NOT in __all__, so "from shapes import *" won't include it,
#     but you can still import it explicitly:
from shapes.utils import _describe

print(f"_describe('Test', x=1) = {_describe('Test', x=1)}")

# 4c. Demonstrate that "from shapes import *" only gives __all__ items
from shapes import *  # noqa: F403

# Circle and Rectangle are available, but _describe and utils are not
print(f"'Circle' available after import *?    = {'Circle' in dir()}")
print(f"'_describe' available after import *? = {'_describe' in dir()}")
print("  ^ _describe was only available because we imported it explicitly above.")

print()

# ============================================================
# BONUS — Inspecting module metadata
# ============================================================
print("=" * 60)
print("BONUS: Module Inspection")
print("=" * 60)

print(f"helpers.__name__   = {helpers.__name__}")
print(f"helpers.__file__   = {helpers.__file__}")
print(f"converters.__path__ = {converters.__path__}")
print(f"converters.__all__  = {converters.__all__}")

# __name__ == '__main__' only for the script you run directly
print(f"this file __name__ = {__name__}")

print()
print("Done! Read the source code + comments for the full explanation.")
