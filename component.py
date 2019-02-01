import os

def addTo():
    i = 1
    stuff = '0'
    while True:
        fname = input('File to append to\n')
        if os.path.exists(fname):
            print('Start typing')
            with open('text.txt', 'a') as f:
                while True:
                    stuff = input(f'{i} ')
                    if not(stuff in 'exit'):
                        f.write(stuff + '\n')
                        i += 1
                    else:
                        break
        elif fname in  'exit':
            break
        else:
            print('\nFile not found!')

##################################################

def create():
    while True:
        fname = input('Name your file\n')
        if not(os.path.exists(fname)):
            content = '0'
            i = 0
            print('Start typing')
            with open(fname, 'w') as f:
                while True:
                    content = input(f'{i} ')
                    if content in 'exit':
                        break
                    else:
                        f.write(content + '\n')
                        i +=1
            break
        else:
            print('\nFilename already in use!')

##################################################

def readFrom():
    while  True:
        fname = input('File to read from\n')
        if fname in 'exit':
            break
        if os.path.exists(fname):
            with open(fname, 'r') as f:
                for line in f:
                    print(line, end='')
            print()
        else:
            print('\nFile not found!')

##################################################
