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
`def fac(n):`  
   `if n == 1:`  
      `return n`  
   `else:`  
      `return n * fac(n-1)`  
  
`print(fac(42))`  
  
The last line will just run the program with an input of 42. As you can see, it is a lot easier to do recursion in Haskell. Another example of the is the fibonacci sequence. An example of the haskell code is as short as:  
`fib 0 = 0`  
`fib 1 = 1`  
`fib n = fib (n-1) + fib (n-2)`