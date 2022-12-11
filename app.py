import argparse
from modules import images, export, extract, translate, sentences


# Usage
parser = argparse.ArgumentParser(description='word')
parser.add_argument('-w', default='car', nargs='*', help='Word you wish to translate', type=str)
parser.add_argument('-t', default='noun', help='Type of word - noun or verb?', type=str)
args = parser.parse_args()

# Open website, get HTML
soup = extract.extract_word(word=args.w, type=args.t)

# Translate word, return dict
translated_word = translate.translate_word(soup=soup, type=args.t)


# Find example sentences based on type
if args.t == 'noun':
    sentences.find_sentences(extract.extract_sentence(translated_word['words'][0]), translated_word)
else:
    sentences.find_sentences(extract.extract_sentence(translated_word['verbs'][-3]), translated_word)


# Open images
images.open_images(' '.join(args.w))
   
# Export to txt     
export.export(translated_word, args.t)
