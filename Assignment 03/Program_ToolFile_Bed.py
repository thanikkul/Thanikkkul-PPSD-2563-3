# Description of this Program
# Author : Thanikkul Promsree
# Program Name : Read & Write File
# Program Language : Python



def menu():  # function menu
    select_menu = input(
        'Menu Program\n Enter W write data to file\n Enter R read data from file\n Enter A append data file\n Enter D remove data from file\n Enter You :')  # Define menu information Get data from the keyboard
    if select_menu == 'W': 
        write_file()
    elif select_menu == 'R': 
        read_file()
    elif select_menu == 'A': 
        append_file()
    elif select_menu == 'D': 
        delete_file()
    else:  
        print('Please Select W , R , A or D')


def write_file():  # function for write File
    file = open('file.txt', 'w') 
    data_list = [] 
    while True: 
        try:
            data_input = int(input('Enter a number :')) 
            data_list.append(str(data_input)) 
        except:
            print('Please Enter a number')  
            break

    file.write(" ".join(data_list)) 
    file.close()  


def read_file():  # function for read File
    file = open('file.txt') 
    data = file.read() 
    print(data) 
    file.close() 


def append_file():  # function for add data to File
    file = open('file.txt', 'a+') 
    data_list = [] 
    while True: 
        try:
            data_input = int(input('Enter a number :'))
            data_list.append(str(data_input)) 
            select = input(
                'Enter S stop record file \nEnter N write  data to file again\nEnter a Select :') 
            if select == 'S': 
                break
            elif select == 'N': 
                pass
            else: 
                break
        except: 
            print('Please Enter a number')
            break

    file.write(" ".join(data_list)) 
    file.close() 


def delete_file():  # function for remove data in File
    file = open("file.txt", 'w') 
    file.write("") 
    file.close() 


menu()
