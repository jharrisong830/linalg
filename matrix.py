'''
AUTHOR:         @jharrisong830
VERSION:        2.0
DATE:           12/06/22
DESCRIPTION:    Matrix creator and matrix operations calculator
'''

from vector import *

class Matrix:
    '''Creates a matrix according to user input\n
        Matrix(m, n) -> creates an m*n matrix and prompts the user for values of each entry\n
        Matrix(n) -> creates a n*n identity matrix\n
        __Matrix(m, n, operation=True) -> creates an m*n matrix initialized with all entries as 0'''

    def __init__(self, m, n="identity", operation=False):
        '''Creates a matrix according to user input\n
        Matrix(m, n) -> creates an m*n matrix and prompts the user for values of each entry\n
        Matrix(n) -> creates a n*n identity matrix\n
        __Matrix(m, n, operation=True) -> creates an m*n matrix initialized with all entries as 0'''
        if n=="identity":
            self.__A=[]
            self.rows=m
            self.columns=m
            for i in range(self.rows):
                self.__A.append([])
                for j in range(self.columns):
                    if i==j:
                        self.__A[i].append(1)
                    else:
                        self.__A[i].append(0)
            print(str(self.rows)+"*"+str(self.columns)+" identity matrix created!")
        elif type(m)!=int or type(n)!=int:
            raise TypeError
        elif m<=0 or n<=0:
            raise DimensionException
        elif operation:
            self.__A=[]
            self.rows=m
            self.columns=n
            for i in range(self.rows):
                self.__A.append([])
                for j in range(self.columns):
                    self.__A[i].append(0)
        else:
            self.__A=[]
            self.rows=m
            self.columns=n
            for i in range(self.rows):
                self.__A.append([])
                print("ROW "+str(i+1)+":")
                for j in range(self.columns):
                    self.__A[i].append(int(input("Entry "+str(j+1)+": ")))
            print(str(self.rows)+"*"+str(self.columns)+" matrix created!")
        
    def __str__(self):
        max_width=0
        for i in range(self.rows):
            for j in range(self.columns):
                width=len(str(self.__A[i][j]))
                if width>max_width:
                    max_width=width
        result=""
        for i in range(self.rows):
            if i==0:
                result+='\u2308'
            elif i==self.rows-1:
                result+='\u230a'
            else:
                result+="|"
            for j in range(self.columns):
                w=" "*(max_width-len(str(self.__A[i][j])))
                result+=w
                result+=str(self.__A[i][j])
                if not j==self.columns-1:
                    result+=" "
            if i==0:
                result+='\u2309\n'
            elif i==self.rows-1:
                result+='\u230b'
            else:
                result+="|\n"
        return result
    
    def get(self, m, n):
        '''Gets the entry of the matrix at (m, n)'''
        return self.__A[m-1][n-1]
    
    def set(self, m, n, arg):
        '''Sets the entry of the matrix at (m, n) to the value specified by arg'''
        self.__A[m-1][n-1]=arg
    
    def get_vector(self, n):
        '''Returns the vector of column n'''
        return self.__column_vector(n)

    def __row_vector(self, m):
        '''Returns a vector of row m'''
        return Vector(self.__A[m-1])
    
    def __column_vector(self, n):
        '''Returns a vector of column n'''
        result=[]
        for i in range(self.rows):
            result.append(self.get(i+1, n))
        return Vector(result)

    def add(self, B):
        '''Returns a new matrix, which is the result of adding the original matrix with B'''
        if self.rows!=B.rows and self.columns!=B.columns:
            raise DimensionException
        C=Matrix(self.rows, self.columns, operation=True)
        for i in range(self.rows):
            for j in range(self.columns):
                C.set(i, j, self.get(i, j)+B.get(i, j))
        return C
    
    def multiply(self, B):
        '''Returns a new matrix, which is the result of multiplying the original matrix with B'''
        if self.columns!=B.rows:
            raise DimensionException
        C=Matrix(self.rows, B.columns, operation=True)
        for i in range(C.rows):
            for j in range(C.columns):
                row_vec=self.__row_vector(i+1)
                col_vec=B.__column_vector(j+1)
                prod=row_vec.dot_product(col_vec)
                C.set(i+1, j+1, prod)
        return C
    
    def transpose(self):
        '''Transposes a matrix'''
        T=[]
        m=self.columns
        n=self.rows
        for i in range(self.columns):
            T.append([])
            for j in range(self.rows):
                T[i].append(self.get(j+1, i+1))
        self.rows=m
        self.columns=n
        self.__A=T
    
    def gauss(self):
        '''Performs standard Gauss Elimination on a given matrix'''
        for i in range(self.rows):
            for j in range(i, self.columns):
                if i==self.rows-1:
                    break
                elif self.get(i+1, j+1)==0:
                    continue
                for k in range(i, self.rows-1):
                    coeff=-(self.get(k+2, j+1))/self.get(i+1, j+1)
                    for l in range(j, self.columns):
                        self.set(k+2, l+1, self.get(k+2, l+1)+(coeff*self.get(i+1, l+1)))
                break