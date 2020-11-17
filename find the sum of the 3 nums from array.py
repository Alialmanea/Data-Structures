import random

def threesum(arr, n):
  result = []
  arr.sort()
  for i in range(len(arr)-3):
    if i == 0 or arr[i] > arr[i-1]:
      start = i+1
      end = len(arr) - 1
      while(start < end):
        if arr[i] + arr[start] + arr[end] == n:
          result.append([arr[i], arr[start], arr[end]])
        if arr[i] + arr[start] + arr[end] < n:
          current = start
          while(arr[start] == arr[current] and start < end):
            start += 1
        else:
          currentend = end
          while(arr[end] == arr[currentend] and start < end):
            end -= 1 
  return result             


def main():
  arr = [random.randrange(10) for i in range(10)]
  print(arr)
  print("The result of 3 is: {}".format(threesum(arr, 8)))


main()


