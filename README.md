# linalg
A personal project that implements matricies, vectors, matrix operations, and other linear algebra topics in Python.
## Creating a Matrix
- **m\*n** matrix -> `Matrix(m, n)`
- **n\*n identity matrix** -> `Matrix(n, "identity")`
## Supported Functions on Matrices
- **Addition** -> `A+B`, where A and B are both `m*n` matrices (*returns a new object*)
- **Multiplication** -> `A*B`, where A is an `m*n` matrix, and B is an `n*p` matrix (*returns a new object*)
- **Copy** -> `A.copy()` (*returns a new object*)
- **Get** -> `A.get(i, j)`, returns the value of the matrix entry at (`i`, `j`)
- **Set** -> `A.set(i, j, x)`, sets the matrix entry at (`i`, `j`) to the value `x`
- **Get Column Vector** -> `A.get_vector(n)`, returns the vector at column n
- **Transpose** -> `A.transpose()`, transposes the current matrix object
- **Symmetric?** -> `A.is_symmetric()`, returns whether a matrix is symmetric
- **Gauss Elimination** -> `A.gauss()`, performs standard Gaussian Elimination on the current matrix object (*returns true if an odd amount of row swaps are made, false if even amount of row swaps are made*)
- **Rank** -> `A.rank()`, returns the rank (number of pivots) of the current matrix object
- **Reduced Row Echelon Form** -> `A.rref()`, brings the current matrix object to its reduced row echelon form
- **Inverse** -> `A.inverse()`, inverts the current matrix object (if invertible)
- **Determinant** -> `A.det()`, returns the determinant of the current matrix object
- **Projection Matrix** -> `A.proj_matrix()`, returns the projection matrix of the current matrix object
- **Projection** -> `A.proj(b)`, returns the projection of vector `b` onto the current matrix object
