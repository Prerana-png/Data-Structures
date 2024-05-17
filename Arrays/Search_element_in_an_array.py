def searchElement(Arr, n , ele):
    for i in range(n):
        if(Arr[i]==ele):
            return i
    return -1

if __name__=="__main__":
    Arr=[1,2,3,4,5,6]
    n=len(Arr)
    ele=5

    index=searchElement(Arr,n, ele)
    if index !=-1:
        print("element found at position " +str(index+1))
    else:
        print("element not found")
