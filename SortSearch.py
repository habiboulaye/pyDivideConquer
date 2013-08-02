#!/usr/bin/env python2
# -*- coding: latin-1 -*-
"""
    Divide & Conquer strategy
    - Sorting algorithm: QuickSort
    - Searching algorithms: Binary Search
      -> Recursive implementation
      -> iterative implementation
    @author: Habib
    @contact: Habiboulaye@gmail.com
"""

# Sorting algorithm
def QuickSort(A, lo, hi):
    """
        QuickSort algorithm 
    """
    mid=A[lo+(hi-lo)/2]
    i,j=lo,hi
    while i<j:
        while A[i] < mid: i+=1
        while A[j] > mid: j-=1
        if i<=j:
            tmp=A[i]
            A[i]=A[j]
            A[j]=tmp
            i+=1
            j-=1
    if i<hi: 
        QuickSort(A,i,hi)
    if j>lo: 
        QuickSort(A,lo,j)    

# Efficient searching algorithms  
def binarySearch(A,lo, hi, val):
    """
        Binary Search: Recusive implementation
    """
    if lo>hi:  
        return -1
    mid=lo+(hi-lo)/2
    if A[mid]==val: 
        return mid

    elif A[mid]>val:
        return binarySearch(A,lo, mid, val)
    elif A[mid]<val:
        return binarySearch(A,mid, hi, val)

def binarySearch2(A,lo, hi, val):
    """
        Binary Search: Iterative implementation
    """
    while lo<=hi:
        mid=lo+(hi-lo)/2
        if A[mid]==val:
            return mid
        elif A[mid]<val:
            lo=mid+1
        elif A[mid]>val:
            hi=mid-1
    return -1
    
    
