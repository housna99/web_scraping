import time
from bs4 import BeautifulSoup
from prometheus_client import Info
import requests
import urllib
#import urllib3.request


html_text= requests.get('https://fr.indeed.com/jobs?q=python&l=France&vjk=9c77a41a4206b998').text
soup= BeautifulSoup(html_text,'lxml')
jobs= soup.find_all('div', class_='job_seen_beacon')

def python_jobs():
    file = open('C:/Users/HOSNA/OneDrive/personnel projects/results/new_file.txt', 'a+b')

    for job in jobs :
        
        date_published=job.find('span', class_='date')
        #print(date_published)
        if '30+' not in date_published.text:
            job_title=job.find('h2',class_='jobTitle')
            company_name= job.find('span', class_='companyName').text
            company_location= job.find('div', class_='companyLocation').text.replace(' ','')
            infos= job.find('div', class_="job-snippet")
            
            print(f"Job title : {job_title.text}")
            print(f"Company Name : {company_name.strip()}")
            print(f"Location : {company_location.strip()}")
            print("--")
            print(infos.li.text)
            print("**")
            file.write(job_title.text.encode()+ b'::\n'+company_name.strip().encode()+b'\n'+company_location.strip().encode()+b'\n'+b'\r')

            
            
if __name__== '__main__':
    while True:
        python_jobs()
        print("waiting & saving...")
        time.sleep(60*1)
        
# with open('index.html','r') as html_file:
#     content=html_file.read()
#     #print(content)
#     soup= BeautifulSoup(content,'lxml')
#     #print(soup.prettify())
#     #grab informations 
#     courses_cards= soup.find_all('div', class_='card')
#     #print(courses_cards)
#     for course in courses_cards:
#         course_name=course.h5.text
#         course_price=course.a.text.split()[-1]

#         print(f'{course_name} costs {course_price}')
    


