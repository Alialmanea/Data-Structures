from random import randint



def Bublesort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-i-1):
      if arr[j+1] < arr[j]:
        print(arr)
        arr[j+1], arr[j] = arr[j], arr[j+1] 

arr = []
for _ in range(10):
  arr.append(randint(-1, 10))
print('Befor be Sorted Array : ',arr)
Bublesort(arr)
print('After be Sorted Array : ',arr)


def main():
  pass

main()  
