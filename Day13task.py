#Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
import re
def string_match(string):
    pattern = re.compile("[A-Za-z0-9]+")
    if pattern.fullmatch(string)is not None:
        print("Found match: " + string)
    else:
        print("No match")
print(string_match("HelloWorld123"))
print(string_match("Hello123Python"))


#Write a Python program that matches a word containing 'ab'.
import re
def string_match(string):
    patterns="ab*?"
    if re.search(patterns, string):
        return("Found a match")
    else:
        return("Not matched")
print(string_match("arabian"))
print(string_match("abc"))
print(string_match("bbca"))


#Write a Python program to check for a number at the end of a word/sentence.
import re
def number_match(string):
    pattern=re.compile(r".*[0-9]$")
    if pattern.match(string):
        return("Found a match")
    else:
        return("Not matched")
print(number_match("helloworld123"))
print(number_match("python123world"))
print(number_match("bestenlist30"))


#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
import re
results = re.finditer(r"([0-9]{1,3})", "Hey Hello 123 95 468 5678 890 going")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))


#Write a Python program to match a string that contains only uppercase letters
import re
def match_string(string):
    pattern=re.compile("[A-Z]+$")
    if re.search(pattern, string):
        return("Found a match")
    else:
        return("not matched")
print(match_string("ABCDEFG"))
print(match_string("AcghhEF"))
print(match_string("abcdefg"))


