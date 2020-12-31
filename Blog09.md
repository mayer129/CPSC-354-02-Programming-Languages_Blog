# Implementing Assignment 1: Part 1: Provided Code, Subtraction in Python

## Explanation
For this blog post, I will be continuing from what I did in the previous blog. I will attempt to implement a python version of the code given in assignment 1 on subtraction. Again, my version uses concrete syntax, while the haskell version uses abstract syntax.

## Reference Code
```haskell
subtr :: NN -> NN -> NN  
subtr O n = O
subtr n O = n
subtr (S n) (S m) = subtr n m
```
This was the reference code given for subtraction. To further clarify what I mean about abstract vs concrete syntax, the example input for this code is below:  
Example input:  
```haskell
subtr (S (S O)) (S O)
``` 
It is using successor notation, similar to discrete math. If this was adapted to concrete syntax it would look like `subtr 2 1` which should give 1

## Writing my Code
I again tried to code this python program with a similar coding style of what I talked about in the previous blog post. As we can see, it is basically just if statements in python, which isn't as clear in the haskell code.

## My Code
[![Run on Repl.it](https://github.com/mayer129/CPSC-354-02-Programming-Languages_Blog/blob/main/runonreplit.svg)](https://repl.it/@mayer129/subtractionpy#main.py)
```python
def subtr(num1, num2):
    if (num1 == 0): return 0
    return num1 if (num2 == 0) else subtr(num1-1, num2-1)
```
If we compare the two versions together, line 1 of the haskell code is basically line 1 of mine. Line 2 of the haskell code is line 2 of mine. Line 3 of the haskell code is everything before the else on line 3 of mine. Line 4 of the haskell code is everything after the else on line 3 of mine.
The example input for this would be:  
```python
print(subtr(2,1))
```
Again, like the haskell code, we must first take care of all base cases for subtraction. And since this is using natural numbers, the smallest number possible is 0. Once the base cases are taken care of, every single other case can be taken care of by the else statement, which will slowly reduce the numbers until one of the base cases are hit.
