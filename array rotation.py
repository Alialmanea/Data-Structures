def rotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)

def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
    arr[n-1] = temp




def main():
    arr=[1,2,3,4,5,6,7,8,9]
    rotate(arr, 2, len(arr))
    print(arr)
