# Implementing Assignment 1: Part 1: Provided Code, Addition in Python

## Explanation
I found what we did for assignment 1 to be extremely interesting. In addition I found what we learned in it to be extremely useful throughout the course, even being used as a reference for other topics including some things on the final exam. I wanted to go back and review it, and also try and make it in another coding language. The language I chose was python. The next few blogs will be implementing other parts of the provided code in python, such as subtraction and multiplication. I feel like the code in python may be a lot easier for some people to understand as most people have at least an understanding of python, and it is similar to most conventional programming languages.
Something to note, is that while the addition, subtraction, multiplcation, etc were originally implemented using abstract syntax, the code I wrote in python uses concrete syntax.

## Reference Code
```
add :: NN -> NN -> NN
add O n = n
add (S n) m = S (add n m)
```
This was the reference code given for addition. To further clarify what I mean about abstract vs concrete syntax, the example input for this code is below:  
Example input:  
`add (S O) (S (S O))`  
It is using successor notation, similar to discrete math. If this was adapted to concrete syntax it would look like `add 1 2` which should give 3
## Writing my Code
When writing the code to adapt the reference code to python, I had been doing research for another blog post about the implementation of a factorial function in haskell vs python. I found an implementation of python code for it [here](https://www.geeksforgeeks.org/python-program-for-factorial-of-a-number/), which I was impressed by how consise it was. It is the second set of code on the link. Their implementation is using ternary operators. I attempted to do something similar with my code.

## My Code
```python
def add(num1, num2):
    return num1 if (num2 == 0) else 1 + add(num1, num2-1)
```
If we compare the two versions together, line 1 of the haskell code is basically line 1 of mine. Line 2 of the haskell code is everything before the else on line 2 of mine. Line 3 of the haskell code is everything after the else on line 2 of mine.  
The example input for this would be:  
`print(add(1,2))`  
Just as with the haskell code, the main thing that happens here is the recursion. I find this very similar to Abstract Reduction Systems, and what we learned about implementing addition or multiplication of numbers in them. It is basically just transferring the successors from one number to the other by recursion, until we finally hit the base case.

