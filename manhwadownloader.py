import streamlit as st
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import shutil
import os, sys



@st.experimental_singleton
def installff():
  os.system('sbase get geckodriver')
  os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

_ = installff()

opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)
URL = st.text_input('Input URL')

if URL:
    
  browser.get(URL)

  all_links = browser.find_elements(By.TAG_NAME, 'img')
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