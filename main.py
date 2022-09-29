from pyfiglet import Figlet


    
def show_menu():

    print('1-Add Product')
    print('2-Edit Product')
    print('3-Delete Product')
    print('4-Search')
    print('5-Show List')
    print('6-Buy')
    print('7-Exit')

PROUDUCT=[]

def load():
    print("loadig")
    f = open('database.txt','r')
    rows = f. read().split('\n')    
    for i in range(len(rows)):
        info = rows[i].split(',')
        PROUDUCT.append({'id': info[0], 'name': info[1], 'price': info[2],'count': info[3]})
    print("program is ready to use")    


load()
f = Figlet(font='standard')
print(f.renderText('akram store'))

show_menu()
choice = int(input('please choose a number'))

if choice == 1:
   pass 
if choice == 2:
   pass
if choice == 3:
   pass
if choice == 4:
   pass
if choice == 5:
   pass
if choice == 6:
   pass
if choice == 7:
   pass
