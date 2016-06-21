from sys import stdin as Si,maxsize as m
from math import floor as F 
from collections import defaultdict as dt,Counter as Co
from operator import itemgetter as ig
from math import pi
from itertools import product as P

if __name__== '__main__':
    n = int(Si.readline())
    L = sorted(list(map(int,Si.readline().split())))
    Max = 1
    for l in L:
        #print(l,Max)
        if l>=Max:  Max+=1
    print(Max)

'''
Alyona and Mex
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Someone gave Alyona an array containing n positive integers a1, a2, ..., an. In one operation, Alyona can choose any element of the array and decrease it, i.e. replace with any positive integer that is smaller than the current one. Alyona can repeat this operation as many times as she wants. In particular, she may not apply any operation to the array at all.

Formally, after applying some operations Alyona will get an array of n positive integers b1, b2, ..., bn such that 1 ≤ bi ≤ ai for every 1 ≤ i ≤ n. Your task is to determine the maximum possible value of mex of this array.

Mex of an array in this problem is the minimum positive integer that doesn't appear in this array. For example, mex of the array containing 1, 3 and 4 is equal to 2, while mex of the array containing 2, 3 and 2 is equal to 1.
Input

The first line of the input contains a single integer n (1 ≤ n ≤ 100 000) — the number of elements in the Alyona's array.

The second line of the input contains n integers a1, a2, ..., an (1 ≤ ai ≤ 109) — the elements of the array.
Output

Print one positive integer — the maximum possible value of mex of the array after Alyona applies some (possibly none) operations.
Examples
Input

5
1 3 3 3 6

Output

5

Input

2
2 1

Output

3

Note

In the first sample case if one will decrease the second element value to 2 and the fifth element value to 4 then the mex value of resulting array 1 2 3 3 4 will be equal to 5.

To reach the answer to the second sample case one must not decrease any of the array elements.
'''
        
    
    

            
                
            
        
