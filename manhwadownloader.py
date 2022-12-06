import streamlit as st
import os, sys
URL = st.text_input('Input URL')
@st.experimental_singleton
def installff():
  os.system('sbase install geckodriver')
  os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

_ = installff()
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

browser.get(URL)
st.write(browser.page_source)









































# # URL = "https://luminousscans.com/tomb-raider-king-chapter-252/"
#
# driver.get(URL)
# all_links = driver.find_elements(By.TAG_NAME, 'img')
# datalist = []
# for links in all_links:
#   x = links.get_attribute("src")
#   if "252" in x:
#     datalist.append(x)
# output_folder = "/app/manhwadownloader"

# for index, item in enumerate(datalist):
#   response = requests.get(item)
#   if response.status_code:
#     fp = open(f"{output_folder}/{index + 1}.png", 'wb')
#     fp.write(response.content)
#     fp.close()

# shutil.make_archive("trk", 'zip', output_folder)

# with open("trk.zip", "rb") as file:
#     btn = st.download_button(
#             label="Download image",
#             data=file,
#             file_name="trk.zip",
#             mime="application/zip"
#           )