class node:
  def __init__(self, data):
    self.data = data
    self.next = None


class linkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = node(data)
    if self.head is None:
      self.head = new_node
      return

    last = self.head
    while(last.next):
      last = last.next

    last.next = new_node

  def __str__(self):
    Str = ''
    temp = self.head
    while(temp):
      Str = Str + '{}--> '.format(temp.data)  
      temp = temp.next
    return Str     

  def NthToLast(self, num):
    current = self.head
    follower = self.head
    for i in range(num):
      if (current is None):
        return None
      current = current.next

    while(current.next != None):
      current = current.next
      follower = follower.next

    return follower.data        

  def count(self, data):
    temp = self.head
    i = 0
    while (temp):
      if temp.data == data:
        return i 
      temp = temp.next
      i = i +1
    print('The data which you ara looking format,  It is not in LinkedList') 
    return None    

  def __len__(self):
    temp = self.head 
    i = 1
    while (temp):  
      temp = temp.next
      i = i +1
    return i   



def main():
  ls = linkedList()
  ls.append(1)
  ls.append(2)
  ls.append(3)
  ls.append(4)
  ls.append(5)
  print(ls)
  print(ls.NthToLast(1))




main()
