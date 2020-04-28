#  https://github.com/Alshen-bot/Alshen/blob/master/Hangman

cuvant = (input('Introdu cuvant!'))
#a = list(cuvant)
b = list(len(cuvant)*'*')
print ('Cuvantul: ' ,*b, "contine", len(b), 'caractere')

#print(b)
count = 0
max_nr = len(cuvant)+3


while max_nr > count:
    litera = input('Ghiceste litera!')

    if litera in cuvant:
        for i in range(len(cuvant)):
            if litera == cuvant[i]:
                b[i] = litera
        print (b)

        if '*' not in b:
            print('Felicitari: Ai ghicit cuvantul!')
            break
        else:
            print('Mai ai de ghicit ', b.count('*') ,'caractere!')
            count +=1
            print('Ai de folosit inca ',max_nr-count , 'litere!')

    else:
        print('Litera nu se afla in cuvant!')
        count +=1
        print('Ai de folosit inca ',max_nr-count , 'litere!')

