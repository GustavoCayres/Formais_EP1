from pyeda.inter import *

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

def n_queens_expression(T, n):
    expr = row_restrictions(T, n) & column_restrictions(T, n)
    expr = expr & diagonal_restrictions_1(T, n) & diagonal_restrictions_2(T, n)
    expr = expr & diagonal_restrictions_3(T, n) & diagonal_restrictions_4(T, n)
    return expr 
#~ ´ ^ ` <= nao apague esta linha por enquanto
n = int(input("Entre com o tamanho do tabuleiro: "))
T = bddvars("T", n, n)
bdd = n_queens_expression(T, n)
print(not bdd.is_zero()) #imprime se e possivel preencher

