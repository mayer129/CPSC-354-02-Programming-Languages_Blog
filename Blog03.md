
# Understanding Assignment 1: Part 1: on the Provided Code

`data NN = O | S NN`  
`deriving (Eq,Show)`  
  
Addition  
`add :: NN -> NN -> NN`  
`add O n = n`  
`add (S n) m = S (add n m)`  
Example input: `add (S O) (S (S O))`  
  
Multiplication  
`mult :: NN -> NN -> NN`  
`mult O n = O`  
`mult (S O) n = n`  
`mult (S n) m = add m (mult n m)`  
Example input: `mult (S O) (S (S O))`  

Subtraction
`subtr :: NN -> NN -> NN`  
`subtr O n = O`  
`subtr n O = n`  
`subtr (S n) (S m) = subtr n m`  
Example input: `subtr (S (S O)) (S O)`

For someone not well versed in Haskell, this code undoubtabley looks imposing. If asked to extend this code to positive numbers, and even convert between the two they might not know where to start. So I'll do my best to explain this code, to help you understand what to do for the rest.

## Addition
`add :: NN -> NN -> NN`  
This just means that the program is taking in a natural number, another natural number, and returning a natural number. In swift it could look like: 
Now we just need to look for the base cases for addition.  
That is just if we are adding a number to 0.  
`add O n = n` 
Every other case can be represented as adding a number to 1.
`add (S n) m = S (add n m)`
We are basically just saying that ((1 + n) + m) is the same as (1 + (n + m)). Anyone familiar with discrete math can see that this is just the law of associativity. What we are doing is simply reducing the numbers until we hit the base case.

## Multiplication
`mult :: NN -> NN -> NN`
This is the same as for addition
Now we just need to look for the base cases for multiplication.
One base case is if we are multiplying n by 0, which would just be 0.  
`mult O n = O`
The next base case would be if we are multiplying by n by 1 (the successor of 0), which would just be n.
`mult (S O) n = n`
Now that all the base cases are out of the way, we just need a line of code which can take care of every other case.
`mult (S n) m = add m (mult n m)`

## Subraction
`subtr :: NN -> NN -> NN`
This is the same as for addition
Now we just need to look for the base cases for subtraction.
As a reminder, we are only dealing with natural numbers here. Meaning that 0 is the smallest number possible. That means that 0 - n is still 0, no matter what n is. This is the first base case.  
`subtr O n = O`
Now we can just look at it the other way around. n - 0. Which is still n.
`subtr n O = n`
All that is left is to code recursively.
`subtr (S n) (S m) = subtr n m`
All this means is that (1 + n) - (1 + m) is the same as (n) - (m). This takes care of all other cases, and will reduce the code to hit the base cases again.

This code may still be a bit foreign, but it has very similar patterns to each other, and should be thought out using basic mathematic reasoning before trying to code it. It is much simpler that way.