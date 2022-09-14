from selenium import webdriver
from requests import get
import time
from bs4 import BeautifulSoup


def get_page_count(keyword):
    browser = webdriver.Chrome()
    base_url = "https://www.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")
    time.sleep(1)

    response = browser.page_source
    soup = BeautifulSoup(response, "html.parser")
    pagination = soup.find("ul", class_="pagination-list")
    if pagination == None:
        return 1
    else:
        pages = pagination.find_all("li", recursive=False)
        count = len(pages)
    if count >= 5:
        return 5
    else:
        return count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    results = []
    for page in range(pages):
        browser = webdriver.Chrome()
        base_url = "https://www.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        browser.get(final_url)
        time.sleep(1)

        response = browser.page_source
        soup = BeautifulSoup(response, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all('li', recursive=False)
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName").find("a")
                location = job.find(
                    "div", class_="companyLocation").find("span")
                job_data = {
                    'link': f"https://kr.indeed.com{link}",
                    'company': company,
                    'location': location,
                    'position': title
                }
                results.append(job_data)
    return results


jobs = extract_indeed_jobs("python")
print(jobs)
