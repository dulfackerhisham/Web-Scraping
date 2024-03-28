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
import time

print('Put some Skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    # step 1 ->  get the url of the website
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="
    page = requests.get(url)

    # step 2 -> creating beautiful soup instance and finding setting up tag
    soup = BeautifulSoup(page.content, 'lxml')
    # step 2.1 -> finding the tag which all the jobs are under
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    #step 2.2 -> finding company name & skills with the jobs tag
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company_name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'More info: {more_info} \n')
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)