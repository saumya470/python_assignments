import wikipedia

while True:
    qinput = input('Q: ')
    #wikipedia.set_lang('es')
    print(wikipedia.summary(qinput, sentences = 2)) # Limiting the number of sentences
