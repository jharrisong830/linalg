'''
AUTHOR:         @jharrisong830
VERSION:        3.3
DATE:           12/10/22
DESCRIPTION:    Matrix creator and matrix operations calculator
'''

import vector

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
        elif type(m)!=int or type(n)!=int:
            raise TypeError
        elif m<=0 or n<=0:
            raise vector.DimensionException
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
                    self.__A[i].append(float(input("Entry "+str(j+1)+": ")))
            print(str(self.rows)+"*"+str(self.columns)+" matrix created!")
        
    def __str__(self):
        max_width=0
        for i in range(self.rows):
            for j in range(self.columns):
                width=len(str(round(self.get(i+1, j+1), 3)))
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
                w=" "*(max_width-len(str(round(self.get(i+1, j+1), 3))))
                result+=w
                result+=str(round(self.get(i+1, j+1), 3))
                if not j==self.columns-1:
                    result+=" "
            if i==0:
                result+='\u2309\n'
            elif i==self.rows-1:
                result+='\u230b'
            else:
                result+="|\n"
        return result
    
    def __add__(self, B):
        '''Returns a new matrix, which is the result of adding the original matrix with B'''
        if self.rows!=B.rows and self.columns!=B.columns:
            raise vector.DimensionException
        C=Matrix(self.rows, self.columns, operation=True)
        for i in range(self.rows):
            for j in range(self.columns):
                C.set(i, j, self.get(i, j)+B.get(i, j))
        return C
    
    def __mul__(self, B):
        '''Returns a new matrix, which is the result of multiplying the original matrix with B'''
        if self.columns!=B.rows:
            raise vector.DimensionException
        C=Matrix(self.rows, B.columns, operation=True)
        for i in range(C.rows):
            for j in range(C.columns):
                row_vec=self.__row_vector(i+1)
                col_vec=B.__column_vector(j+1)
                prod=row_vec.dot_product(col_vec)
                C.set(i+1, j+1, prod)
        return C
    
    def copy(self):
        '''Returns a copy of a matrix object'''
        copy=Matrix(self.rows, self.columns, operation=True)
        for i in range(copy.rows):
            for j in range(copy.columns):
                copy.set(i+1, j+1, self.get(i+1, j+1))
        return copy

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
        return vector.Vector(self.__A[m-1])
    
    def __column_vector(self, n):
        '''Returns a vector of column n'''
        result=[]
        for i in range(self.rows):
            result.append(self.get(i+1, n))
        return vector.Vector(result)
    
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

    def is_symmetric(self):
        '''Returns whether a matrix is symmetric or not'''
        if self.rows!=self.columns:
            raise vector.DimensionException
        temp=self.copy()
        temp.transpose()
        for i in range(temp.rows):
            for j in range(temp.columns):
                if self.get(i+1, j+1)!=temp.get(i+1, j+1):
                    return False
        return True
    
    def gauss(self):
        '''Performs standard Gauss Elimination on a given matrix. Returns True for an odd amount of row swaps, False for even'''
        row_swaps=False
        for i in range(self.rows-1):
            for j in range(i, self.columns):
                if self.get(i+1, j+1)==0:
                    for l in range(i+1, self.rows):
                        if self.get(l+1, j+1)!=0:
                            row_swaps=not row_swaps
                            curr_row=self.__row_vector(i+1).to_list().copy()
                            next_row=self.__row_vector(l+1).to_list().copy()
                            for x in range(self.columns):
                                self.set(i+1, x+1, next_row[x])
                                self.set(l+1, x+1, curr_row[x])
                            break
                for k in range(i, self.rows-1):
                    coeff=-(self.get(k+2, j+1))/self.get(i+1, j+1)
                    for l in range(j, self.columns):
                        self.set(k+2, l+1, self.get(k+2, l+1)+(coeff*self.get(i+1, l+1)))
                break
        return row_swaps
    
    def rank(self):
        '''Returns the rank of a matrix'''
        temp=self.copy()
        temp.gauss()
        pivots=0
        for i in range(temp.rows):
            row=temp.__row_vector(i+1)
            for j in range(i, temp.columns):
                if row.get(j+1)!=0:
                    col=temp.__column_vector(j+1)
                    coL=col.to_list()
                    if coL!=[] and sum(coL[j+1:])==0:
                        pivots+=1
                        break
        return pivots
    
    def rref(self):
        '''Brings a matrix to its reduced-row-echelon form'''
        self.gauss()
        for i in range(self.rows):
            for j in range(self.columns):
                if self.get(i+1, j+1)==0:
                    continue
                coeff=self.get(i+1, j+1)
                for x in range(j, self.columns):
                    self.set(i+1, x+1, self.get(i+1, x+1)/coeff)
                break
        for i in range(1, self.rows):
            for j in range(self.columns):
                if self.get(i+1, j+1)==0:
                    continue
                for k in range(i, 0, -1):
                    coeff=-(self.get(k, j+1))/self.get(i+1, j+1)
                    for l in range(j, self.columns):
                        self.set(k, l+1, self.get(k, l+1)+(coeff*self.get(i+1, l+1)))
                break
    
    def inverse(self):
        '''Inverts a matrix using the Gauss-Jordan process (if invertible)'''
        if self.rank()<self.columns:
            raise vector.DimensionException
        I=Matrix(self.columns, "identity")
        gj=AugMatrix(self, I)
        gj.rref()
        inv=gj.get_aug()
        for i in range(self.rows):
            for j in range(self.columns):
                self.set(i+1, j+1, inv.get(i+1, j+1))
    
    def determinant(self):
        if self.rows!=self.columns:
            raise vector.DimensionException
        temp=self.copy()
        sign=temp.gauss()
        if sign:
            det=-1
        else:
            det=1
        for i in range(self.columns):
            det*=temp.get(i+1, i+1)
        return det
    
    def projection_matrix(self):
        '''Returns a projection matrix of the current matrix'''
        At=self.copy()
        At.transpose()
        proj=At*self
        proj.inverse()
        proj=proj*At
        proj=self*proj
        return proj
    
    def projection(self, b):
        '''Returns the projection of vector b onto the current matrix'''
        b=b.to_matrix()
        return self.projection_matrix()*b


class AugMatrix(Matrix):

    def __init__(self, A, B):
        if A.rows!=B.rows:
            raise vector.DimensionException
        Matrix.__init__(self, A.rows, A.columns+B.columns, operation=True)
        self.reg_columns=A.columns
        self.aug_columns=B.columns
        for i in range(self.rows):
            for j in range(self.reg_columns):
                self.set(i+1, j+1, A.get(i+1, j+1))
            for k in range(self.reg_columns, self.columns):
                self.set(i+1, k+1, B.get(i+1, k+1-self.reg_columns))
    
    def __str__(self):
        max_width=0
        for i in range(self.rows):
            for j in range(self.columns):
                width=len(str(round(self.get(i+1, j+1), 3)))
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
            for j in range(self.reg_columns):
                w=" "*(max_width-len(str(round(self.get(i+1, j+1), 3))))
                result+=w
                result+=str(round(self.get(i+1, j+1), 3))
                if not j==self.reg_columns-1:
                    result+=" "
            result+=" | "
            for k in range(self.reg_columns, self.columns):
                w=" "*(max_width-len(str(round(self.get(i+1, k+1), 3))))
                result+=w
                result+=str(round(self.get(i+1, k+1), 3))
                if not k==self.columns-1:
                    result+=" "
            if i==0:
                result+='\u2309\n'
            elif i==self.rows-1:
                result+='\u230b'
            else:
                result+="|\n"
        return result
    
    def get_aug(self):
        '''Returns a matrix of the augmented section'''
        aug_matrix=Matrix(self.rows, self.aug_columns, operation=True)
        for i in range(self.rows):
            for j in range(self.aug_columns):
                aug_matrix.set(i+1, j+1, self.get(i+1, j+1+self.reg_columns))
        return aug_matrix