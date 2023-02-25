my_list = [1, 3, 5, 7, 9, 11, 23, 59, 98]
def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = int((low + high)/2)
        quess = list[mid]
        if quess == item:
            print("Значение найдено")
            return mid
        if quess > item:
            print("Переходим в первую половину")
            high = mid - 1
        if quess < item:
            print("go to right")
            low = mid + 1
    return "В списке нет такого числа"




print(binary_search(my_list,23))


