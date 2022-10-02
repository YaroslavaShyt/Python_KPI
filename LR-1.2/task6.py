class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return BinaryTree(data)
    if list(data.keys()) < list(node.data.keys()):
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node


def inorder(r):
    if r:
        inorder(r.left)
        print(r.data)
        inorder(r.right)


class Counter:
    def __init__(self):
        self.goods = {}
        self.choice = 1
    
    def search(self, r, code):
        if r is None or code == list(r.data.keys())[0]:
            if r:
                return r.data[code]
            return r
        if list(r.data.keys())[0] < code:
            return self.search(r.right, code)
        return self.search(r.left, code)
    
    def scan_count(self):
        price = 0
        while self.choice:
            print('Enter code and quantity: ')
            code, n = int(input()), int(input())
            if not self.search(root, code):
                print('This item does not exist!')
            else:
                self.goods[code] = n
                print('Add more goods? - (0 - no; 1 - yes)')
                self.choice = int(input())
                price += self.search(root, code) * n
        return price


root = None
root = insert(root, {8987: 33})
root = insert(root, {3876: 234})
root = insert(root, {1218: 55})
root = insert(root, {6392: 22})
root = insert(root, {7223: 333})
inorder(root)
c = Counter()
print('Total:', c.scan_count())
