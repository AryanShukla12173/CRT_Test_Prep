#  Logic  : Compare consecutive elements in a array and swap them if one is greater than the other do this n no of times where n is the no. of elements in the array
def bubble_sort(list1):
    for i in range(0,len(list1)):
        for j in range(0,len(list1)-1):
            k = j+1
            if list1[j] > list1[k]:
                temp = list1[k]
                list1[k] = list1[j]
                list1[j] = temp
    return list1

unsorted_list = list()
unsorted_list = list(map(int, input().split()))
print(f"sorted List {bubble_sort(list1=unsorted_list)}")
