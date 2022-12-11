import webbrowser

def open_images(word):
    
    print('Loading images...')
    url = f'https://duckduckgo.com/?q={word}&t=newext&atb=v346-1&iar=images&iaf=type%3Agif&iax=images&ia=images'
    firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    firefox.open_new_tab(url)