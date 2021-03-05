class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None


    def add(self, item):
        """二叉树增加元素"""
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)

            while queue:
                cur_node = queue.pop(0)
                print(node.elem)
                if cur_node.lchild is None:
                    cur_node.lchild = node
                    return
                else:
                    queue.append(cur_node.lchild)
                if cur_node.rchild is None:
                    cur_node.rchild = node
                    return
                else:
                    queue.append(cur_node.rchild)

    def breath_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        """前序"""
        if node is None:
            return
        print(node.elem, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """中序"""
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=' ')
        self.inorder(node.rchild)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=' ')
#
class Solution:
    """最小深度"""
    def run(self , root ):
        depth = 0
        if root is None:
            return depth
        queue = [root]
#         depth = 1
        while queue:
            tempnode = []
#             depth += 1
            for node in queue:
                if  node.lchild is not None:
                        tempnode.append(node.lchild)
                if  node.rchild is not None:
                        tempnode.append(node.rchild)
            queue = tempnode
            depth += 1
        return depth

    def run_recursion(self, root):
        """递归的方式计算 最小深度"""
        if root is None:
            return 0
        if root.rchild is None and root.lchild is None:
            return 1
        if root.rchild is None or root.lchild is None:
            return max(self.run_recursion(root.rchild), self.run_recursion(root.lchild)) + 1
        # else:
        return min(self.run_recursion(root.rchild), self.run_recursion(root.lchild)) + 1


# class Solution:
#     def minDepth(self, root) -> int:
#         if root == None:
#             return 0
#         if root.rchild == None and root.lchild == None:
#             return 1
#         if root.rchild == None or root.lchild == None:
#         # 如果只有一个子节点，如只有左子节点，
#         # 这时，需要沿着左子节点向下寻找直到找到没有左右子节点的节点
#             return max(self.minDepth(root.rchild),self.minDepth(root.lchild))+1
#         return min(self.minDepth(root.rchild),self.minDepth(root.lchild))+1




if __name__ =='__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)


    tree.breath_travel()
    tree.preorder(tree.root)
    print(' ')
    tree.inorder(tree.root)
    print(' ')
    tree.postorder(tree.root)
    depth = Solution()
    # a = depth.run(tree.root)
    # print(' ')
    # print(a)
    b = depth.run_recursion(tree.root)
    print(' ')
    print(b)

