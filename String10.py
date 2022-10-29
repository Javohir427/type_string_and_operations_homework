def main(x,y):
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    
    return (str('(')+str(x)+str('+')+str(y))+str(')')+str('*')+str('2')+str('=')+str((x+y)*2)

print (main(4,6))