# Abstract Reduction Systems Continued

I decided to make a very basic program to calculate the normal forms for abstract reduction systems. I chose to code the program is python, as I am fairly familiar with the language.  
I chose to store the ARS rules in a dictionary as the rules are basically key value pairs. It was not until later that I realized that this would pose a problem.
I already explained how to think of an ARS in the previous blog, so if you have not read it, it will make it a lot easier to understand why I am doing what I am doing for my code.  
So I am trying to find the normal form of a given word which is stored in a string. So first what I did is to write a method to search the key value pairs for any pair that matched any part of the given string.  
I did this like so:  
[![Run on Repl.it](https://github.com/mayer129/CPSC-354-02-Programming-Languages_Blog/blob/main/runonreplit.svg)](https://repl.it/@mayer129/arspy#main.py)
```
def dict_contains(value, searchDict):
    for element in searchDict.keys():
        #print("Searching dictionary: " + element)
        if element in findNormal:
            return element
    return -1 
```
This code searches the dictionary for a given value, and returns the key if found. If not, it returns -1.
As simple as this is, its' actually the majority of the code. The rest of the code is:
```
def calculate():
    count = 0
    global findNormal
    while (True):
        count += 1
        temp = dict_contains(findNormal, ars_dict)
        if (count > 100):
            print("Looks like you're stuck in an infinite loop!\nBreaking...")
            break
        if (temp != -1):
            print(findNormal)
            print("Changing: '" + temp + "' To: '" + ars_dict.get(temp) + "'")
            findNormal = findNormal.replace(temp, ars_dict.get(temp), 1)
        else:
            print("Normal form: '" + findNormal + "'")
            break
```
This basically just runs the code until either the dict_contains function returns -1 which means that the dictionary keys can no longer be found in the word, or until the iterations reaches > 100. I implemented the > 100 break because there are many cases where rules cause the ARS to be nonterminating and therefore nonconfluent, which would make the function get stuck in an infinite loop. Besides the issue of the infinite loop there are several other problems this code has. The code has an issue in that the order of the keys stored in the dictionary matters, as that is the order it will search for the terms in. I have found for several different example ARS's that I need to order specific rules in a specific order for it to successfully return the correct normal form. Another key issue is the issue I mentioned at the end of the last blog. The key's are not always unique. When searching through the keys in the dict_contains function, it will start in order, and then return the key. When the main funtion calculate uses that key to get the value, it actually is not search in order. Meaning if you have an ARS such as:
```
ars_dict = {
"aaa": "",
"aa": "b",
"ab": "",
"bb": "a",
"ba": "ab",
"ab": "ba"
}
```
When it runs this code if the normal form ever contains `ab`, the dict_contains function will search it, find the key `ab` which would give the value of `""`, and then send the key back to the calculate function. The calculate function will use the key `ab` and return the value `ba` instead for some reason, as it seems .get does not search in order.  
This is a hard issue to resolve as dictionaries cannot be accessed by index. Meaning that I probably would have to use a different way to store the data. One way I though of doing this would be to make an array of arrays, where 0 stores the key and 1 stores the value. Or I could make an array where odd numbers store the key (ie. 1,3,5,7) and even numbers store the value (ie. 2,4,6,8). There may be much better ways to store this data, and I may be overthinking this, however I am not very experienced in this area, and this is simply what I came up with.  

I spoke to Professor Kurz about this, and from my understanding, a way to resolve all of the issues mentioned here would be to treat the ARS as a graph, and use depth first search.
        