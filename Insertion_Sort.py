# [ 8, 5, 7, 3, 2] For insertion sort working , consider the first element to be in its sorted position and remaining elements are not sorted
# Algo : Step 1 : Take out the first element in the unsorted partition and consider its index to be blank in this case it will 5
        # Step 2 : Increase the size of the sorted portion
        # Step 3 : Compare all elements in the sorted portion if element > sorted_element then go to Step 4 else Step 5
        # Step 4 : Place element at i+1 position after the element which is being compared
        # Step 5 : Shift element that is being compared to its right by an increment and place the element at its position and then go to step 3 until all elements are finished

def insertion_sort( list1):
    key,j = 0,0
    for i in range(1,len(list1)):
        key = list1[i]
        j = i-1
        while j>=0 and list1[j] > key:
            list1[j+1] = list1[j]
            j-= 1
        print(list1)
        list1[j+1] = key
        print(list1)
    return list1
unsorted_list = list()
unsorted_list = list(map(int, input().split()))
print(f"sorted List {insertion_sort(list1=unsorted_list)}")

            
