class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def insert(self, node, data):
        if node is None:
            return Node(data)
        if list(data.keys()) < list(node.data.keys()):
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)


class Counter:
    def __init__(self):
        self.goods = {}
        self.choice = 1

    def search(self, root, code):
        if root is None:
            return root
        elif root and code == list(root.data.keys())[0]:
            return root.data[code]
        elif list(root.data.keys())[0] < code:
            return self.search(root.right, code)
        return self.search(root.left, code)

    def scan_count(self, root):
        price = 0
        while self.choice:
            print('Enter code and quantity: ')
            code, n = int(input()), int(input())
            if not self.search(root, code):
                raise ValueError('This item does not exist!')
            self.goods[code] = n
            print('Add more goods? - (0 - no; 1 - yes)')
            self.choice = int(input())
            if not isinstance(self.choice, int):
                raise TypeError('Incorrect value for choice!')
            elif self.choice not in range(0, 2):
                raise ValueError('Incorrect number for choice!')
            price += self.search(root, code) * n
        return price


def main():
    try:
        r = None
        b = BinaryTree()
        r = b.insert(r, {8987: 33})
        r = b.insert(r, {3876: 234})
        r = b.insert(r, {1218: 55})
        r = b.insert(r, {6392: 22})
        r = b.insert(r, {7223: 333})
        b.inorder(r)
        c = Counter()
        print('Total:', c.scan_count(r))
    except Exception as ex:
        print(ex)


main()
