def print1toN(n):
    if n == 0:
        return 
    print(n,end=" ")
    print1toN(n-1)

# print1toN(5)

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

# print(fact(32))

def power(a,b):
    if b == 1:
        return a
    return a*power(a,b-1)
# print(power(2,3))

def sum1toN(n):
    if n == 1:
        return 1
    return n+sum1toN(n-1)
# print(sum1toN(4))

#0 1 1 2 3 5 8
def fibonacci(n):
    prev = 0
    curr = 1
    term = 0
    if n == 2 or n == 3:
        return 1
    for i in range(n-2):
        term = prev + curr
        prev = curr
        curr = term
    return term
        
print(fibonacci(1))
l1  = [34,89,56,1,7]
def max_ele(li,m = None):
    if m == None:
        m = li[0]
    elif len(li) == 0:
        print('max element',m)
        return
    elif m<li[0]:
        m= li[0]
    max_ele(li[1:],m)

# max_ele(l1)

def count_no_zeroes(n,count = 0):
    if n % 10 == n:
        print(count)
        return
    
    elif n % 10 == 0:
        count +=1
    count_no_zeroes(n//10,count) 

# print(count_no_zeroes(100))

# Linear Search
def linear_search(l1,key):
    if key == l1[0]:
        print("Key found")
        return
    linear_search(l1[1:],key)
# print(linear_search([10,20,30],20)) 
# def binarySearch(li,key):
#     mid = 
#     right = li[0]
#     left = li[-1]
#     if mid == key or right == key or left == key:
#         print('Key found')
#         return
#     if key> mid:
#         binarySearch(li[mid:],key)
#     if key < mid:  
#         binarySearch(li[:mid+1],key)

# binarySearch([10,20,30,40],20)