# a = 1
# print(a)
# print(a)
# a += a
#
#
# def fun(f):
#     b = f + 1
#     return b
#
#
# d = 10
# c = fun(d)
# print(a)


class Node(object):
    def __init__(self, ele):
        self.elem = ele
        self.next = None


class SingleLinkList(object):
    def __init__(self, node_1=None):
        self.__head = node_1

    def is_empty(self):
        return self.__head is None

    def length(self):
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count 用来记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # cur游标，用来移动遍历节点

        cur = self.__head
        while cur is not None:
            print(cur.elem,  end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:

            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:

            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 当循环推出后 pre指向pos-1
            node.next = pre.next
            pre.next = node

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next




if __name__ == "__main__":

    l1 = SingleLinkList()
    print(l1.is_empty())
    print(l1.length())

    l1.append(1)
    print(l1.is_empty())
    print(l1.length())
    l1.append(2)
    l1.add(8)
    l1.append(3)
    l1.travel()
    l1.insert(-1, 10)
    l1.travel()
    l1.insert(2, 120)
    l1.travel()
    l1.insert(10, 1320)
    l1.travel()
    l1.add(1)
    l1.travel()

    l1.remove(1)
    l1.travel()



