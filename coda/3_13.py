class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None

class DoubleLinkeList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None
    
    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        if self.is_empty():
            node = Node(item)
            node.next = self.__head
            self.__head = node
        else:
            node = Node(item)
            node.next = self.__head
            self.__head = node
            node.next.prev = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.pre = cur

    def insert(self, pos, item):

        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next = node
            cur.next.prev = node

    def remove(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                # 删除的头节点
                if cur == self.__head:
                    self.__head = cur.next
                    # 判断链表是否只有一个节点
                    if cur.next is not None:
                        cur.next.prev = None

                else:
                    # 删除的中间节点
                    cur.prev.next = cur.next
                    # 判断链表是否尾节点
                    if cur.next is not None:
                        cur.next.pre = cur.pre
                break
            else:
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False






if __name__ == "__main__":
    dll = DoubleLinkeList()
    a = dll.is_empty()
    b = dll.length()
    print(a)
    print(dll.length())
    dll.add(1)
    print(dll.length())
    dll.travel()
    dll.add(2)
    dll.travel()
    dll.insert(2, 3)
    dll.travel()
    dll.remove(2)
    dll.travel()







