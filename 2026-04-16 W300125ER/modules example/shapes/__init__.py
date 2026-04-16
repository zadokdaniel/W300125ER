# ----------  Pattern 4: Package with __all__ and relative imports  ----------
# __all__ defines exactly what "from shapes import *" will export.
# Anything NOT in __all__ stays hidden from star-imports (but can
# still be imported explicitly: from shapes.utils import _describe).

from .circle import Circle
from .rectangle import Rectangle

__all__ = ["Circle", "Rectangle"]  # utils is intentionally excluded
