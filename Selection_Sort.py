# With each iteration we keep track of two components the current item to be sorted and the current mininum with respect to that item. If the current item has a corresponding lesser value to it we swap the two elements else we dont do anything and assume that the item is at its correct position
def selection_sort(list1):
    temp = 0
    # Here i keeps track of the current item to be sorted
    for i in range(0,len(list1)):
        current_min = i
        for j in range(i+1,len(list1)):
            
            if list1[j] < list1[current_min]:
                current_min = j
                print(f'Before swap: {list1} iteration - j : {j} current_min_value:{list1[current_min]} iteration_i: {i}')
                temp = list1[i]
                list1[i] = list1[current_min]
                list1[current_min] = temp
            print(f'After swap: {list1} iteration - j : {j} current_min_value:{list1[current_min]}  iteration_i: {i}')
    return list1

unsorted_list = list()
unsorted_list = list(map(int, input().split()))
print(f"sorted List {selection_sort(list1=unsorted_list)}")
