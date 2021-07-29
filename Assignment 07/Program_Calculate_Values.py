# Description of this Program
# Author : Thanikkul Promsree
# Since : 2021-07-29
# Program Name : Calculate Values
# Program Language : Python
# Program Purpose : Calculate
import math  # import module math for use 'sqrt'


def count_number():  # function count number
    data_numbers = []  # add data enter list
    while True:  # This function is used to check the data, if correct it will continue.
        try:
            # Define menu information Get data from the keyboard
            number = int(input('Enter a number :'))
            data_numbers.append(number)  # add data enter list
        except:
            # this function for read file and displayed to screen
            print('%d numbers in list' % len(data_numbers))
            # this function for read file and displayed to screen
            print('-End Program-')


def minimum_number():  # function minimum number
    data_minimum_number = []  # add data enter list
    while True:  # This function is used to check the data, if correct it will continue.
        try:
            # Define menu information Get data from the keyboard
            number = int(input('Enter a number :'))
            data_minimum_number.append(number)  # add data enter list
        except:
            # this function for read file and displayed to screen
            print('Min number = %d' % min(data_minimum_number))
            # this function for read file and displayed to screen
            print('-End Program-')


def maximum_number():  # function minimum number
    data_maximum_number = []  # add data enter list
    while True:  # This function is used to check the data, if correct it will continue.
        try:
            # Define menu information Get data from the keyboard
            number = int(input('Enter a number :'))
            data_maximum_number.append(number)  # add data enter list
        except:
            # this function for read file and displayed to screen
            print('Max number = %d' % max(data_maximum_number))
            # this function for read file and displayed to screen
            print('-End Program-')


def mean_number():  # function mean number
    data_mean_number = []  # add data enter list
    while True:
        try:
            # Define menu information Get data from the keyboard
            number = int(input('Enter a number :'))
            data_mean_number.append(number)  # add data enter list
        except:
            # This function store sum data in list
            summing = float(sum(data_mean_number))
            # This function store count data in list
            count = float(len(data_mean_number))
            # this function for read file and displayed to screen
            print('Mean number = {:.2f}'.format(summing/count))
            # this function for read file and displayed to screen
            print('-End Program-')


def median_number():  # function median number
    data_median_number = []  # add data enter list
    data_median_number.sort()  # this function sort data
    while True:
        try:
            # Define menu information Get data from the keyboard
            number = int(input('Enter a number :'))
            data_median_number.append(number)  # add data enter list
        except:
            # This function if data mod 2 not equal to 0 will continue
            if len(data_median_number) % 2 != 0:
                # This function count data and divide 2  will continue
                median = data_median_number[int(len(data_median_number)/2)]
            else:
                median = data_median_number[(int(len(
                    data_median_number)/2)) - 1] + data_median_number[int(len(data_median_number)/2)]  # This function count data and divide 2 and minus 1 plus data and multiply data divide 2 will continue
                median = median / 2  # This function  data divide 2
            # this function for read file and displayed to screen
            print('median number = %d' % float(median))
            # this function for read file and displayed to screen
            print('-End Program-')


def StandardDeviation_number():  # function StandardDeviation
    StandardDeviation_number = []  # add data enter list
    while True:
        try:
            # Define menu information Get data from the keyboard
            number = int(input('Enter a number :'))
            StandardDeviation_number.append(number)  # add data enter list
        except:
            # This function store sum data in list
            Sum_StandardDeviation_number = (sum(StandardDeviation_number))
            RaisedPower = StandardDeviation_number
            for i in range(len(RaisedPower)):  # This function store sum data in list
                # This function store sum to the power of 2 data in list each data
                RaisedPower[i] = RaisedPower[i]**2
            SumRaisedPower = (sum(RaisedPower))
            SumStandardDeviation = ((len(StandardDeviation_number)*((SumRaisedPower)) - (
                Sum_StandardDeviation_number**2))) / (len(StandardDeviation_number)*((len(StandardDeviation_number)-1)))  # This function calculator before bringing use sqrt
            # This function calculator  use sqrt
            StandardDeviation = math.sqrt(SumStandardDeviation)
            print('StandardDeviation number ={:.8f} '.format(
                StandardDeviation))  # this function for read file and displayed to screen
            # this function for read file and displayed to screen
            print('-End Program-')
            break
