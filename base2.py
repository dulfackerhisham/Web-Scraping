# working with regular expressions
import re

""".findall() to find any text within a string that matches a given regular expression"""
# h = re.findall("ab*c", "abdcABc") #its case sensitive
h = re.findall("ab*c", "abdcABc", re.IGNORECASE) #heres's the sollution
# print(h)

h = re.findall("a.c", "aacdcabc") # (.) to stand for any single charecter
# h = re.findall("a.c", "ac")
# print(h)

h = re.findall("a.*c", "abkjcbkjasc") #.* inside a regular expression stands for any character repeated any number of times. For instance, you can use "a.*c" to find every substring that starts with "a" and ends with "c", regardless of which letter—or letters—are in between
print(h)

""".search() to search for a particular pattern inside a string, it returns an object called MatchObject that stores different groups of data. This is because there might be matches inside other matches,
 and re.search() returns every possible result."""
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results.group()
print(match_results.group())


"""re.sub(), which is short for substitute, allows you to replace the text in a string that matches a regular expression with new text."""
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "sulthani", string)
# print(string)

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "sulthani", string)
print(string)