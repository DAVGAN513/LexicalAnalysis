# LexicalAnalysisz
DESCRIPTION

The language I chose consists of a finite one about some specific words that are [certhans, cirth, coire, coranar, cormallen] the objective is to recognize patterns within input string about of character from the alphabet.
The modeling technique I decided to use was a Deterministic Finite Automaton (DFA) I chose this one because it provides a direct an efficient way to map the transitions of the words.

<img width="900" height="1600" alt="image" src="https://github.com/user-attachments/assets/37eda190-a3ee-454e-830b-82fa570dda4c" />


IMPLEMENTATION

For my implementation of the lexical analysis, I followed the regular expressions defined in the file, in this one you need to provide the input in the format of a string like cirth, and then the program will return "YES" if the string is accepted by the DFA or it will return "NO" if the string is not part of the language or for this words. 
EXAMPLES OF THE INPUTS AND OUTPUTS ARE:
cirth ==> YES
coire ==> YES
coranar ==> YES
certhans ==> YES
cor ==> NO 
cirtha ==> NO

ANALYSIS

The complexity of this model is O(n) where the n is yhe length of the string to be processed.
for any input string of length n, the engine starts at the initial state, for each character in the string it moves to exactly one next state.
I used the python´s "re" library this one helps to compiles the expression into highly optimized transition table and is used to match patterns in strings and follow a complex map.

REFERENCES 
https://www.cs.rochester.edu/u/nelson/courses/csc_173/fa/fa.html
https://www.geeksforgeeks.org/python/python-regex/

