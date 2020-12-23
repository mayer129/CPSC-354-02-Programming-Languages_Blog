# Issues with Concrete Syntax using `!` Symbol

When creating the negate function for my concrete syntax I ran into an issue. The symbol I wanted to use for the negate function was `!`. However, this produced some interesting results. It caused the parse to always fail. I tried many different inputs, and the result was the same.
```  
travismayer@Traviss-MBP Calculator2 % echo "!5" | ./TestNumbers  
echo "cpsc" | ./TestNumbers  

Parse              Failed...  

Tokens:  
[PT (Pn 0 1 1) (TV "cpsc")]  
syntax error at line 1, column 1 before `cpsc'  
```

Another error it gave me was:  
```
travismayer@Traviss-MBP Calculator2 % echo "2*!6" | ./TestNumbers  
echo "2*ls" | ./TestNumbers  
  
Parse              Failed...  
  
Tokens:  
[PT (Pn 0 1 1) (TI "2"),PT (Pn 1 1 2) (TS "*" 5),PT (Pn 2 1 3) (TV "ls")]  
syntax error at line 1, column 3 before `ls'  
```
After encountering this error, I tried using multiple other symbols for the negate symbol, and they all worked. I eventually went with the `-` symbol:  
```
travismayer@Traviss-MBP Calculator2 % echo "2*-6" | ./TestNumbers  
  
Parse Successful!  
  
[Abstract Syntax]  
  
Times (Num 2) (Negate (Num 6))  
  
[Linearized tree]  
  
2 * - 6  
```
After consulting Professor Kurz, he found that the also ran into the issue, but it was a different issue:
```
~/alexhkurz-at-github/programming-languages-2020/Local/Calculator3>echo "!2" | ./TestBang  
bash: !2: event not found  
``` 
He found that putting an extra space after the `!` fixed the issue. 
```
~/alexhkurz-at-github/programming-languages-2020/Local/Calculator3>echo "! 2" | ./TestBang  
```
Upon testing, I found that it also fixed the issue for me. We found that the different error message is likely due to the fact that he was using bash and I was using zsh. 