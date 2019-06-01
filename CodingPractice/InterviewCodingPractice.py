import math;


def printPowerSet(set, set_size):
    # set_size of power set of a set
    # with set_size n is (2**n -1)
    pow_set_size = (int)(math.pow(2, set_size))
    counter = 0;
    j = 0;
    count = 0

    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size):
        for j in range(0, set_size):

            # Check if jth bit in the
            # counter is set If set then
            # print jth element from set
            if ((counter & (1 << j)) > 0):
                print(set[j], end="")
              #  print("count : ",sum(set[j]))

        print("");

    # Driver program to CodingPractice printPowerSet



# set = ['a', 'b', 'c'];
set = [1, 2, 3, 4, 5];

v=printPowerSet(set, 5)

t = sum(v)

print(t)


#source -- >   https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
q=[]
queries = []
zero = [0]*(n+1)
def arrayManipulation(n, queries):    
    for i in range(len(queries)):
        q=queries[i]        
        zero[q[0]-1]+=q[2]
        zero[q[1]]-=q[2]    
    return max(accumulate(zero))


#source -- > https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/hamiltonian-and-lagrangian/

n = int(input())             # Number of elements of array
array = [int(i) for i in input().split()]
def compare(array,val):
    return (all(val>=x for x in array))
a_1=array[:]           
for i in a_1:
    array.pop(0)
    if compare(array,i):
        print(i,end=" ")

