'''
Subtraction
`subtr :: NN -> NN -> NN`  
`subtr O n = O`  
`subtr n O = n`  
`subtr (S n) (S m) = subtr n m`  
Example input: `subtr (S (S O)) (S O)`
'''

def subtr(num1, num2):
    if (num1 == 0): return 0
    return num1 if (num2 == 0) else subtr(num1-1, num2-1)




print(subtr(2,1))