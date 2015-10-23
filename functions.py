from pyeda.inter import *

#creates the expression that restricts the existence of queens in row i
def row_restriction(T, n, i):
    row_restriction = 1
    for k in range(0, n - 1):
        temp = 1
        for j in range(k + 1, n):
            temp = temp & ~T[i][j]
        row_restriction = row_restriction & (~T[i][k] | temp)
    temp = 0
    for j in range(0, n):
        temp = temp | T[i][j]
    row_restriction = row_restriction & temp
    return bdd2expr(row_restriction)

#creates the expression that restricts the existence of queens in column j
def column_restriction(T, n, j):
    column_restriction = 1
    for k in range(0, n - 1):
        temp = 1
        for i in range(k + 1, n):
            temp = temp & ~T[i][j]
        column_restriction = column_restriction & (~T[k][j] | temp)
    temp = 0
    for i in range(0, n):
        temp = temp | T[i][j]
    column_restriction = column_restriction & temp
    return bdd2expr(column_restriction)

def diagonal_restriction_1(T, n):
    diagonal_restriction = 1
    for k in range(0, n):
        for i in range(0, n - 1 - k):
            temp = 1
            for j in range(i + 1, n - k):
                temp = temp & ~T[j][j + k]
            diagonal_restriction = diagonal_restriction & (~T[i][i + k] | temp)
    return bdd2expr(diagonal_restriction)



    
#~ ´ ^ `
#n = int(input("Entre com o tamanho do tabuleiro: "))
n= 2
T = bddvars("T", n, n)
print(expr2truthtable(diagonal_restriction_1(T, n)))

    
#A = ~T[0][0]
#for j in range(1, n):
#    A = A & ~T[0][j]
#print(A)
