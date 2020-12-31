'''
Multiplication  
`mult :: NN -> NN -> NN`  
`mult O n = O`  
`mult (S O) n = n`  
`mult (S n) m = add m (mult n m)`  
Example input: `mult (S O) (S (S O))`  
'''

def add(num1, num2):
    return num1 if (num2 == 0) else 1 + add(num1, num2-1)


def mult(num1, num2):
    if (num1 == 0): return 0
    return num2 if (num1 == 1) else add(num2, mult(num1-1, num2))



print(mult(4,2))