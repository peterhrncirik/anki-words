# For readability and progress bar
from rich import print
from rich.progress import track
import time

def find_sentences(word_translated, word):
    print(word_translated)
    ptag = word_translated.find_all('p', class_ = 'rLinks')

    for p in track(ptag[:10], description='Getting sentences...'):
        time.sleep(.3)
        

        # print(p.text.strip())
        word['sentences'].append(p.text.strip())
        