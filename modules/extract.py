import requests
from bs4 import BeautifulSoup
import webbrowser

def extract_word(word, type, to_eng):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}
    url = f'https://dict.leo.org/german-english/{" ".join(word)}{"?side=left" if type == "noun" and not to_eng else ""}'
    firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # firefox.open_new_tab(url)
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def extract_sentence(word):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}
    url = f'https://www.satzapp.de/saetze/?w={word}'
    firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # firefox.open_new_tab(url)
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup