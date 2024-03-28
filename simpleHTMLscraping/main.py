from bs4 import BeautifulSoup

# opening the html file
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

# # finding tags this is how we work with tags
#     soup = BeautifulSoup(content, 'lxml')
#     courses_html_tags = soup.find_all('h5') #find all method finds all of the tags instead find() method only looks for 1st instance
#     for course in courses_html_tags:
#         print(course.text) #text method brings the content only rather than printing out with the tags


"""Listing all courses along with its prices"""

# step 1 -> grabbing the cards in html file
soup = BeautifulSoup(content, 'lxml') #creating new instance of beautifulSoup
course_cards = soup.find_all('div', class_ = 'card') #here class_ we are refering to attribute of that div tag class. because we have class in python we need to write code in this format for class
# print(course_cards)
for course in course_cards:
    course_name = course.h5.text
    course_price = course.a.text.split()[-1]

    print(f'{course_name} costs {course_price}')