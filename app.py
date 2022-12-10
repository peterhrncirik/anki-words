import requests
import argparse
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import unicodedata
from os import startfile

# For readability and progress bar
from rich import print
from rich.progress import track

# Webbrowser testing
import webbrowser

# Usage
parser = argparse.ArgumentParser(description='word')
parser.add_argument('-w', default='car', nargs='*', help='Word you wish to translate', type=str)
parser.add_argument('-t', default='noun', help='Type of word - noun or verb?', type=str)
args = parser.parse_args()

# Main cotainer
word = {
    'words': [],
    'sentences': [],
}

def extract_word(type):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}

    if type == 'noun':
        url = f'https://dict.leo.org/german-english/{" ".join(args.w)}?side=left'
    else:
        url = f'https://dict.leo.org/german-english/{" ".join(args.w)}'

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

def translate_word(soup):


    # regex
    pattern = '(d.{2} [A-ZäöüÄÖÜß].*)'
    
    # table with translations
    table = soup.find_all('tr', class_ = 'is-clickable')
    
    # split translation and append to list
    if args.t == 'noun':
        for w in track(table[0:2], description='Translating words..'):

            time.sleep(.3)

            found_words = re.findall(pattern, w.text)
            for _ in found_words:
                word['words'].append(_.split('\xa0pl.:'))
                
    elif args.t == 'verb':
        
        for w in track(table[0:2], description='Translating verbs....'):
            time.sleep(.3)
            word['words'].append(w.text.replace('\xa0', ''))

           
    return

def find_sentences(word_translated):
    
    ptag = word_translated.find_all('p')

    for p in track(ptag[:10], description='Getting sentences...'):

        time.sleep(.3)
        word['sentences'].append(p.text.strip())
    
def open_images(word):
    
    print('Loading images...')
    url = f'https://duckduckgo.com/?q={word}&t=newext&atb=v346-1&iar=images&iaf=type%3Agif&iax=images&ia=images'
    firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    firefox.open_new_tab(url)

translate_word(extract_word(args.t))

if args.t == 'noun':
    find_sentences(extract_sentence(word['words'][0][0]))
else:
    find_sentences(extract_sentence(' '.join(args.w)))
    
open_images(' '.join(args.w))
print(word)

def export(d):
    print('Saving file...')
    
    with open('word.txt', 'w') as file:

        for words in d.get('words'):
            
            for word in words:
                
                if args.t == 'noun':
                    file.write(word.strip())
                    file.write('\n')
                else:
                    file.write(word)


        file.write('\n')
        file.write('SENTENCES:')
        file.write('\n')
        file.write('\n')
        for sentences in d.get('sentences'):
            
            for s in sentences:
                
                file.write(s)
                if s == '.':
                    file.write('\n')       
    
    startfile('word.txt')
        
export(word)