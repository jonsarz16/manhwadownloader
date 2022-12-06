import streamlit as st

# URL = "https://luminousscans.com/tomb-raider-king-chapter-252/"
URL = st.text_input('Input URL')

!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import shutil

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',options=options)
wd.get(URL)
# wd.page_source
all_links = wd.find_elements(By.TAG_NAME, 'img')

datalist = []
for links in all_links:
  x = links.get_attribute("src")
  if "252" in x:
    datalist.append(x)

output_folder = "/content/saved"

for index, item in enumerate(datalist):
  response = requests.get(item)
  if response.status_code:
    fp = open(f"{output_folder}/{index + 1}.png", 'wb')
    fp.write(response.content)
    fp.close()

shutil.make_archive("trk", 'zip', output_folder)