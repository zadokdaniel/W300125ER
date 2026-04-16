# ----------  Pattern 2: Regular Package  ----------
# A directory with __init__.py is a "regular package".
# __init__.py runs when you first import the package.
# Use it to re-export things so users get a clean public API.

from .temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from .distance import km_to_miles, miles_to_km

# __all__ controls what "from converters import *" exports
__all__ = [
    "celsius_to_fahrenheit",
    "fahrenheit_to_celsius",
    "km_to_miles",
    "miles_to_km",
]

print("  [converters/__init__.py executed]")  # proves this runs on import
