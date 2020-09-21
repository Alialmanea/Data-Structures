from random import randint


def SelectionSort(arr):
  min = -1
  for i in range(len(arr)):
    min = i
    for j in range (i+1, len(arr)):
      if arr[min] > arr[j]  :
        min = j
      
    print('min = {}   '.format(arr[min]),arr)
    arr[i], arr[min] =  arr[min], arr[i]




def main():
  arr = []
  for _ in range(10):
    arr.append(randint(-1, 10))
  print('Befor be Sorted Array : ',arr)
  SelectionSort(arr)
  print('After be Sorted Array : ',arr)

main()  
