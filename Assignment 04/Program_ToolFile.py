# Description of this Program
# Author : Thanikkul Promsree
# Since : 2021-05-06
# Program Name : Read & Write File
# Program Language : Python
# Program Purpose : Write a small program

#Modify : 2021-05-28
#Modify Description : -Add Error system check when type to enter function
#                     -Add system resume or end program when typing Error
#                     -fix check lenght of Data before Write to File
#Modify by : Thanikkul Promsree

def menu():  # function menu
    select_menu = input(
        'Menu Program\n Enter W write data to file\n Enter R read data from file\n Enter A append data file\n Enter D remove data from file\n Enter You :')  # Define menu information Get data from the keyboard
    if select_menu == 'W':  # this function for compare if get "W" from keyboard then run write_file Function
        write_file()
    elif select_menu == 'R':  # this function for compare if get "R" from keyboard then run read_file Function
        read_file()
    elif select_menu == 'A':  # this function for compare if get "A" from keyboard then run append_file Function
        append_file()
    elif select_menu == 'D':  # this function for compare if get "D" from keyboard then run delete_file Function
        delete_file()
    else:  # This function is for comparison if input from the keyboard other than set. The message will be displayed
        print('!!! Please Select W , R , A or D !!!')
        select_Return = input(
            'Do you want to start working again?\n Enter N start Menu again\n If you type other options, the program will exit.\nEnter a Select : ')  # Define menu information Get data from the keyboard
        if select_Return == 'N':  # this function for compare if get "N" from keyboard then run menu Function
            menu()


def write_file():  # function for write File
    file = open('file.txt', 'w')  # this function for open file
    data_list = []  # This function is for storing data in list
    while True:  # This function is used to check the data, if correct it will continue.
        try:
            # Define data information Get data from the keyboard
            data_input = int(input('Enter a number :'))
            # Keep the received data in data_list
            data_list.append(str(data_input))
        except:
            # This function is for comparison if input from the keyboard other than set. The message will be displayed
            print('!!! Please Enter a number !!!')
            select_Return = input(
                'Do you want to start working again?\n Enter N write data to file again\n If you type other options, the program will exit.\nEnter a Select : ')  # Define menu information Get data from the keyboard
            if select_Return == 'N':  # this function for compare if get "N" from keyboard then run write_file Function
                write_file()
            else:  # this function for another from keyboard then stop a program
                break

    file.write(" ".join(data_list))  # this function for write file
    file.close()  # this function for close file


def read_file():  # function for read File
    file = open('file.txt')  # this function for open file
    data = file.read()  # this function for read file
    print(data)  # this function for read file and displayed to screen
    file.close()  # this function for close file


def append_file():  # function for add data to File
    file = open('file.txt', 'a+')  # this function for open file
    data_list = []  # This function is for storing data in list
    while True:  # This function is used to check the data, if correct it will continue.
        try:
            # Define data information Get data from the keyboard
            data_input = int(input('Enter a number :'))
            # Keep the received data in data_list
            data_list.append(str(data_input))
            select = input(
                'Enter S stop record file \nEnter N write  data to file again\nEnter a Select :')  # Define menu information Get data from the keyboard
            if select == 'S':  # this function for compare if get "S" from keyboard then stop a program
                break
            elif select == 'N':  # this function for compare if get "N" from keyboard then Will receive more information
                pass
            else:  # this function for another from keyboard then stop a program
                break
        except:  # this function for another from keyboard then stop a program
            print('!!! Please Enter a number !!!')
            select_Return = input(
                'Do you want to start working again?\n Enter N append data to file again\n If you type other options, the program will exit.\nEnter a Select : ')  # Define menu information Get data from the keyboard
            if select_Return == 'N':  # this function for compare if get "N" from keyboard then run write_file Function
                append_file()
            else:  # this function for another from keyboard then stop a program
                break

    file.write(" ".join(data_list))  # this function for writr file
    file.close()  # this function for close file


def delete_file():  # function for remove data in File
    file = open("file.txt", 'w')  # this function for open file
    file.write("")  # this function for remove file
    file.close()  # this function for close file


menu()  # this function for Run menu
