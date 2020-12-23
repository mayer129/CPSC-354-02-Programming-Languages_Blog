# My first thoughts on Assignment 1: Part 1: on the Provided Code
  
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

Upon seeing this provided code for assigment 1, my first thoughts on it was that it reminded me of what I learned last semester in Discrete Mathematics with Professor Moshier. When trying to solve these functions, it felt remarkabley similar to solving a proof. Therefore for solving a proof for `k` where `k` can be any number, we must first start at the `Basis` and prove that it also holds true for `0`  
`Basis: add O n = n`
Then, with the `Inductive Hypothesis` we suppose that it holds true for `k` for some `k ∈ N.`
Last, we must use the `Inductive Step` and show that the proof holds true for some `k next` which will prove that it holds true all natural numbers  
`Inductive Hypothesis: add (S n) m = S (add n m)`  
  
While we are really just programming recursively, and taking care of all the base cases and cases, thinking about it through a Discrete Mathematics viewpoint helped me to better understand what we were doing.

