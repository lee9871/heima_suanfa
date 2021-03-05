def shell_sort(alist):
    """希尔排序"""
    # 最坏时间复杂度为o(n^2)
    # 稳定性：不稳定

    # a[0],a[4],a[8],进行插入排序，a[1],a[5],a[9],进行插入排序，a[2],a[6]进行插入排序，a[3],a[7]进行插入排序
    # 整体来说
    # grep = 4
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        # for i in range(gap):
            # while i < n-gap:
            #     if alist[i] > alist[gap+i]:
            #         alist[i], alist[gap+i] = alist[gap+i], alist[i]
            #     i += gap
        for i in range(gap, n):
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                i -= gap

        gap //= 2
    return alist




if __name__ == '__main__':
    l1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(l1)
    alist = shell_sort(l1)
    print(alist)

    # alist = shell_sort(alist, 2)
    # print(alist)
    #
    # alist = shell_sort(alist, 1)
    #
    # print(alist)

    # alist = shell_sort(l1, 1)
    #
    # print(alist)











