


def main(x1,x2,x3):
    """
    Given three integers, x1, x2, and x3, return the "[x1, x2, x3]" string.
    Args:
        x1: int
        x2: int
        x3: int
    Returns:
        str: return answer.
    """
    a=str(x1)
    b=str(x2)
    c=str(x3)
    return '[' + a + ', ' + b + ', ' + c + ']'
print(main(1,2,3)) 
   