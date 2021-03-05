def select_sort(alist):
    """选择排序"""
    # 升序中选择最小的
    # 最坏时间复杂度为o(n^2)
    # 最优时间复杂度为o(n^2)
    # 不稳定：对于升序中选择最大的  稳定性是指对于两个相同的数值，在排序后仍保持原来顺序 则是稳定的

    # 第一个 a[0] 1-n-1,range(1,n),第二个 a[1] 2-n-1,range(2,n),最后一个 a[n-2] n-1,range(n-1,n)
    for j in range(1, len(alist)):
        min_index = j-1
        for i in range(j, len(alist)):

            if alist[min_index] > alist[i]:
                min_index = i

        alist[min_index], alist[j-1] = alist[j-1], alist[min_index]
        print(alist)



if __name__ == '__main__':
    l1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(l1)
    select_sort(l1)
    print(l1)