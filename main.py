from requests import get
from bs4 import BeautifulSoup
# extractors 폴더의 wwr파일에서 extract_wwr_jobs라는 함수를 import
from extractors.wwr import extract_wwr_jobs

jobs = extract_wwr_jobs("python")
print(jobs)
