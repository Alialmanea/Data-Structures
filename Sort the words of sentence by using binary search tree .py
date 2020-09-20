class Node:
  def __init__(self, data):
    self.data = data
    self.Next = None


class LinkedList:
  def __init__(self):
    self.head = None
 
  def push(self, data): 
    if self.head is None:
      print('Error ! There is no Head')
      return
    new_node = Node(data) 

    new_node.Next = self.head 

    self.head = new_node 

  def append(self, data): 

        new_node = Node(data) 

        if self.head is None: 
            self.head = new_node 
            return

        last = self.head 
        while (last.Next): 
            last = last.Next
  
       
        last.Next =  new_node   

  def insertAfter(self, prev_node, data): 
   
        if prev_node is None: 
            print ('The given previous node must inLinkedList.')
            return

        new_node = Node(data) 

        new_node.next = prev_node.next
   
        prev_node.next = new_node       
    
  

  def __str__(self): 
        temp = self.head 
        Str = '' 
        while (temp): 
          Str = Str + '{} ->'.format(temp.data)
          temp = temp.Next
        return(Str)  

        

  def count(self, data):
    temp = self.head
    i = 1
    while (temp):
      if temp.data == data:
        return i 
      temp = temp.Next
      i = i +1
    print('The data which you ara looking format,  It is not in LinkedList') 
    return None

  def __len__(self):
    temp = self.head 
    i = 0
    while (temp):  
      temp = temp.Next
      i = i +1
    return i    




def main():
  ls = LinkedList()
  ls.append(2)
  ls.push(1)
  ls.push(0)
  ls.append(3)
  ls.append(4)
  print(ls)
  var = 4
  print('The Number of [{} ] Node in LinkedList is {}  '.format(var,ls.count(var)))
  print('The Lenght of LinkedList is {} '.format(len(ls)))
main()

