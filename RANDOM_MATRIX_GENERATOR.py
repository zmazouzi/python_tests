

## RANDOM MATRIX OF NUMBERS FROM 0 TO 9 


# class Reverse:
#     def __init__(self,data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if(self.index == 0):
#             raise StopIteration
#         self.index = self.index -1
#         return self.data[self.index]
#
#
# rev = Reverse('hello')
# for char in rev:
#     print(char)
#
import random

class Matrix:
    def __init__(self,height):
        self.height = height
        self.matrix = [ [ random.randrange(0,10) for i in range(self.height)] for i in range(self.height)]
        print(self)
        for i in range(self.height):
            for j in range(self.height):
                print("  ",str(self.matrix[i][j]),"  ",end=' ')
            print("\n")
    def produit_element(self,other1,other2):
        sum = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                sum+=other1.matrix[]

matrice = Matrix(5)
























