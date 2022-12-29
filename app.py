import argparse
from modules import extract_sentences, extract_word, images, export, translate


# Usage
parser = argparse.ArgumentParser(description='Get noun/verb translation')
parser.add_argument('word', nargs='*', help='Word you wish to translate', type=str)
parser.add_argument('-t', default='verb', help='Type of word - noun or verb?', type=str)
parser.add_argument('-eng', default=False, help='Translate from German to English', type=bool)

args = parser.parse_args()

# Parser
word_to_translate = args.word
word_type = args.t
to_eng = args.eng


# Open website, get HTML
soup = extract_word.extract_word(word=word_to_translate, type=word_type, to_eng=to_eng)

# Translate word, return dict
translated_word = translate.translate_word(soup=soup, type=word_type)

# Find example sentences based on type
if word_type == 'noun' and to_eng:
    extract_sentences.extract_sentences((' '.join(word_to_translate)), translated_word)
elif word_type == 'noun':    
    extract_sentences.extract_sentences((translated_word['words'][0]), translated_word)
else:
    # extract_sentences.extract_sentences((translated_word['verbs'][-3]), translated_word)
    extract_sentences.extract_sentences((' '.join(word_to_translate)), translated_word)


# Open images
images.open_images(' '.join(word_to_translate))
   
# Export to txt     
export.export(translated_word, word_type)
