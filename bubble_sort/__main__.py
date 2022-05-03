example_list = [
    20, 25, 15, 14, 8, 32, 19, 40, 2, 17
]

def bubble_sort(iterable: list):
    list_length = len(iterable)
    last_elem_idx = list_length - 1

    for passNbr in range(last_elem_idx, 0, -1):
        for idx in range(passNbr):
            if iterable[idx] > iterable[idx + 1]:
                iterable[idx], iterable[idx + 1] = iterable[idx+1], iterable[idx]

    return iterable


if __name__ == '__main__':
    x = bubble_sort(example_list)
    print(x)