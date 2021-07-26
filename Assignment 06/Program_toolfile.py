# Description of this Program
# Author : Thanikkul Promsree
# Since : 2021-05-06
# Program Name : Read & Write File
# Program Language : Python
# Program Purpose : Write a small program

# Modify : 2021-07-27
# Modify Description : -Add filename function
#                      -Check file repetition frequency
#                      -fix check Open and Write to File
# Modify by : Thanikkul Promsree
def filename():
    global filename
    print('---Please Create file .txt ---')
    try:
        filename = str(input('Please enter the filename of the file : '))
    except:
        print(
            'A filename cannot contain any of the following characters: \ / : * ? " < > |')
        select_Return = input(
            'Do you want to start working again?\n Enter Y write data to file again\n If you type other options, the program will exit.\nEnter a Select : ')  # Define menu information Get data from the keyboard
        if select_Return.upper() == 'Y':  # this function for compare if get "Y" from keyboard then run write_file Function
            write_file()
        else:  # this function for another from keyboard then stop a program
            print('---End Program---')


def menu():  # function menu
    select_menu = input(
        '---Menu Program---\n Enter W write data to file\n Enter R read data from file\n Enter A append data file\n Enter D remove data from file\n Enter You :')  # Define menu information Get data from the keyboard
    select = select_menu.upper()
    if select == 'W':  # this function for compare if get "W" from keyboard then run write_file Function
        write_file()
    elif select == 'R':  # this function for compare if get "R" from keyboard then run read_file Function
        read_file()
    elif select == 'A':  # this function for compare if get "A" from keyboard then run append_file Function
        append_file()
    elif select == 'D':  # this function for compare if get "D" from keyboard then run delete_file Function
        delete_file()
    else:  # This function is for comparison if input from the keyboard other than set. The message will be displayed
        print('!!! Please Select W , R , A or D !!!')
        select_Return = input(
            'Do you want to start working again?\n Enter Y start Menu again\n If you type other options, the program will exit.\nEnter a Select : ')  # Define menu information Get data from the keyboard
        if select_Return.upper() == 'Y':  # this function for compare if get "Y" from keyboard then run menu Function
            menu()


def write_file():  # function for write File
    filename()
    try:
        file = open(filename, 'x')  # this function for open file
    except:
        print('!!! The file you will create already exists. !!!')
        select_Return = input(
            'Do you want to start working again?\n Enter Y write data to file again\n If you type other options, the program will exit.\nEnter a Select : ')  # Define menu information Get data from the keyboard
        if select_Return.upper() == 'Y':  # this function for compare if get "Y" from keyboard then run write_file Function
            menu()
        else:  # this function for another from keyboard then stop a program
            print('---End Program---')

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
                'Do you want to start working again?\n Enter Y write data to file again\n If you type other options, the program will exit.\nEnter a Select : ')  # Define menu information Get data from the keyboard
            if select_Return.upper() == 'Y':  # this function for compare if get "Y" from keyboard then run write_file Function
                write_file()
            else:  # this function for another from keyboard then stop a program
                print('---End Program---')
                break

    file.write(" ".join(data_list))  # this function for write file
    file.close()  # this function for close file


def read_file():  # function for read File
    filename()
    file = open(filename)  # this function for open file
    data = file.read()  # this function for read file
    print(data)  # this function for read file and displayed to screen
    file.close()  # this function for close file


def append_file():  # function for add data to File
    filename()
    file = open(filename, 'a+')  # this function for open file
    data_list = []  # This function is for storing data in list
    while True:  # This function is used to check the data, if correct it will continue.
        try:
            # Define data information Get data from the keyboard
            data_input = int(input('Enter a number :'))
            # Keep the received data in data_list
            data_list.append(str(data_input))
            select = input(
                'Enter S stop record file \nEnter N write  data to file again\nEnter a Select :')  # Define menu information Get data from the keyboard
            if select.upper() == 'S':  # this function for compare if get "S" from keyboard then stop a program
                break
            elif select.upper() == 'N':  # this function for compare if get "N" from keyboard then Will receive more information
                pass
            else:  # this function for another from keyboard then stop a program
                break
        except:  # this function for another from keyboard then stop a program
            print('!!! Please Enter a number !!!')
            select_Return = input(
                'Do you want to start working again?\n Enter Y append data to file again\n If you type other options, the program will exit.\nEnter a Select : ')  # Define menu information Get data from the keyboard
            if select_Return.upper() == 'N':  # this function for compare if get "Y" from keyboard then run write_file Function
                append_file()
            else:  # this function for another from keyboard then stop a program
                print('---End Program---')
                break

    file.write(" ".join(data_list))  # this function for write file
    file.close()  # this function for close file


def delete_file():  # function for remove data in File
    filename()
    file = open(filename, 'w')  # this function for open file
    file.write("")  # this function for remove file
    file.close()  # this function for close file


menu()  # this function for Run menu
