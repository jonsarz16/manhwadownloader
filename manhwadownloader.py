import streamlit as st
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import requests
import shutil

TIMEOUT = 2
firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    options=firefoxOptions,
    service=service,
)
# URL = "https://luminousscans.com/tomb-raider-king-chapter-252/"
URL = st.text_input('Input URL')
driver.get(URL)
all_links = driver.find_elements(By.TAG_NAME, 'img')
datalist = []
for links in all_links:
  x = links.get_attribute("src")
  if "252" in x:
    datalist.append(x)
output_folder = "/app/manhwadownloader"

for index, item in enumerate(datalist):
  response = requests.get(item)
  if response.status_code:
    fp = open(f"{output_folder}/{index + 1}.png", 'wb')
    fp.write(response.content)
    fp.close()

shutil.make_archive("trk", 'zip', output_folder)

with open("trk.zip", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="trk.zip",
            mime="application/zip"
          )