from random import randint

def insertionSort(arr):  
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 

   

def main():
  arr = []
  for _ in range(10):
    arr.append(randint(-1, 10))
  print('Befor be Sorted Array : ',arr)
  insertionSort(arr)
  print('After be Sorted Array : ',arr)

main()  
