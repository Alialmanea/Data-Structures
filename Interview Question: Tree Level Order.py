
class Node:
  def __init__(self, data):
    self.left = None
    self.data = data
    self.right = None
    

def travarse(root):
  if root is None:
    return

  tovisited = []
  tovisited.append(root)
  
  while(len(tovisited) != 0):
    current = tovisited.pop(0)
    print(current.data, end=" ")
    if current.left is not None: tovisited.append(current.left)
    if current.right is not None: tovisited.append(current.right)
    


def main():
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.right = Node(7)
  root.right.left = Node(6)

  """     1
        /  \
      2     3
     / \   / \
    4   5 6   7
  
  """
  travarse(root)


main()


