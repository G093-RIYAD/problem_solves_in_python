#01 Reverse a list in Python
list1 = [100, 200, 300, 400, 500]          #Exercise 1: Reverse a list in Python
list1.reverse()
print(list1)

#02 Concatenate two lists index-wise.
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

#03 Turn every item of a list into its square.
numbers = [1, 2, 3, 4, 5, 6, 7]
res = []
for i in numbers:
    res.append(i*i)
print(res)

#04 Concatenate two lists in the following order.
list01 = ["Hello ", "take "]
list02 = ["Dear", "Sir"]
res = [x + y for x in list01 for y in list02]
print(res)

#05 Iterate both lists simultaneously.
num_list1 = [10, 20, 30, 40]
num_list2 = [100, 200, 300, 400]
for x,y in zip(num_list1,num_list2[::-1]):
    print(x,y)
