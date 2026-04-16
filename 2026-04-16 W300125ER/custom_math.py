"""_summary_
this is some module's documentation
"""
import math_utils


print(__name__)
print(__file__)
print(__doc__)          # if there is no doc string for the module it will be None
print(__package__)

def multiply(a,b): 
    sum = 0
    for _ in range(b):
        sum = math_utils.add(sum, a)
    return sum

if __name__ == "__main__":
    print(multiply(5,5))