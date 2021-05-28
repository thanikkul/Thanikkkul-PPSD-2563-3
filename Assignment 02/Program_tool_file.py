# HW_2
def menu(): #function menu
    k_menu = input(
        'Menu Program\n Enter W write data to file\n Enter R read data from file\n Enter A append data file\n Enter D remove data from file\n Enter You :')
    if k_menu == 'W':
        write_file()
    elif k_menu == 'R':
        read_file()
    elif k_menu == 'A':
        append_file()
    elif k_menu == 'D':
        delete_file()
    else:
        print('Please Select W , R , A or D')


def write_file(): #function for write File
    f = open('test.txt', 'w')
    data_list = []
    while True:
        try:
            data_input = int(input('Enter a number :'))
            data_list.append(str(data_input))
        except:
            print('Please Enter a number')
            break

    f.write(" ".join(data_list))
    f.close()


def read_file(): #function for read File
    f = open('test.txt')
    data = f.read()
    print(data)
    f.close()



menu()
