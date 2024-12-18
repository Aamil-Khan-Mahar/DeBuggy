# filename: Code1Buggy.py

class Math:
    def __init__(self):
        pass

    def add(self, a, b):
        # Fixed the bug here by changing the operator from - to +
        return a + b

    def subtract(self, a, b):
        # Fixed the bug here by changing the operator from * to -
        return a - b

    # Fixed the bug here by changing the parameter from aa to a 
    # and adding self to the method definition
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        # Fixed the bug by removing extra characters in b variable
        return a / b

    def power(self, a, b):
        # Fixed logic error by ensuring the method only returns the power of a raised to b
        return a ** b


def test():
    math = Math()
    print(math.add(2, 3))        # Expected output: 5
    print(math.subtract(2, 3))   # Expected output: -1
    print(math.multiply(2, 3))   # Expected output: 6
    print(math.divide(2, 3))     # Expected output: 0.666...
    print(math.power(2, 3))      # Expected output: 8

random_number = 5
random_code = 'random_code'
