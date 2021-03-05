def insert_sort(alist):
    """插入序列"""
    # 第一个 0 放在0的位置，第二个 0 和1 比较 range(2),第三个将a[2]和a[0]、a[1]对比range(3)，
    # 第四个将a[3]和a[0]、a[1]、a[2]对比，第n-1个将a[n]和a[0]，……，a[n-2]对比
    # 最坏时间复杂度为o(n^2)
    # 最优时间复杂度为o(n^2)
    # 稳定性为稳定的
    # for j in range(1, len(alist)):
    #     i = j - 1
    #     for i in range(j-1, -1, -1):
    #         if alist[i] > alist[j]:
    #             alist[i], alist[j] = alist[j], alist[i]
    #             j = j - 1
    #             if j <= 0:
    #                 break
    #
    #         else:
    #             break

    for j in range(1, len(alist)):
        i = j - 1
        while i >= 0:
            # for i in range(j-1, -1, -1):

            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                i = i - 1
                # if j <= 0:
                #     break

            else:
                break


if __name__ == '__main__':
    l1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(l1)
    insert_sort(l1)
    print(l1)
#
# def ca(a):
#     for i in range(a):
