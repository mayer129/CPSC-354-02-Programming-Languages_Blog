# Abstract Reduction Systems and How to Make Sense of Them

Abstract reduction systems look very imposing in concept, however they can actually be fairly simple when one understands the concepts behind them.

We define an ARS (A,->) and let (a,b) range over A, the relation can be given with the following rules:  
`ba -> ab`  
`ab -> ba` 

`aaa ->`  
`aa -> b`  
`ab ->`  
`bb -> a`  

You can pretty much think of these rules as a list of key, value pairs with what is on the left of the `->` as the key, and what is on the right as the value.
As a side note, those keys that have nothing on the right can also be show as `-> []`, where `[]` is considered an empty word, with no value.
Now that we understand the rules, we just need to be given something to use them on. For that we would be given a set of letters, and asked to compute the normal form of them. Such as:  
Compute the normal form of:  
`bbbb`  

With no prior knowledge of this, this would probably be very intimidating. In actuality, you can treat it like a word search puzzle.  
`bbbb` is the array of letters, and the given rules are the words you are trying to find in the word search.
The only difference is that instead of crossing out the words you find, you simply swap them out with what they have on the right.
Meaning in the word search `bbbb`, you can find `bb` in it so you replace `bb` with `a`.
You now have `abb`. You can replace `bb` with `a` again.
Now you have `aa`, and if we look at the list of words to find again, we can see that `aa` reduces to `b`.
With `b` there are no other words we can find in the word search.  
Therefore we can see that the normal form of `bbbb` reduces to `b`.  
If we wanted to write code to solve this, what data type would you thing to use to hold the rules?  
As I explained above, these rules can be represented as a key, value pair. Therefore, logically, most people may think that a dictionary would be suitable.  
There is one issue with this that I will go into in the next blog. The issue is that the keys are not always unique.
