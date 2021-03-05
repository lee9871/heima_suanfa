def binary_search(alist, item):
    """二分查找"""
    # 稳定的
    # 最坏时间复杂度为o(1)
    # 最优时间复杂度为o(nlog2n)
    # n = len(alist)
    # first = 0
    # last = n-1
    ## 非递归
    # while first <= last:
    #     mid = first + last//2
    #     if first == last and item !=alist[first]:
    #         return False
    #     if item < alist[(first+last)//2]:
    #         last = (first+last)//2
    #     elif item > alist[(first+last)//2]:
    #         first = (first + last) // 2+1
    #     elif item == alist[(first+last)//2]:
    #         return (first+last)//2

    ## 递归

    n = len(alist)
    if n ==0:
        return False
    first = 0
    last = n - 1


    # if first == last and item !=alist[first]:
    #          return False
    if item < alist[(first+last)//2]:
            last = (first+last)//2
            return binary_search(alist[first:last], item)
    elif item > alist[(first+last)//2]:
            first = (first + last) // 2 + 1
            return binary_search(alist[first: last+1], item)
    elif item == alist[(first+last)//2]:
            # return (first+last)//2
            return True
    else:
        return False


if __name__ == '__main__':
    l1 = [17,26, 31, 44, 55, 65, 67, 98,555]
    print(l1)
    a = binary_search(l1,0)
    print(a)


