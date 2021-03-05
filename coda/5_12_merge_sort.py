def merge_sort(alist):
    """归并排序"""
    # 稳定的
    # 最坏时间复杂度为o(nlog2n)
    # 最优时间复杂度为o(nlog2n)
    n = len(alist)
    if n == 1:
        return alist
    mid = n//2
    # left = alist[:mid]
    # right = alist[mid:]
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    left_pointer = 0
    right_pointer = 0
    result = []

    while left_pointer <= len(left)-1 or right_pointer <= len(right)-1:
            if left_pointer >= len(left):
                result.append(right[right_pointer])
                right_pointer += 1
            elif right_pointer >= len(right):
                result.append(left[left_pointer])
                left_pointer += 1

            elif left[left_pointer] <= right[right_pointer] and left_pointer <= len(left)-1 and right_pointer <= len(right)-1:
                result.append(left[left_pointer])
                left_pointer += 1
            elif left[left_pointer] > right[right_pointer] and left_pointer <= len(left)-1 and right_pointer <= len(right)-1:
                result.append(right[right_pointer])
                right_pointer += 1

    return result

    # left_sort = merge_sort(left)
    # right_sort = merge_sort(right)
    # left_sort.extend(right_sort)


if __name__ == '__main__':
    l1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(l1)
    result = merge_sort(l1)
    print(result)
























