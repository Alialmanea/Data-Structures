class node:
  def __init__(self):
    self.data = None
    self.next = None
    self.oldmax = None

class Stack:
  def __init__(self):
    self.__stack = None
    self.__max = None

  def push(self, data):
    n = node()
    n.data = data
    if (self.__stack is None):
      self.__stack = n
    else:
      n.next = self.__stack
      self.__stack = n  
    if self.__max is None or n.data > self.__max.data:
      n.oldmax = self.__max
      self.__max = n

  def pop(self):
    if self.__stack is None:
      print('The Stack is None !')
      return
    n = self.__stack
    self.__stack = n.next
    if n.oldmax is not None:
      self.__max = n.oldmax

    return n

  def __str__(self):
    Str = ''
    temp = self.__stack
    while(temp):
      Str = Str + '{} '.format(temp.data)  
      temp = temp.next
    return Str

  def max(self):
    if self.__max is not None:
      return self.__max.data 
    return None             



def main():
  stack = Stack()
  stack.push(3)
  stack.push(2)
  stack.push(1)
  print(stack)
  stack.pop()
  print(stack)
  print(stack.max())



main()
