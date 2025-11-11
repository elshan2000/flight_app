# https://github.com/password123456/setup-selenium-with-chrome-driver-on-ubuntu_debian?tab=readme-ov-file

#====windows================
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#===========================
import pytz
from datetime import datetime
import requests
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# (w_1) from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = Options()
#options.add_argument('--headless=new')  # modern headless mode
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/122.0.0.0 Safari/537.36")

options.page_load_strategy = "eager"

# (w_2) driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#CHROMEDRIVER_PATH = r"C:\Users\Lenovo\Python_app\chromedriver-win64\chromedriver.exe"
CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

'''
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
})

'''

#======================================
def to_english(input_str):
    persian_numbers = "۰۱۲۳۴۵۶۷۸۹"
    arabic_numbers = "٠١٢٣٤٥٦٧٨٩"
    english_numbers = "0123456789"

    translation_table = str.maketrans(
        persian_numbers + arabic_numbers,
        english_numbers * 2
    )

    return input_str.translate(translation_table)

#======================================
# Telegram bot API token
api_token = '7533520720:AAFZHJr6VKoQBej6gqF1nDCZEgeY4CZSTJg'
url = f"https://api.telegram.org/bot{api_token}/sendMessage"
# Telegram chat ID (can be a user or a group)
client_id = 'client_id' # client_id
elshan_id = '142629922' # elshan
group_id = '-4713480856' # group

#===========================================================
# don't use
#response = requests.get(url, params=params, verify=False, proxies=proxies)
proxies = {
    'http': 'http://192.168.62.37:3128',
    'https': 'http://192.168.62.37:3128',
}

#============================================================
# Print the date and time
tehran_tz = pytz.timezone('Asia/Tehran')
now_utc = datetime.now(pytz.utc)
now = now_utc.astimezone(tehran_tz)
now.strftime("%Y-%m-%d %H:%M:%S")
#=============================================================

print("start")
url_1="https://safarmarket.com/flights/cTBZ-cIST/2025-06-02/0/allclasses/1adults/0children/0infants"
url_2="https://www.pateh.com/flightsearch/TBZ-IST/?departing=1404%2F01%2F17&returning=&roundTrip=false&flightType=in&adults=1&children=0&infants=0"
url_3=""

#driver.set_page_load_timeout(10)  ##don't use

#time.sleep(random.uniform(1, 3))  # slow down to avoid bot detection
driver.get(url_1)
print("Page loaded!")
time.sleep(30)
page_source = driver.page_source

soup = BeautifulSoup(page_source, "html.parser")
divs = soup.find_all("div", attrs={"class": "owl-item active"})



#==========================
message_client = f"""
====================================
{now}
My dear Clinet 

Every moment feel free.  \n\n
"""
cond = 0
message = ""
for div in divs:
    date = div.find('div', {'data-date': True})['data-date']
    persian_date = div.find_all('div')[1].text.strip()
    million_value = div.find_all('div')[2].text.strip().encode('utf-8').decode('utf-8')

    message_add = f"""
    Date: {date}
    Persian Date: {persian_date}
    Min Price (milion_toman):  {million_value} \n
    """
    message = message + message_add 
  # Print the extracted values
    print(f"Date: {date}")
    print(f"Persian Date: {persian_date}")
    print(f"Min Price: ﻢﯿﻠﯾﻮﻧ ﺕﻮﻣﺎﻧ {million_value}")
    print("=======================")

    if million_value == "--" :
       continue
    elif float(to_english(million_value)) < float(7) :
       cond = 1
  
#parent_div = driver.find_element(By.CLASS_NAME, "owl-stage")
#sub_divs = parent_div.find_element(BY.CLASS_NAME, "active")
#for sub_div in sub_divs:
#    print(sub_div.get_attribute("outerHTML"))
full_message = message_client + message

def tel_bot(chat_id):
	params = {
    		'chat_id': chat_id,
    		'text': full_message
		 }
	response = requests.get(url, params=params, verify=False)
	if response.status_code == 200:
    		print("Message sent successfully!")
	else:
    		print("Failed to send message:", response.status_code)
#==========================
tel_bot(group_id)
if cond == 1 :
    tel_bot(elshan_id)
    tel_bot(client_id)


	
#driver.quit()




if driver.service.process and driver.service.process.poll() is None:
    try:
        driver.quit()
    except Exception as e:
        print(f"Error while quitting driver: {e}")

