
# Explanation of Assignment 1: Part 1: Natural Numbers vs Positive Numbers: Addition, Multiplication, Subtraction  
  
`data NN = O | S NN` Natural Number (NN) = 0 | Successor (S) of natural numbers is S  
`deriving (Eq,Show)`  
  
`-- addition`  
`add :: NN -> NN -> NN` Input: Natural Number, Natural Number; Ouput: Natural Number  
`add O n = n` Adding (0 + n) is still n  
`add (S n) m = S (add n m)` Adding ((n + 1) + m) is the same as (1 + (n + m))  
`-- add (S O) (S (S O))` Test input  
  
`-- multiplication`  
`mult :: NN -> NN -> NN` Input: Natural Number, Natural Number; Ouput: Natural Number  
`mult O n = O` Multiplying (0 * n) gives 0  
`mult (S O) n = n` Multiplying (1 * n) gives n  
`mult (S n) m = add m (mult n m)` Multiplying ((1 + n) * m) is the same as (m + (n * m))  
`-- mult (S O) (S (S O))` Test input  
  
`subtr :: NN -> NN -> NN` Input: Natural Number, Natural Number; Ouput: Natural Number  
`subtr O n = O` Subtracting (0 - n) gives 0, as it can only return a natural number (0+)  
`subtr n O = n` Subtracting (n - 0) obviously gives n  
`subtr (S n) (S m) = subtr n m` Subtracting ((n + 1) - (m + 1)) is the same as (n - m)  
`-- subtr (S (S O)) (S O)` Test input  
  
`data PN = I | T PN` Positive Number (PN) = 1 | Successor (T) of positive numbers is T  
`deriving (Eq,Show)`  
  
`-- addition of positive numbers`  
`-- use recursion over PN`  
`addP :: PN -> PN -> PN` Input: Positive Number, Positive Number; Ouput: Positive Number  
`addP I n = T n` Adding (1 + n) is the same as (n + 1)  
`addP (T n) m = T (addP n m)` Adding ((n + 1) + m) is the same as (1 + (n + m))  
`-- addP (T I) (T (T I))` Test input  
  
`multP :: PN -> PN -> PN` Input: Positive Number, Positive Number; Ouput: Positive Number  
`multP I n = n` Multiplying (1 * n) gives n  
`multP (T n) m = addP m (multP n m)` Multiplying ((1 + n) * m) is the same as (m + (n * m))  
`-- multP (T I) (T (T I))`  
  
`subtrNP :: NN -> PN -> NN` Input: Natural Number, Positive Number; Ouput: Natural Number  
`subtrNP O n = O` Subtracting (0 - n) gives 0, as it can only return a natural number (0+)  
`subtrNP n I = subtr n (S O)` Subtracting (n - 1) is the same as subtracting (n - (0 + 1))  
`subtrNP (S n) (T m) = subtrNP n m` Subtracting ((n + 1) - (m + 1)) is the same as (n - m)  
`-- subtrNP (S (S (S O))) (T I)` Testing Input  
  
As you can see, the difference in the natural number functions and the positive number functions is primarily in their base cases. That is why the function for natural numbers to positive numbers and visa versa is:  
`p2n :: PN -> NN` Input: Positive Number; Output: Natural Number  
`p2n I = (S O)` 1 is the same as (0 + 1)  
`p2n (T n) = S (p2n n)` (n+1) is the same as (1 + (n))  
`-- p2n (T (T I))` Test input  
  
`n2p :: NN ->PN` Input: Natural Number; Output: Positive Number  
`n2p (S O) = I` (0 + 1) is the same as 1  
`n2p (S n) = T (n2p n)` (n + 1) is the same as (1 + (n))  
`-- n2p (S (S (S O)))` Test Input  
  
You will find that these two functions basically do the same thing, just oppositely.  
  
At its core, this is grade school math, however the issue is knowing how to put this grade school math into code. After grasping these problems yourself you should be able to do most other functions that we used for this assigment.