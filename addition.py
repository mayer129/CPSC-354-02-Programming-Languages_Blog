'''
Addition  
`add :: NN -> NN -> NN`  
`add O n = n`  
`add (S n) m = S (add n m)`  
Example input: `add (S O) (S (S O))` 
'''

def add(num1, num2):
    return num1 if (num2 == 0) else 1 + add(num1, num2-1)




print(add(1,2))