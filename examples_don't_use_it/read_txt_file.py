with open('prova.txt', 'r') as f:
    content = f.read()
print('ciao' + content.replace('latest: ', '')) 
input()