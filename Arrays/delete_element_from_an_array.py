def delElement(arr, ele):
    arr.remove(ele)

if __name__=='__main__':
    arr=[1,2,3,4,5,6,7]
    ele=6

    print("before removing")
    print(arr)

    delElement(arr,ele)
    print("after deletion")
    print(arr)