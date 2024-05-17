def insertElement(arr, ele):
    arr.append(ele)

if __name__=='__main__':
    arr=[1,3,4,56,8]
    ele=36

    print("before insertion the array is ")
    print(arr)

    insertElement(arr , ele)
    print("after insertion")
    print(arr)