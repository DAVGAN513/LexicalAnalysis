# LexicalAnalysisz
# DESCRIPTION

The language I chose consists of a finite one about some specific words that are:

    certhans
    cirth
    coire
    coranar
    cormallen

The objective of this lexical analyzer is to determine a given input string belongs to this languague or not.
For this problem can be modeled using a finite automata, which are models used to recognize patterns in strings the Finite Automata that I chose was a DFA
I chose the DFA because esch input symbol leads to exactly one state, for that helps to making it predictable,efficient, and also easy to implement for a finite set of known words.
So for this problem that have the language that only consists of five valid words, the DFA is sufficient to represent all valid transitions without ambiguity. 

# MODELS

The alphabet used in this language is: 

    ∑ = a, c, e, h, i, l, m, n, o, r, s, t
    
Any character outside this alphabet is rejected, so the DFA was designed that each word follow a unique path from the initial state to an accepting state, if theres at any point the input deviates from this paths the string will be rejected

<img width="900" height="1600" alt="image" src="https://github.com/user-attachments/assets/37eda190-a3ee-454e-830b-82fa570dda4c" />


# IMPLEMENTATION

For my implementation of the lexical analysis it was made in python, i used the "re" library to work with regular expressions this helps to match patterns in strings and follow a complex map, so for this is like each input string is processed character by character following a deterministic path defined by the pattern wivh ensure efficience.
Also the program is based on a regular expression that represent all the valid words in the language and its defined as: 


    expression = r"^c(erthans|irth|o(ire|r(anar|mallen)))$"

On this expression help to the pattern to ensure this: 

1- The string only can start with the character "c"

2- It must continue with one of the valid sequences: erthans, irth, oire, oranar, ormallen

3- Now for the symbol of "^" and "$" helps to to the start and end, enforcing that the entire string must match exactly, preventing an extra or missing character.

Also on the program theres some words to test them with teh list of strings defined:

    words = ["certhans", "cirth", "coire", "coranar", "cor", "cirtha", "cormallen"]

Also on the program theres a function that iterates over each word and checks if it matches woth the defined regular expressions
If the string matches the pattern the program will print "YES" if there is no matching word it will print "NO"

EXAMPLES OF THE INPUTS AND OUTPUTS ARE:

    cirth ==> YES
    coire ==> YES
    coranar ==> YES
    certhans ==> YES
    cor ==> NO 
    cirtha ==> NO

For this results confirm that the analyzer correctly identifies valid words from the language and rejects the invalid ones

# ANALYSIS

The tine Complexity for this implementation is O(n) where where the n is yhe length of the string to be processed.
for any input string of length n, the engine starts at the initial state, for each character in the string it moves to exactly one next state. Also the program processes each character once, making it more efficient and scalable 

And now i´m going to explain why I chose the DFA because the language consists of a finite set of predefined words where each input followa an unique and well defined path. So for this compared to an NFA the DFA is simpler to implement and more efficient for this type of problems, besides a NFA would introduce unnecesary complexity and to be converted into a DFA.

# REFERENCES 
https://www.cs.rochester.edu/u/nelson/courses/csc_173/fa/fa.html
https://www.geeksforgeeks.org/python/python-regex/
