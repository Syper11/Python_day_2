l1 = [1,2,3,4,5,6]
l2 = [3,4,5,6,7,8,10]

def merged():
    list = l1+l2
    list.sort(reverse=False)
    print(list)

merged()
