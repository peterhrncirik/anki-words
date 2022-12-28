import argparse
from modules import images, export, extract, translate, sentences


# Usage
parser = argparse.ArgumentParser(description='Get noun/verb translation')
parser.add_argument('word', nargs='*', help='Word you wish to translate', type=str)
parser.add_argument('-t', default='noun', help='Type of word - noun or verb?', type=str)
parser.add_argument('-eng', default=False, help='Translate from German to English', type=bool)

args = parser.parse_args()

# Parser
word_to_translate = args.word
word_type = args.t
to_eng = args.eng

# Open website, get HTML
soup = extract.extract_word(word=word_to_translate, type=word_type, to_eng=to_eng)

# Translate word, return dict
translated_word = translate.translate_word(soup=soup, type=word_type)


# Find example sentences based on type
if word_type == 'noun':
    sentences.find_sentences(extract.extract_sentence(translated_word['words'][0]), translated_word)
else:
    sentences.find_sentences(extract.extract_sentence(translated_word['verbs'][-3]), translated_word)


# Open images
# images.open_images(' '.join(word_to_translate))
   
# Export to txt     
# export.export(translated_word, word_type)
