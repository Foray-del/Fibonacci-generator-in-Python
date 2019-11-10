def fibonacci():
    """ Generator yielding Fibonacci numbers
    
    :returns: int -- Fibonacci number as an integer
    """
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y
        @@ -1,5 +1,8 @@
def fibonacci():
    """ Generator yielding Fibonacci numbers """
    """ Generator yielding Fibonacci numbers
    
    :returns: int -- Fibonacci number as an integer
    """
    a, b = 0, 1
    while True:
        yield a
        @@ -0,0 +1,6 @@
def fibonacci():
    """ Generator yielding Fibonacci numbers """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
