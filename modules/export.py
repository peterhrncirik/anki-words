from os import startfile

def export(d, type):
    print('Saving file...')

    with open('word.txt', 'w') as file:

        for word in d.get('words'):
        
            if type == 'noun':
                file.write(word)
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
    
