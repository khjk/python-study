from selenium import webdriver
from requests import get
import time
from bs4 import BeautifulSoup

# extractors 폴더의 wwr파일에서 extract_wwr_jobs라는 함수를 import
from extractors.wwr import extract_wwr_jobs

browser = webdriver.Chrome()

browser.get("https://www.indeed.com/jobs?q=python&limit=50")
time.sleep(1)

response = browser.page_source
soup = BeautifulSoup(response, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all('li', recursive=False)
results = []
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
            'link': f"https://kr.indeed.com{link}",
            'company': company.string,
            'location': location.string,
            'position': title.string
        }
        results.append(job_data)
