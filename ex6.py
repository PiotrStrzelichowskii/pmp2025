class MathOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        print(f"Sum: {self.a + self.b}")
    
    def subtract(self):
        print(f"Difference: {self.a - self.b}")

    def __str__(self):
        print(f"Values: {self.a}, {self.b}")

class AdvancedMath(MathOperation):
    def __init__(self, a, b):
        super().__init__(a, b)

    def multiply(self):
        print(f"Multiplication: {self.a * self.b}")
    
    def divide(self):
        if self.b != 0:
            print(f"Division: {self.a / self.b}")
        else:
            print("Division by zero is not allowed")

class Power:
    def power(self, a, b):
        print(f"Power: {a}^{b} = {a ** b}")

class ScientificMath(AdvancedMath, Power):
    def __init__(self, a, b):
        super().__init__(a, b)

    def modulus(self):
        print(f"Modulus: {self.a % self.b}")




op1 = MathOperation(10, 5)
op1.__str__()
op1.add()
op1.subtract()
print()


op2 = AdvancedMath(6, 34)
op2.__str__()
op2.add()
op2.subtract()
op2.multiply()
op2.divide()
print()

op3 = ScientificMath(10, 3)
op3.__str__()
op3.add()
op3.subtract()
op3.multiply()
op3.divide()
op3.modulus()
op3.power(2, 3)
