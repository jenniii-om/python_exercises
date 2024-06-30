"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

class Solution { public int solution(int N); }

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""


def solution(N):
  
  # Cast to string since casting to binary gives a prefix of 0b
  x = str(bin(N))

  #x = bin(9)
  #print(x)
  #print(type(x))
  #print(x[2:])
  
  # Initialize variables
  ctr = 0
  max_gap = 0

  for i in x[2:]:                       # Iterate throughout the string length starting from 3rd position discarding the 0b prefix
      if i == "1":                      # If value is 1, check if max_gap has a value that is greater than the counter
        if max_gap >= ctr:                  # if greater than the counter, retain, max_gap number
           max_gap
        else:                               # if not, get the max_gap value from the counter value
           max_gap = ctr
        ctr = 0                         # Reset counter value since it's not a binary gap
      else:
        ctr += 1                        # Else, count for binary gap or not "1"
        
     # print(i, ">> ctr: ", ctr, " >> big gap: ", big_gap)
  return max_gap

print(solution(9)   , " >> binary: ", bin(9))
print(solution(529) , " >> binary: ", bin(529))
print(solution(20)  , " >> binary: ", bin(20))
print(solution(32)  , " >> binary: ", bin(9))

#print("no. of gaps: ", gap_ctr)


