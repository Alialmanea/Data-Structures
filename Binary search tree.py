class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

def add(root, data):
  if root is None:
    return Node(data)
  else:
    if root.data == data:
      return root
    elif root.data < data :  
      root.right = add(root.right, data)
    else:
      root.left = add(root.left, data)
  return root




