import random

def random_int_list(start=1, stop=1000, length=500):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    return [random.randint(start, stop) for _ in range(length)]


