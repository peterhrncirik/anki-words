import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from rich.progress import track


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_executable = Service(executable_path='C:\Program Files (x86)\chromedriver.exe', log_path='NUL')
driver = webdriver.Chrome(service=chrome_executable, options=chrome_options)

def extract_sentences(word_translated, word):

    url = f'https://www.satzapp.de/saetze/?w={word_translated}'
    driver.get(url)

    time.sleep(5)

    consent_btn = driver.find_element(By.CLASS_NAME, 'fc-primary-button')
    consent_btn.click()

    sentences = driver.find_elements(By.CSS_SELECTOR, 'p')

    for i, sentence in track(enumerate(sentences[:15]), description='Getting sentences..'):
        time.sleep(.3)
        
        word['sentences'].append(sentence.text.strip())

