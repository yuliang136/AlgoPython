def findSmallest(arr):
    smallest = arr[0] # 默认第一个为最小
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    # 进行一次深拷贝
    copiedArr = list(arr) # copy array before mutating

    # 每次从copiedArr里操作
    # 从某些语言来看, 这样写有问题
    # 在foreach里 不能改变操作的元素?
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr


if __name__ == '__main__':
    print('PyCharm')

    print(selectionSort([5, 3, 6, 2, 10]))