def reverse(A): 
    N = len(A)
    
    for i in range(N // 2): 
        k = N - i - 1
        A[i], A[k] = A[k], A[i] 
        
    return A

reverse([1,2,3]);

#######

"""
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].

"""


def solution(A, K):

    if A:
        #arr_len = len(A) - 1
        num_rotate = 0

        while num_rotate < K:
            A.insert(0, A[-1])
            #A.insert(0, A[arr_len])
            #print(A[arr_len])
            #print(A)
            A.pop(-1)

            #print("pop: ", A)
            num_rotate += 1
        return A
    return A 

print(solution([3, 8, 9, 7, 6], 3))
print(solution([0, 0, 0], 3))
#print(solution([1, 2, 3, 4], 4))
print(solution([], 1))


"""
def solution(A=[0], K=0):

        arr_len = len(A) - 1     
        num_rotate = 0

        while num_rotate < K:
            A.insert(0, A[arr_len])
            #print(A[arr_len])
            #print(A)
            A.pop(-1)

            #print("pop: ", A)
            num_rotate += 1
        return A


#print(solution([3, 8, 9, 7, 6], 3))
#print(solution([1, 2, 3, 4], 4))
print(solution())

"""

######


#def solution(A)

from collections import Counter


A = [9,3,9,3,9,7,9]

# check if array passed is odd or even

Is_Odd = (len(A) % 2 != 0)
print(Is_Odd)

# check if elements are odd numbers

Is_N_Odd = list(filter(lambda x: x % 2 == 0, A))
print(Is_N_Odd)
print(Is_N_Odd == [])



if Is_Odd == True and Is_N_Odd==[] : 

    ctr = Counter()

    for i in A:
        ctr[i] += 1
        
    print (ctr)

    for key in ctr:
        ctr_val = ctr.get(key)
    
        if ctr_val == 1:
            print(ctr_val)
            
            print(key)    


######

