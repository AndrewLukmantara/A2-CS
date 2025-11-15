# Method Overloading

# class Overload():

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def add(self, a,b):
#         return self.a + self.b
    
#     def add(self, a,b,c): 
#         return self.a + self.b + self.c
    

# test = Overload(1,2)
# print(test.add(1,2)) # Python does not support method overloading. It only calls the last method which is defined
# print(test.add(1,2))


def add(a, b, c = 0):
    return a + b + c

print(add(1,2))