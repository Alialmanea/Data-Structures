class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def preorder(root):
    if root is None:
        return

    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=' ')





def main():
    node = Node(5)
    node.left = Node(4)
    node.left.left = Node(3)
    node.right = Node(2)
    node.right.right = Node(1)
    print('inorder:', end=' ')
    inorder(node)
    print()
    print('preorder:', end=' ')
    preorder(node)
    print()
    print('postorder:', end=' ')
    postorder(node)

if __name__ == '__main__':
    main()



