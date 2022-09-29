
language=[]

def load():
    print("loadig")
    f = open('words .txt','r')
    rows = f. read().split('\n')    
    for i in range(len(rows)):
        info = rows[i].split(',')
        language.append({'english': info[0], 'farsi': info[1]})
    print("program is ready to use") 


def edit_word():
    c=input('kodam kalameh ra wiraesh mikonid?   ')         
    for i in range(len(language)):
        if  c==language[i]['english'] or  c==language[i]['farsi']  :
            print(language[i])
            n1= input("aya kalamehe english ra taghir midahid? y or no")
            if n1=="y":
                language[i]['english'] = input("new english")
            n2= input("aya kalamehe farsi ra taghir midahid? y or no")
            if n2=="y": 
                language[i]['farsi'] =(input("new farsi")) 
        else:
            print("in kalameh yaft nashod. ")            
            print(language[i])

def search():
    a = input('word enter for search??  ')
    for i in range(len(language)):
        if  language[i]['english']==a or  language[i]['farsi']==a :
            print(language[i])
        else:
            print("word for search not found")

def show_menu():
    print('1-Add word')
    print('2-Edit word')
    print('3-Search')
    print('4-english_to_farsi')
    print('5-farsi_to_english')
    print('6-Exit & save')

def main():
    choice = int(input('please choose a number :  '))
    if choice ==1:
        add_word()
    elif choice == 2:
        edit_word()
    elif choice == 3:
        search()    
    elif choice == 4:
        english_to_farsi()
    elif choice == 5:
        farsi_to_english()    
    elif choice == 6:
        save_exit ()

def add_word():
    n = int(input('How many word do you add?  '))
    for i in range(n): 
        english = input(' english :  ')
        while english in language:
            print("kala tekrari hast")
            print("be edit bravid")
            english = input(' english :  ')
        mydict1 = {}
        mydict1['english'] = english
        mydict1['farsi'] = input('mani farsi:   ')
        language.append(mydict1)        


def tekrar():
    repeat="y"
    while repeat == "y":
        repeat=input("aya edameh midahid?  (y or n)")
        if repeat=="y":
            show_menu()
            main()   

def save_exit ():
    f = open("words .txt", "w") 
    for i in range(len(language)):
        ss = list(language[i].values())
        if i == 0:
            f.write(str(ss[0])+','+str(ss[1]))
        else:
            f.write('\n'+str(ss[0])+','+str(ss[1]))   
    f.close()



def english_to_farsi():
    translate=[]
    sentence = input('sentence(words) enter for translate??  ')
    sentence_count=sentence.split('.')
    for i in range(len(sentence_count)):
        qqqq=sentence_count[i]
        word_count=qqqq.split(' ')
        #print(word_count)
        for i in range(len(word_count)):
            a = word_count[i]
            for i in range(len(language)):
                if  language[i]['english']==a:
                    translate.append(language[i]['farsi'])
                    #print(language[i]['english'],":",language[i]['farsi'])
                #else:
                 #   print("this word isnot in database.please you add word to database.")
    print("input: ",sentence)
    print("output: ",end='')             
    for i in range (len(translate)):
        print(translate[i],end=' ')
    print()

def farsi_to_english():
    translate=[]
    sentence = input('sentence(words) enter for translate??  ')
    sentence_count=sentence.split('.')
    for i in range(len(sentence_count)):
        qqqq=sentence_count[i]
        word_count=qqqq.split(' ')
        #print(word_count)
        for i in range(len(word_count)):
            a = word_count[i]
            for i in range(len(language)):
                if  language[i]['farsi']==a :
                    translate.append(language[i]['english'])
                    #print(language[i]['english'],":",language[i]['farsi'])
                #else:
                #    print("this word isnot in database.please you add word to database.")
    print("input: ",sentence)
    print("output: ",end='')             
    for i in range (len(translate)):
        print(translate[i],end=' ')
    print()
        

load()
for i in range (len(language)):
    print(language[i])
show_menu()
main()
tekrar()    