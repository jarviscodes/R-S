example_list = [
    20, 25, 15, 14, 8, 32, 19, 40, 2, 17
]

def insertion_sort(iterable: list):
    for i in range(1, len(iterable)):
        j = i - 1
        next_elem = iterable[i]
        while (iterable[j] > next_elem) and (j >= 0):
            iterable[j+1] = iterable[j]
            j = j - 1
        iterable[j+1] = next_elem
    return iterable

if __name__ == '__main__':
    x = insertion_sort(example_list)
    print(x)
