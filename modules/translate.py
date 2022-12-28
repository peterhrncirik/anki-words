import re

# For readability and progress bar
from rich import print
from rich.progress import track
import time

def translate_word(soup, type):

    word = {
        'words': [],
        'verbs': [],
        'sentences': []
    }

    # regex
    pattern = '(d.{2} [A-ZäöüÄÖÜß].*)'
    
    # table with translations
    table = soup.find_all('tr', class_ = 'is-clickable')
    
    # split translation and append to list
    if type == 'noun':
        for w in track(table[0:2], description='Translating words..'):

            time.sleep(.3)

            found_words = re.findall(pattern, w.text)
            
            # split found words seperately and append them into list
            for _ in found_words:
                both_forms = _.split('\xa0pl.:')
                for form in both_forms:
                    word['words'].append(form.strip())
    
                
    elif type == 'verb':

        #FIXME: When it's verb, I need to split it somehow for sentences look up
        
        for w in track(table[0:1], description='Translating verbs....'):
            time.sleep(.3)
            word['words'].append(w.text.replace('\xa0', ''))
            all_forms = w.text.replace('\xa0', '').split()
            for form in all_forms:
                word['verbs'].append(form.strip())

           
    return word