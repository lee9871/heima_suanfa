class Stack(object):
    """栈"""

    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加"""
        self.__list.append(item)

    def pop(self):
        """弹出"""
        return self.__list.pop()

    def peek(self):
        """"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == '__main__':

    s = Stack()
    print(s.size())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.pop())
    print(s.pop())
    print(s.pop())

