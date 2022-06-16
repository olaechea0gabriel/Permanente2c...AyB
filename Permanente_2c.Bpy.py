#Permanente_2cB.py
#/////////////////////////////////////////////////////////////////
import time
import random

n = [10000, 50000]

def BUBBLE_SORT(L):
    n = len(L)
    for i in range(n):
        for j in range (n - i - 1):
            if(L[j] > L[j + 1]):
                L[j], L[j + 1] = L[j+1], L[j]
    return L

BUBBLE_SORT(n)
