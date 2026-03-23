# this is the library for stand regular expression in python, and is used to match patterns in strings and follow a complex map
import re
# the prefix of r stand for raw string, the "^" and "$" are used to indicate the start and end of the string, respectively.
# the $ is used to indicate the end of the string, ensuring that the entire string must match the pattern.
expression = r"^c(erthans|irth|o(ire|r(anar|mallen)))$"
words = ["certhans", "cirth", "coire", "coranar", "cor", "cirtha", "cormallen"]

def validate_words():
    for word in words:
        # the re.match() function is used to check if the word matches the regular expression pattern defined in the expression variable 
        # it returns a match object if the word matches the pattern, if it match it will return "Yes" otherwisse it will return "NO"
        if re.match(expression, word):
            print("YES")
        else:
            print("NO")

validate_words()