from datetime import datetime

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

def inorder(root):
  if root :
    inorder(root.left)
    print(root.data ,end=' ')
    inorder(root.right)

def main():
  str = "the quick brown fox jumps over the lazy dog"
  str = str.replace(" ",'')
  #print(str)

  start_time = datetime.now()
  root = Node('')
  for char in str:
    root = add(root, char)
  inorder(root)  
  end_time = datetime.now()
  print('     Duration: {}'.format(end_time - start_time))
  

main()



