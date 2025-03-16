"""
A pandigital number is one that has its digits from 1 to 9 occuring only once (they do not have the digit 0).

The number 169, is the first pandigital square, higher than 100, having its square root, 13, pandigital too.

The number 1728 is the first pandigital cubic, higher than 1000, having its cubic root, 12, pandigital too.

Make the function pow_root_pandigit(), that receives three arguments:

a minimum number, val

the exponent of the n-perfect powers to search, n

k, maximum amount of terms that we want in the output

The function should output a 2D-array with an amount of k pairs of numbers(or an array of an only pair if we have this case). 

Each pair has a nth-perfect power pandigital higher than val with its respective nth-root that is pandigital, too.
"""

def pow_root_pandigit(val, n, k):
    def is_pandigital(num):
        num_str = str(num)
        return '0' not in num_str and len(set(num_str)) == len(num_str)
    
    solutions = []
    x = int(val ** (1/n))  

    while len(solutions) < k:
        num = x ** n  
        if num > val and is_pandigital(num) and is_pandigital(x): 
            solutions.append([x, num])
        x += 1  

    return solutions

print(pow_root_pandigit(388, 2, 3))
