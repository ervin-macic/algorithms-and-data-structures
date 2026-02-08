from math import floor, log2
from random import randint
k = 20000 # number of bits
n = 1000000 # number of operations
r = 0 # runtime so far
t = 0 # number of calls to increment since last reset
A = [0] * k
def increment():
    global r, t 
    t += 1
    i = 0
    while i < k and A[i] == 1:
        A[i] = 0
        r += 1 # keep track of changes to bits
        i += 1
    if i < k:
        A[i] = 1
        r += 1 # we have a change here, too
def reset():
    global r, t
    if t == 0:
        return
    for i in range(floor(log2(t)) + 1):
        A[i] = 0
        r += 1
    t = 0
for _ in range(n):
    if randint(1,1000) == 1:
        reset()
    else:
        increment()
print(r / n)