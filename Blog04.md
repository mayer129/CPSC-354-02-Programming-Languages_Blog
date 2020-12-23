# Basic Haskell Program vs Python Program:  
  
Haskell has some advantages to other common languages, particularly when it comes to recursion.  
Create a file called `fac.hs` and put the below code in it:  
`fac 0 = 1`  
`fac n = n * fac (n-1)`  
  
Then in the terminal enter:  
`ghci` to enter into the haskell console using the shortened alias we made earlier  
`:load fac.hs` to load the file we just created  
`fac 42` to run the program with an input of 42  
  
  
Meanwhile in python we would create a file called `fac.py` and put the following code in it:  
```
def factorial(n): 
    if n < 0: 
        return 0
    elif n == 0 or n == 1: 
        return 1
    else: 
        fact = 1
        while(n > 1): 
            fact *= n 
            n -= 1
        return fact  
```
  
`print(fac(42))`  
[Credit for above code](https://www.geeksforgeeks.org/python-program-for-factorial-of-a-number/)
  
The last line will just run the program with an input of 42. As you can see, it is a lot easier to do recursion in Haskell. Another example of the is the fibonacci sequence. An example of the haskell code is as short as:  
`fib 0 = 0`  
`fib 1 = 1`  
`fib n = fib (n-1) + fib (n-2)`