import QuickSort
import random

def RANDOM_PARTITION(A, p, r):
    # i = random.choice(A)
    # A[A.index(i)], A[r] = A[r], A[A.index(i)]
    i = random.choice(range(p, r+1))
    A[i], A[r] = A[r], A[i]
    return QuickSort.PARTITION(A, p, r)

def RANDOMIZED_QUICKSORT(A, p, r):
    if p < r:
        q = RANDOM_PARTITION(A, p, r)
        RANDOMIZED_QUICKSORT(A, p, q - 1)
        RANDOMIZED_QUICKSORT(A, q + 1, r)

if __name__ == "__main__":
    A = [12, 123, 22, 66, 5, 134, 56, 1241, 541]
    RANDOMIZED_QUICKSORT(A, 0, len(A) - 1)
    print(A)