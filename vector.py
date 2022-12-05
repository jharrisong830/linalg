'''
AUTHOR:         @jharrisong830
VERSION:        1.0
DATE:           12/05/22
DESCRIPTION:    Vector class
'''

import math

class DimensionException(Exception):
    def __init__(self, message="Invalid dimensions for this operation"):
        super().__init__(message)

class Vector:

    def __init__(self, L):
        if type(L)!=list:
            raise TypeError
        self.__vec=L
        self.dimension=len(self.__vec)

    def __str__(self):
        result="<"
        for i in range(len(self.__vec)):
            result+=str(self.__vec[i])
            if i==len(self.__vec)-1:
                result+=">"
            else:
                result+=" "
        return result
    
    def length(self):
        '''Returns the vector length'''
        sum_of_squares=0
        for i in range(self.dimension):
            sum_of_squares+=self.get(i+1)**2
        return math.sqrt(sum_of_squares)

    def get(self, n):
        return self.__vec[n-1]
    
    def set(self, n, arg):
        self.__vec[n-1]=arg
    
    def push_back(self, arg):
        '''adds an argument to the end of a vector'''
        self.__vec.append(arg)
        self.dimension+=1
    
    def pop_back(self):
        '''removes an element from the end of a vector, and returns that value'''
        pop=self.get(0)
        self.__vec=self.__vec[:-1]
        self.dimension-=1
        return pop
    
    def dot_product(self, v):
        '''Returns the dot product of the original vector and v'''
        prod=0
        for i in range(self.dimension):
            prod+=(self.get(i+1)*v.get(i+1))
        return prod