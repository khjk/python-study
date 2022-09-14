from selenium import webdriver
# extractors 폴더의 wwr파일에서 extract_wwr_jobs라는 함수를 import
from extractors.wwr import extract_wwr_jobs

browser = webdriver.Chrome()

browser.get("https://www.indeed.com/jobs?q=python&limit=50")

print(browser.page_source)
