def bubble_sort(alist):
    """冒泡排序"""
    # j是遍历的轮次
    # i是每层遍历，第一次0 - n-2,range(0,n-1),第二次0 - j-3,最后一次 0-1
    # 最坏时间复杂度为o(n^2)
    # 最优时间复杂度为o(n)
    # 稳定性：是稳定的

    n = len(alist)
    for j in range(len(alist)-1):
        count = 0
        for i in range(0, n-j-1):
            if alist[i] > alist[i+1]:
                count += 1
                alist[i + 1], alist[i] = alist[i], alist[i + 1]
        if 0 == count:
            break


if __name__ == '__main__':
    l1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(l1)
    bubble_sort(l1)
    print(l1)