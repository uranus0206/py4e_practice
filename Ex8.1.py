def chop(alist):
    del alist[0]
    del alist[-1]
    return None

def middle(alist):
    return alist[1:-1]


arr = [1, 2, 3, 4]
arr2 = arr.copy()
arr3 = arr.copy()

print('arr2 origin: ', arr2)
chop(arr2)
print('arr2 after chop: ', arr2)

print('arr3 origin: ', arr3)
print('arr3 of middle: ',  middle(arr3))
print('arr3 after call middle: ',  arr3)