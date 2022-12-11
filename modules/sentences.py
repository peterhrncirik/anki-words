# For readability and progress bar
from rich import print
from rich.progress import track
import time

def find_sentences(word_translated, word):
    
    ptag = word_translated.find_all('p')

    for p in track(ptag[:10], description='Getting sentences...'):

        time.sleep(.3)
        word['sentences'].append(p.text.strip())
        