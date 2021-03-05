def quick_sort(alist, first, last):
    # 最优时间复杂度为o(n8log2 n)

    # 最坏时间复杂度为o(n^2)
    # 稳定性：不稳定
    # n = len(alist)
    if first >= last:
        return
    mid = alist[first]
    high = last
    low = first
    while low < high:
        while (low < high) and (alist[high] >= mid):
            high -= 1
        alist[low] = alist[high]

        while (low < high) and (alist[low] <= mid):
            low += 1
        alist[high] = alist[low]

    alist[low] = mid

    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)


if __name__ == '__main__':
    l1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(l1)
    quick_sort(l1,0,len(l1)-1)
    print(l1)














