def insertElement(arr, n , x, pos):
    for i in range(n-1, pos-1 , -1):
        arr[ i+ 1]=arr[i]
    arr[pos]=x

if __name__=='__main__':
    arr=[1,2,3,4,5,-1,-1,-1,-1]
    n=5

    print("before insertion")
    for i in range(0, n):
        print(arr[i] , end='')
        print("\n")

    x=10
    pos=2
    insertElement(arr,n,x,pos)
    n+=1

    print("after insertion")
    for i in range(0,n):
        print(arr[i], end='')

