#Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

def countDigitOne(n):
    countr = 0;
    for i in range(1, n + 1):
        str1 = str(i);
        countr += str1.count("1");
 
    return countr;
 
n = 13;
print(countDigitOne(n));
