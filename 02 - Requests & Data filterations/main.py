# # Check if the request was successful
# if response.status_code == 200:
#     # Pass the content of the response to BeautifulSoup
#     soup = BeautifulSoup(response.content, 'lxml')
#     # Now you can work with the soup object
# else:
#     print('Failed to retrieve the webpage:', response.status_code)

"""search for job ads
    Bring jobs from specific website 
    those main skill requirement is python and also only posted few days ago"""

from bs4 import BeautifulSoup
import requests

# step 1 ->  get the url of the website
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="
page = requests.get(url)

# step 2 -> creating beautiful soup instance and finding setting up tag
soup = BeautifulSoup(page.content, 'lxml')
# step 2.1 -> finding the tag which all the jobs are under
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
#step 2.2 -> finding company name & skills with the jobs tag
for job in jobs:
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        print(f'''
        Company Name: {company_name}
        Required Skills: {skills}
        ''')