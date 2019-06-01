# import math;
#
#
# def printPowerSet(set, set_size):
#     # set_size of power set of a set
#     # with set_size n is (2**n -1)
#     pow_set_size = (int)(math.pow(2, set_size))
#     counter = 0
#     j = 0
#     count = 0
#
#     # Run from counter 000..0 to 111..1
#     for counter in range(0, pow_set_size):
#         for j in range(0, set_size):
#
#             # Check if jth bit in the
#             # counter is set If set then
#             # print jth element from set
#             if ((counter & (1 << j)) > 0):
#                 print(set[j], end="")
#                 print("count : ", sum(set[j]))
#
#         print("")
#
#     # Driver program to CodingPractice printPowerSet
#
#
# # set = ['a', 'b', 'c'];
# set = [1, 2, 3, 4, 5];
#
# v = printPowerSet(set, 5)
#
# t = sum(v)
#
# print(t)

#Fibonacci series in Python
# Enter number of terms for the series                 #0,1,1,2,3,5....
a=int(input("Enter the terms"))
f=0  #first element of series
s=1  #second element of series
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s
        print(next,end=" ")
        f=s
        s=next


# Find N largest element from given list of integers

# Function returns N largest elements
def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j];

        list1.remove(max1);
        final_list.append(max1)

    print(final_list)
