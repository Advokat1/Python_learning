"""
Реализуйте функции для перемножения матриц с использованием библиотеки NumPy и без неё 
(то есть на чистом Python). Сравните время работы функций при помощи команды %%time
"""
#Python

#ввод параметров матриц
import random
import numpy as np
 
def matrix_mult(m1,m2):
    s=0     #сумма
    t=[]    #временная
    C=[] #матрица после перемножения
    r1=len(m1) 
    c1=len(m1[0]) 
    c2=len(m2[0])  
    for z in range(0,r1):
        for j in range(0,c2):
            for i in range(0,c1):
               s=s+m1[z][i]*m2[i][j]
            t.append(s)
            s=0
        C.append(t)
        t=[]           
    return C
 
a_column=1
b_string=2
#проверка введенных параметров до тех порпока матрицы не будут совместимы
while a_column!=b_string:
    a_string=int(input ('Введите кол-во строк для первой матрицы: '))
    a_column=int(input ('Введите кол-во столбцов для первой матрицы: '))
    b_string=int(input ('Введите кол-во строк для второй матрицы: '))
    b_column=int(input ('Введите кол-во столбцов для второй матрицы: '))
    
#создание матриц 
A = [[random.randrange(0,10) for y in range(a_column)] for x in range(a_string)]
B = [[random.randrange(0,10) for y in range(b_column)] for x in range(b_string)]
#вывод матрица А 
for item in range (a_string):
    print(A[item])
print('_______________')
#вывод матрицы B
for item in range (b_string):
    print(B[item])
print('_______________')
#перемножение матриц в функции
C=matrix_mult(A,B)
#вывод построчно после перемножения
for item in range (a_string):
    print(C[item])

#----------------------------------------------------------------------------------------
#NumPy
print('_________________')
#делаю две матрицы со случайными чсилами (0-1)
A = np.random.sample((a_string,a_column))
B = np.random.sample((b_string,b_column))
C = A.dot(B)
#вывод матрица А 
for item in range (a_string):
    print(A[item])
print('_______________')
#вывод матрицы B
for item in range (b_string):
    print(B[item])
print('_______________')
#вывод построчно после перемножения
for item in range (a_string):
    print(C[item])