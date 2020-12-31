# Implementing Assignment 1: Part 1: Provided Code, Multiplication in Python

## Explanation
For this blog post, I will be continuing from what I did in the previous blog. I will attempt to implement a python version of the code given in assignment 1 on multiplication. Again, my version uses concrete syntax, while the haskell version uses abstract syntax.

## Reference Code
```
mult :: NN -> NN -> NN 
mult O n = O
mult (S O) n = n
mult (S n) m = add m (mult n m)  
```
This was the reference code given for multiplication. To further clarify what I mean about abstract vs concrete syntax, the example input for this code is below:  
Example input:  
`mult (S O) (S (S O))`  
It is using successor notation, similar to discrete math. If this was adapted to concrete syntax it would look like `mult 1 2` which should give 2

## Writing my Code
I again tried to code this python program with a similar coding style of what I talked about in the previous blog post. As we can see, it is basically just if statements in python, which isn't as clear in the haskell code. For this program, just as with the haskell, to do multiplication it requires addition. So it will call the addition function that we have previously written. If you want to test it out yourself, you will need to have both of the functions in your file for it to work.

## Previous Addition Code
```python
def add(num1, num2):
    return num1 if (num2 == 0) else 1 + add(num1, num2-1)
```
## My Code
```python
def mult(num1, num2):
    if (num1 == 0): return 0
    return num2 if (num1 == 1) else add(num2, mult(num1-1, num2))
```
If we compare the two versions together, line 1 of the haskell code is basically line 1 of mine. Line 2 of the haskell code is line 2 of mine. Line 3 of the haskell code is everything before the else on line 3 of mine. Line 4 of the haskell code is everything after the else on line 3 of mine.
The example input for this would be:  
`print(mult(1,2))`  
Again, like the haskell code, we must first take care of all base cases for subtraction. This is just simple math. Any (n)umber * 0 = 0. Any n(umber) * 1 = n. All the rest of the code is just reducing it using addition. Let us walk through the steps:
Given an input of:
`print(mult(4,2))`
What it looks like: (4*2)
Steps:
1. Defaults to else: 2 + (3*2)
2. Defaults to else: 2 + 2 + (2*2)
3. Defaults to else: 2 + 2 + 2 +(1*2)
4. As num1 == 1, return num2.  
 num2 == 2, so we get 2 + 2 + 2 + 2  
 which gives = 8  
Most people are not very experienced with stuff like this, so it is hard to grasp at first, but it really isn't much work. We only need to implement a few steps, which can end up taking care of all numbers.
All multiplication is fundamentally addition, so we just have the addition function we wrote do all the work for us.