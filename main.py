
# class Dog:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
  
#   def bark(self):
#     print(f"{self.name} barks")

# sparky = Dog("Sparky", 4)

# sparky.bark()

# # to extend a class: 
# class SmallDog(Dog):
#   def __init__(self, name, age):
#     super().__init__(name, age)
#   def bark(self):
#     print(f"{self.name} yaps")

# MiniSparky = SmallDog("Mini Sparky", 2)

# MiniSparky.bark()



# class Calculator:
#   lastResult = 0

#   # @classmethod
#   def calculate(cls, num1, num2, operator):
#     cls.lastResult = eval(f"{num1} {operator} {num2}")
#     return cls.lastResult

#   # @staticmethod
#   def showLastResult():
#     print(Calculator.lastResult)


# Calculator.calculate(2, 2, "+")
# Calculator.showLastResult()

# numbers

# a = 6
# print(a, "is of type", type(a))

# a = 3.0

# print(a, "is of type", type(a))

# a = 1+2j

# print(a, "is of type", type(a))
# print(a, "is complex number?", isinstance(1+2j, complex))

# strings
s = '''Apple'''
print(s)
# triple quote for multi-line. 