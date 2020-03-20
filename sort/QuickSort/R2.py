import QuickSort
import random

def RANDOM_PARTITION(A, p, r):
    i = random.choice(A)
    i = A.index(i)
    # A[A.index(i)], A[r] = A[r], A[A.index(i)]
    # i = random.choice(range(p, r+1))
    A[i], A[r] = A[r], A[i]
    print "i is", i, "A is", A
    return QuickSort.PARTITION(A, p, r)

def RANDOMIZED_QUICKSORT(A, p, r):
    if p < r:
        q = RANDOM_PARTITION(A, p, r)
        RANDOMIZED_QUICKSORT(A, p, q - 1)
        RANDOMIZED_QUICKSORT(A, q + 1, r)

A = [12, 123, 22, 66, 5, 134, 56, 1241, 541]
print "A is", A
RANDOMIZED_QUICKSORT(A, 0, len(A) - 1)
print A