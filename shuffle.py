from random import randint


def shuffle_v2(array):
    ''' randomize in-place '''
    _array = array.copy()
    n = len(_array)
    for i in range(n):
        pos = randint(i, n-1)
        _array[i], _array[pos] = _array[pos], _array[i]
    return _array


def shuffle_v1(array):
    ''' permute by sorting '''

    n = len(array)
    keys = [randint(0, n**3) for i in range(n)]
    shuffled, sorted_keys = mergeSort(array, keys)
    return shuffled


def mergeSort(array, keys):
    if len(array) == 1:
        return array, keys
    mid = len(array) // 2
    l, k_l = mergeSort(array[:mid], keys[:mid])
    r, k_r = mergeSort(array[mid:], keys[mid:])
    return merge(l, r, k_l, k_r)


def merge(left, right, key_left, key_right):

    i = j = 0
    c = []
    k = []

    while i < len(left) and j < len(right):
        if key_left[i] <= key_right[j]:
            c.append(left[i])
            k.append(key_left[i])
            i += 1
        else:
            c.append(right[j])
            k.append(key_right[j])
            j += 1

    if i <= len(left) - 1:
        c += left[i:]
        k += key_left[i:]
    elif j <= len(right) - 1:
        c += right[j:]
        k += key_right[j:]
    return c, k


def main():
    ls = list(range(0, 10))
    ss = shuffle_v2(ls)

    print("Before shuffle {}:".format(ls))
    print("_After shuffle {}:".format(ss))


if __name__ == "__main__":
    main()
