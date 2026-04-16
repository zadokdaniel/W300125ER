# ----------  Pattern 3: Namespace Package  ----------
# This directory has NO __init__.py — it's a "namespace package".
# You can still import sub-modules, but you CANNOT import the
# package itself to get attributes (there's no __init__.py to define them).

import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"
    return bool(re.match(pattern, email))
