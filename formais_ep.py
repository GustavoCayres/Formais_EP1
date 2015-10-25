from pyeda.inter import *
import sys

#restricts the existence of queens per row
def row_restrictions(T, n):
    row_restriction = 1
    for i in range (0, n):
        for k in range(0, n - 1):
            temp = 1
            for j in range(k + 1, n):
                temp = temp & ~T[i][j]
            row_restriction = row_restriction & (~T[i][k] | temp)
        temp = 0
        for j in range(0, n):
            temp = temp | T[i][j]
        row_restriction = row_restriction & temp
    return row_restriction

#restricts the existence of queens per column
def column_restrictions(T, n):
    column_restriction = 1
    for j in range(0, n):
        for k in range(0, n - 1):
            temp = 1
            for i in range(k + 1, n):
                temp = temp & ~T[i][j]
            column_restriction = column_restriction & (~T[k][j] | temp)
        temp = 0
        for i in range(0, n):
            temp = temp | T[i][j]
        column_restriction = column_restriction & temp
    return column_restriction

#restricts the existence of queens per diagonal above the main one
def diagonal_restrictions_1(T, n):
    diagonal_restrictions = 1
    for k in range(0, n):
        for i in range(0, n - 1 - k):
            temp = 1
            for j in range(i + 1, n - k):
                temp = temp & ~T[j][j + k]
            diagonal_restrictions = diagonal_restrictions & (~T[i][i + k] | temp)
    return diagonal_restrictions

#restricts the existence of queens per diagonal below the main one
def diagonal_restrictions_2(T, n):
    diagonal_restrictions = 1
    for k in range(1, n):
        for i in range(0, n - 1 - k):
            temp = 1
            for j in range(i + 1, n - k):
                temp = temp & ~T[j + k][j]
            diagonal_restrictions = diagonal_restrictions & (~T[i + k][i] | temp)
    return diagonal_restrictions

def diagonal_restrictions_3(T, n):
    diagonal_restrictions = 1
    for k in range(0, n):
        for i in range(0, n - 1 - k):
            temp = 1
            for j in range(i + 1, n - k):
                temp = temp & ~T[n - 1 - k - j][j]
            diagonal_restrictions = diagonal_restrictions & (~T[n - 1 - k - i][i] | temp)
    return diagonal_restrictions

def diagonal_restrictions_4(T, n):
    diagonal_restrictions = 1
    for k in range(1, n):
        for i in range(0, n - 1 - k):
            temp = 1
            for j in range(i + 1, n - k):
                temp = temp & ~T[n - 1 - j][j + k]
            diagonal_restrictions = diagonal_restrictions & (~T[n - 1 - i][i + k] | temp)
    return diagonal_restrictions

def n_queens_BDD(T, n, queens):
    expr = row_restrictions(T, n) & column_restrictions(T, n)
    expr = expr.restrict(queens)
    expr = expr & diagonal_restrictions_1(T, n) & diagonal_restrictions_2(T, n)
    expr = expr.restrict(queens)
    expr = expr & diagonal_restrictions_3(T, n) & diagonal_restrictions_4(T, n)
    expr = expr.restrict(queens)
    return expr 

def display(solution, T, n):
    chars = list()
    for r in range(n):
        for c in range(n):
            if solution[T[r,c]]:
                chars.append("Q")
            else:
                chars.append(".")
        if r != n-1:
            chars.append("\n")
    print("".join(chars))

#~ ´ ^ ` <= nao apague esta linha por enquanto
data = sys.stdin.readlines()

n = int(data[0].split()[0])
T = bddvars("T", n, n)

k = int(data[0].split()[1])
queens = {}
for i in range(1, k + 1):
    x = int(data[i].split()[0])
    y = int(data[i].split()[1])
    queens[T[x][y]] = 1
print(queens)
bdd = n_queens_BDD(T, n, queens)

if bdd.is_zero():
	print("UNSAT") #imprime se e possivel preencher
else:
	print("SAT") #imprime se e possivel preencher
	display(bdd.satisfy_one(), T, n)

