def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    ans = fib(n-1) + fib(n-2)
    return ans
"""
As we can see in the above example the for the 55th term of the fibonacci series python takes a significant amount of time meaning recursion is not feasible for large number of recursive operations, in such cases we use DP(Dynammic Programming) which will have less complexity than the recursive approach.
We have some key concepts in DP such as Memoization which means storing an intermediate result for a calculation and using this stored calculation to perform the next calculation
"""

#DP Implementation of Fibonacci Series using Top Down Approach
# def fibo(n,dp=None):
#     if dp == None:
#         dp = [-1] *(n+1)
#     if n == 0:
#         dp[n] = 0
#         return n
#     if n == 1:
#         dp[n] = 1
#         return n
#     if dp[n] != -1:
#         return dp[n]
#     ans = fibo(n-1,dp) + fibo(n-2,dp)
#     dp[n] = ans
#     print(dp)
#     return ans

# print(fibo(3))

#DP Implementation of Fibonacci Series using Bottom Up Approach
# def fibo(n):
#     if n<=1:
#         return n
#     dp = [0]*(n+1)
#     dp[1] = 1
#     for i in range(2,n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]

# print(fibo(44))
        
# Subset of a List only solvable by backtracking
x = [1,2,3]
def subsetofList(ans = None,index=0):
    if ans == None:
        ans = []
    if index == len(x):
        print(ans,end=" ")
        return
    subsetofList(ans+[x[index]],index+1)
    subsetofList(ans,index+1)

subsetofList(x)

"""
Knapsack Problem Steps:
Calculate profit or weight per kg
Sort the price or weight list to get the max price
According to bag capacity push product into bag
Types of Knapsack:
0/1 Knapsack (item cannot be  repeated in the bag and items cannot be added in fractions )
Fractional Knapsack (item can be repeated in the bag and items can be added in fractions)
Unbounded Knapsack (item can be repeated inside the bag and items cannot be divided )
"""

# class Knapsack:
#     def __init__(self,max_capacity,items_list) -> None:
#         self.max_capacity = max_capacity
#         self.items_list = items_list
    
#     def solveKnapsack(self):
#         self.items_list.sort(key = lambda x:x[2],reverse=True)
#         weights_list = 
#         print(self.items_list)
#         price_per_kg = []
#         # for material,weight in self.items_list:
            
            

        
# k = Knapsack(10,[['Silver',10,30],['Gold',20,100],['Plastic',5,15]])
# k.solveKnapsack()

    
        