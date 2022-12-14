from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input('What do you want to search?')

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr

# 개행문자때문에 파일오픈 형식 지정
file = open(f"{keyword}.csv", "w", encoding="utf-8")
file.write("Position,Company,Location,URL")

for job in jobs:
    file.write(
        f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()
