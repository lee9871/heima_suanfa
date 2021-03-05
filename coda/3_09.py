
class Node(object):
    def __init__(self, ele):
        self.elem = ele
        self.next = None


class SingleLinkList(object):
    """单向循环链表"""
    def __init__(self, node_1=None):
        self.__head = node_1
        if node_1:
            node_1.next = node_1

    def is_empty(self):
        return self.__head == None

    @property
    def length(self):
        # cur游标，用来移动遍历节点
        # count 用来记录数量
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        # if cur.next == None:
        #     return count

        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # cur游标，用来移动遍历节点
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem,  end=' ')
            cur = cur.next
        # 退出循环，cur指向尾节点，但尾节点没有打印
        print(cur.elem,  end=' ')
        print('')

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环之后，cur指向尾节点
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length -1:
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
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                if cur == self.__head:
                    # 头节点
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 尾节点
        if cur.elem == item:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next


if __name__ == "__main__":
    l1 = SingleLinkList()
    print(l1.is_empty())
    print(l1.length)
    l1.append(1)
    print(l1.is_empty())
    print(l1.length)
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