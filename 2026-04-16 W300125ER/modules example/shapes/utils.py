# shapes/utils.py  — internal helper, not re-exported by __init__.py

import math

PI = math.pi

def _describe(name, **measurements):
    """Format a shape description. Underscore prefix = private by convention."""
    parts = ", ".join(f"{k}={v}" for k, v in measurements.items())
    return f"{name}({parts})"
