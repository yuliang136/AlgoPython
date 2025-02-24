# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 这里连类型都不知道
# 外部输入的反而是暗藏的答案值
def binary_search(arr, quest_value):
    low = 0
    # 数组元素个数为0的话, high为-1 low为0 直接不满足条件
    # 这个值具体为index
    high = len(arr) - 1

    # 这种写法把所有边界情况都考虑了,
    while low <= high:
        mid = (low + high) // 2 # 向下取整的除法

        # algo_mid_guess.
        # item 为外部输入猜测数字.
        algo_mid_guess = arr[mid]
        if algo_mid_guess == quest_value:
            return mid # 这里关键点在返回index值,
        elif algo_mid_guess > quest_value: # 猜的值大了,就把大的范围值砍掉,
            high = mid - 1 # 把整个搜索空间减半
        else:
            # 猜的值小了,就把小的范围值砍掉,
            low = mid + 1 # 把整个搜索空间减半
    return None

# my_list = [1, 3, 5, 7, 9]
my_list = [1, 3, 5, 7, 9]

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # print_hi('moon')
    print(binary_search(my_list, 5)) # => 1
    # print(binary_search(my_list, -1)) # => None
    # l_low = 0
    # l_high = 1
    # l_test = (l_low + l_high) // 2
    # print(l_test)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
