# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

from collections import Counter
def majorityElement(arr):
 
    n = len(arr)


    counter = Counter(arr)

  
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1

arr = [3,1,3,1,1]
ans = majorityElement(arr)
print("The majority element is:", ans)