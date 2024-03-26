from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)
print(page) #HTTPResponse object

"""To extract the HTML from the page, first use the HTTPResponse object’s .read() method,
 which returns a sequence of bytes.
 Then use .decode() to decode the bytes to a string using UTF-8:"""

html_bytes = page.read()
# print(html_bytes)
html = html_bytes.decode("utf-8")
print(html)

# Extract Text From HTML With String Methods
# .find() returns the index of the first occurrence of a substring, you can get the index of the opening <title> tag by passing the string "<title>" to .find():
title_index = html.find("<title>") #.find() to search through the text of the HTML for the <title> tags and extract the title of the web page.
# print(title_index)

""" you’ll extract the title of the web page that you requested in the previous example. If you know the index of the first character of the title and the index of the first character of the closing </title> tag,
 then you can use a string slice to extract the title."""

# You don’t want the index of the <title> tag, though. You want the index of the title itself. 
start_index = title_index + len("<title>")
print(start_index)
end_index = html.index("</title>")

title = html[start_index:end_index]
print(title)

# Real-world HTML can be much more complicated and far less predictable than the HTML on the Aphrodite profile page