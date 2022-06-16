#Permanente2cA.py
#///////////////////////////////////////////////////////////////////
import time
import random

n = 100000
x = time.time()
y = time.time()

parametro = list(range(n))
random.shuffle(parametro)

def INSERTION_SORT(A):
    for j in range(len(A)-1):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
        time.time()
    return A

INSERTION_SORT(parametro)
print("TIEMPO == ", y - x)

#_________________________________________

#n = [10000, 50000]

#def BUBBLESORT(L):
#    n = len(L)
#    for i in range(n):
#        for j in range (n - i - 1):
#            if(L[j] > L[j + 1]):
#                L[j], L[j + 1] = L[j+1], L[j]
#    return L

#BUBBLESORT(n)
