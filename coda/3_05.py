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
        self._head = node_1

    def is_empty(self):
        return self._head is None

    def length(self):
        # cur游标，用来移动遍历节点
        cur = self._head
        # count 用来记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count



    def travel(self):
        # cur游标，用来移动遍历节点

        cur = self._head
        while cur is not None:
            print(cur.elem)
            cur = cur.next


    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:

            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            
if __name__ =="__main__":
        l1 = SingleLinkList()
        print(l1.is_empty())
        print(l1.length())

        l1.append(1)
        print(l1.is_empty())
        print(l1.length())
        l1.append(2)
        l1.append(3)
        l1.travel()










node = Node(100)
sll = SingleLinkList(node)
print(2)