import os  # for the remove and rename functions
import matplotlib.pyplot as plt  # for displaying charts
import pickle  # for binary files
import random  # to create random variables
import numpy as np

def revenue_sum():  # total sum of loans, savings and deposits

    # global variables
    global sum_deposit
    global sum_loans
    global sum_savings

    sum_deposit=0
    sum_loans=0
    sum_savings=0

    try:
        customers_file = open('customers.txt', 'r')  # Open the customers.txt file.
        # Read the contents of the file into a list.
        customers_list = customers_file.readlines()

        # Strip the \n from each element.
        index = 0
        while index < len(customers_list):
            customers_list[index] = customers_list[index].rstrip('\n')
            index += 1

        # Close the file.
        customers_file.close()

        index=len(customers_list)
        if index!=0: #checking if the customers file is empty
            i=5
            sum_deposit=0
            while (i<index):
                sum_deposit = int(sum_deposit +int(customers_list[i]))  # sum all the deposits of the bank
                i+=7

        else:
            sum_deposit=0
    except FileNotFoundError:
        return

    try:
        loan_file = open('loans.txt', 'r')  # Open the loans.txt file.
        # Read the contents of the file into a list.
        loans_list = loan_file.readlines()

        # Close the file.
        loan_file.close()
        # Strip the \n from each element.
        index = 0
        while index < len(loans_list):
            loans_list[index] = loans_list[index].rstrip('\n')
            index += 1

        index = len(loans_list)
        if index != 0:  # checking if the loans file is empty
            i = 2
            sum_loans = 0
            while (i < index):
                sum_loans = int(sum_loans + int(loans_list[i]))  # sum all the loans of the bank
                i += 3
        else:
            sum_loans=0
    except FileNotFoundError:
        pass

    try:
        saving_file = open('savings.txt', 'r')  # Open the savings.txt file.
        # Read the contents of the file into a list.
        savings_list = saving_file.readlines()

        # Close the file.
        saving_file.close()

        # Strip the \n from each element.
        index = 0
        while index < len(savings_list):
            savings_list[index] = savings_list[index].rstrip('\n')
            index += 1

        index = len(savings_list)
        if index != 0:  # checking if the savings file is empty
            i = 2
            sum_savings = 0
            while (i < index):
                sum_savings = int(sum_savings + int(savings_list[i]))  # sum all the savings of the bank
                i += 3

        else:
            sum_saving=0
    except FileNotFoundError:
        pass

def delete_customer_services(ID):  # delete loans and savings, as part of customer delete

    try:
        loans_file = open('loans.txt', 'r')  # Open the loans.txt file.

        # Read the contents of the file into a list.
        loans_list = loans_file.readlines()

        # Strip the \n from each element.
        index = 0
        while index < len(loans_list):
            loans_list[index] = loans_list[index].rstrip('\n')
            index += 1
        flag = 0
        try:
            search_index = loans_list.index(ID)
            flag = 1
        except ValueError:
            pass

        if (flag == 1):
            del loans_list[search_index:search_index + 3]
            loans_file = open('loans.txt', 'w')  # Open the loans.txt file.
            loans_file.seek(0)
            loans_file.truncate()

            for item in loans_list:
                loans_file.write(str(item) + '\n')
        # Close the file.
        loans_file.close()

    except FileNotFoundError:   # in case no file was found
        pass

    try:
        saving_file = open('savings.txt', 'r')  # Open the savings.txt file.

        # Read the contents of the file into a list.
        savings_list = saving_file.readlines()

        # Strip the \n from each element.
        index = 0
        while index < len(savings_list):
            savings_list[index] = savings_list[index].rstrip('\n')
            index += 1
        flag = 0
        try:
            search_index = savings_list.index(ID)
            flag = 1
        except ValueError:
            pass

        if (flag == 1):
            del savings_list[search_index :search_index + 3]
            saving_file = open('savings.txt', 'w')  # Open the savings.txt file.
            saving_file.seek(0)
            saving_file.truncate()

            for item in savings_list:
                saving_file.write(str(item) + '\n')
        # Close the file.
        saving_file.close()

    except FileNotFoundError:   # in case no file was found
        pass

def withdraw_savings():  # withdraw customer savings

    validation_flag = 0  # Create a variable to use as a flag

    while validation_flag == 0:  # checking input validation
        try:
            search = int(input('\nEnter customer ID: '))  # ID to search for by user
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")
    search = str(search)

    try:
        customers_file = open('customers.txt', 'r')  # Open the customers.txt file.

    except FileNotFoundError:   # in case no file was found
        print("\nError: No customers file found. \nPlease make sure customers.txt is in the same library as the program, or add a customer to create a file, and try again.")
        return

    # Read the contents of the file into a list.
    customers_list = customers_file.readlines()

    # Close the file.
    customers_file.close()

    # Strip the \n from each element.
    index = 0
    while index < len(customers_list):
        customers_list[index] = customers_list[index].rstrip('\n')
        index += 1

    # search for id in list
    flag = 0
    try:
        search_index = customers_list.index(search)
        currentdeposit = int(customers_list[search_index + 4])
        flag = 1
    except ValueError:
        print('\nNo customer with ID entered was found.')
        return

    try:
        saving_file = open('savings.txt', 'r')  # Open the savings.txt file.

    except FileNotFoundError:   # in case no file was found
        print("\nError: No savings file found. \nPlease make sure savings.txt is in the same library as the program, or add a savings to create a file, and try again.")
        return

    # Read the contents of the file into a list.
    savings_list = saving_file.readlines()

    # close the file
    saving_file.close()

    # Strip the \n from each element.
    index = 0
    while index < len(savings_list):
        savings_list[index] = savings_list[index].rstrip('\n')
        index += 1

    # search for id in list
    flag = 0
    try:
        search_saving_index = savings_list.index(search)
        currentsaving = int(savings_list[search_saving_index + 2])
        flag = 1
    except ValueError:
        print('\nNo savings was found.')
        return

    validation_flag = 0 # variable to use as a flag
    while validation_flag == 0:  # checking ID validation
            print('\nCustomer can withdraw:', str(currentsaving),'dollars. \nAre you sure you want to continue? (Yes/No)')
            answer = str(input())
            if answer!='YES' and answer!='yes' and answer!='NO' and answer!='no' and answer!='Yes' and answer!='No':
                print(
                    "\nInvalid input. Please enter 'Yes' or 'No' only. ")
            else:
                validation_flag = 1

            if validation_flag == 1:
                if answer=='YES' or answer=='yes' or answer=='Yes':
                    # update the customers.txt file
                    newdeposit = str(currentsaving + currentdeposit)
                    customers_list[search_index + 4] = newdeposit  # update the deposit money in the list
                    customers_file = open('customers.txt', 'w')  # Open the customers.txt file.
                    customers_file.seek(0)
                    customers_file.truncate()  # delete file content

                    # write into file
                    for item1 in customers_list:
                        customers_file.write(str(item1) + '\n')

                    del savings_list[search_saving_index:search_saving_index + 3]  # delete saving from the savings.txt file
                    saving_file = open('savings.txt', 'w')  # Open the savings.txt file.
                    saving_file.seek(0)
                    saving_file.truncate()

                    for item2 in savings_list:
                        saving_file.write(str(item2) + '\n')

                    print('\nThe file has been updated, savings have been moved to account.')

                    # Close the files.
                    customers_file.close()
                    saving_file.close()
                else:
                    print('\nNo change has been done.')
                    return

def new_saving():  # open new savings account
    validation_flag = 0  # Create a variable to use as a flag
    while validation_flag == 0:  # checking ID validation
        try:
            search = int(input('\nEnter customer ID: '))
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")
    search = str(search)

    try:
        customers_file = open('customers.txt', 'r')  # Open the customers.txt file.
    except FileNotFoundError:   # in case no file was found
        print("\nError: No customers file found. \nPlease make sure to add a customer before making a new savings account.")
        return

    # Read the contents of the file into a list.
    customers_list = customers_file.readlines()

    # Close the file.
    customers_file.close()

    # Strip the \n from each element.
    index = 0
    while index < len(customers_list):
        customers_list[index] = customers_list[index].rstrip('\n')
        index += 1

    try:
        search_index = customers_list.index(search)
    except ValueError:
        print('\nNo customer with ID entered was found, please add a new customer.\n')
        add_newcustomer()

    try:  # checking if customer already has a loan
        saving_file = open('savings.txt', 'r')  # Open the savings.txt file.
        # Read the contents of the file into a list.
        savings_list = saving_file.readlines()

        # Close the file.
        saving_file.close()

        # Strip the \n from each element.
        index = 0
        while index < len(savings_list):
            savings_list[index] = savings_list[index].rstrip('\n')
            index += 1
        try:  # checking id in file
            search_index = savings_list.index(search)
            print('\nID entered already has a savings account.')
            return
        except ValueError:  # ID wasn't found in file
            pass

    except FileNotFoundError:   # in case no file was found
        pass

    typesaving = input('\n**** Main Menu --> Services --> Savings --> Open Savings account **** \n 1 - Saving for 3 months \n 2 - Saving for 12 months \n 3 - Go back \n 4 - Exit program \n')
    while (typesaving != '1' and typesaving != '2' and typesaving != '3' and typesaving != '4'):  # input validation
        print("\n**Invalid input, please enter valid numbers!\n")
        typesaving = input('\n**** Main Menu --> Services --> Savings --> Open Savings account **** \n 1 - Saving for 3 months \n 2 - Saving for 12 months \n 3 - Go back \n 4 - Exit program \n')
    typesaving = int(typesaving)
    if (typesaving == 1):
        typesavingstr = 'Saving for 3 months'
    elif typesaving == 2:
        typesavingstr = 'Saving for 12 months'
    elif typesaving == 3:
        return
    elif typesaving == 4:
        exit()

    customers_file = open('customers.txt', 'r')  # Open the customers.txt file.

    # Read the contents of the file into a list.
    customers_list = customers_file.readlines()

    # Close the file.
    customers_file.close()

    # Strip the \n from each element.
    index = 0
    while index < len(customers_list):
        customers_list[index] = customers_list[index].rstrip('\n')
        index += 1

    search_index = customers_list.index(search)

    currentdeposit= int(customers_list[search_index+4])
    validation_flag = 0
    while validation_flag == 0:  # checking ID validation
        try:
            print('\nEnter the requested amount. Based on account deposit money, customer has', str(currentdeposit) , 'dollars.')
            savingamount=int(input())
            if currentdeposit < savingamount:
                print("\nInvalid input. please enter amount up to" , str(currentdeposit) , "dollars.")
            else:
                validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")
    savings_tuple = (search, typesavingstr, savingamount)
    saving_file = open('savings.txt', 'a')  # Open the savings.txt file.

    for item in savings_tuple:  # update the saving file
        saving_file.write(str(item) + '\n')

    newdeposit= str(currentdeposit-savingamount)
    customers_list[search_index + 4] = newdeposit
    customers_file = open('customers.txt', 'w')  # Open the customers.txt file.
    customers_file.seek(0)
    customers_file.truncate()   # delete file content

    for item in customers_list: # update the customers file
        customers_file.write(str(item) + '\n')

    print('\nThe file has been updated.')

    # Close the files.
    customers_file.close()
    saving_file.close()

def changeloan():  # change loan

    validation_flag = 0  # variable to use as a flag

    while validation_flag == 0:  # input validation
        try:
            search = int(input('\nEnter customer ID: '))  # ID to search
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")
    search = str(search)

    try:
        loan_file = open('loans.txt', 'r')  # Open the loans.txt file.

    except FileNotFoundError:   # in case no file was found
        print("\nError: No loans file found. \nPlease make sure loans.txt is in the same library as the program, or add a customer to create a file, and try again.")
        return

    # Read the contents of the file into a list.
    loans_list = loan_file.readlines()

    # Strip the \n from each element.
    index = 0
    while index < len(loans_list):
        loans_list[index] = loans_list[index].rstrip('\n')
        index += 1

    # search for id in list
    flag = 0
    try:
        search_index = loans_list.index(search)
        flag = 1
    except ValueError:
        print('\nNo loan was found.')
        return

    validation_flag = 0
    while validation_flag == 0:  # checking validation
        try:
            newchangeinloan = int(input('Enter customer new change in loan: '))
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")

    # in case customer was found
    if (flag == 1):
        loans_list[search_index + 2] = newchangeinloan
        loan_file = open('loans.txt', 'w')  # Open the loans.txt file.
        loan_file.seek(0)
        loan_file.truncate()  # delete file content

        for item in loans_list: # update the file
            loan_file.write(str(item) + '\n')

        print('\nThe file has been updated.')

    # Close the file.
    loan_file.close()

def delete_loan():  # delete loan
    validation_flag = 0  # Create a variable to use as a flag
    while validation_flag == 0:  # checking input validation
        try:
            search = int(input('\nEnter customer ID to delete: '))  # ID to search for by user
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")
    search = str(search)

    try:
        loans_file = open('loans.txt', 'r')  # Open the loans.txt file.

    except FileNotFoundError:   # in case no file was found
        print("\nError: No loans file found. \nPlease make sure loans.txt is in the same library as the program, or add a customer to create a file, and try again.")
        return

    # Read the contents of the file into a list.
    loans_list = loans_file.readlines()

    # Strip the \n from each element.
    index = 0
    while index < len(loans_list):
        loans_list[index] = loans_list[index].rstrip('\n')
        index += 1
    flag = 0
    try:
        search_index = loans_list.index(search)
        flag = 1
    except ValueError:
        print('\nNo customer with ID entered was found.')

    if (flag == 1):
        del loans_list[search_index :search_index + 3]
        loans_file = open('loans.txt', 'w')  # Open the loans.txt file.
        loans_file.seek(0)
        loans_file.truncate()

        for item in loans_list:
            loans_file.write(str(item) + '\n')

        print('\nThe file has been updated.')

    # Close the file.
    loans_file.close()

def new_loan():  # open a new loan
    validation_flag = 0  # Create a variable to use as a flag
    while validation_flag == 0:  # checking ID validation
        try:
            search = int(input('\nEnter customer ID: '))
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")
    search = str(search)

    try:
        customers_file = open('customers.txt', 'r')  # Open the customers.txt file.

    except FileNotFoundError:   # in case no file was found
        print("\nError: No customers file found. \nPlease make sure to add a customer before making a new loan.")
        return

    # Read the contents of the file into a list.
    customers_list = customers_file.readlines()

    # Close the file.
    customers_file.close()

    # Strip the \n from each element.
    index = 0
    while index < len(customers_list):
        customers_list[index] = customers_list[index].rstrip('\n')
        index += 1

    try:
        search_index = customers_list.index(search)
    except ValueError:
        print('\nNo customer with ID entered was found, please add a new customer.\n')
        add_newcustomer()

    try: # checking if customer already has a loan
        loan_file = open('loans.txt', 'r')  # Open the loans.txt file.
        # Read the contents of the file into a list.
        loans_list = loan_file.readlines()

        # Close the file.
        loan_file.close()
        # Strip the \n from each element.
        index = 0
        while index < len(loans_list):
            loans_list[index] = loans_list[index].rstrip('\n')
            index += 1
        try:
            search_index = loans_list.index(search)
            print('\nID entered already has a loan.\n')
            return
        except ValueError:  # ID wasn't found in file
            pass
    except FileNotFoundError:   # in case no file was found
        pass

    typeloan = input('\nPlease choose option by number: \n 1 - Car loan \n 2 - Mortgage \n')
    while (typeloan != '1' and typeloan != '2'):  # input validation
        print("\n**Invalid input, please enter valid numbers!\n")
        typeloan = input('\nPlease choose option by number: \n 1 - Car loan \n 2 - Mortgage \n')
    typeloan = int(typeloan)
    if (typeloan == 1):
        typeloanstr = 'Car loan'
    else:
        typeloanstr = 'Mortgage'
    validation_flag = 0
    while validation_flag == 0:  # checking ID validation
        try:
            loanamount = int(input('\nEnter the requested amount '))
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")
    loan_tuple = (search, typeloanstr, loanamount)
    loan_file = open('loans.txt', 'a')  # Open the loans.txt file.

    for item in loan_tuple:
        loan_file.write(str(item) + '\n')

    print('\nThe file has been updated.')

def savings_menu():  # savings menu
    # Print choice menu
    choice = input(
        "\n**** Main Menu --> Services --> Savings **** \n 1 - Open savings account \n 2 - Withdraw savings \n 3 - Go back \n 4 - Exit program \n ")
    while (choice != '1' and choice != '2' and choice != '3' and choice != '4'):  # input validation
        print("\n**Invalid input, please enter valid numbers!\n")
        choice = input(
            "\n**** Main Menu --> Services --> Savings **** \n 1 - Open savings account \n 2 - Withdraw savings \n 3 - Go back \n 4 - Exit program \n ")
    choice = int(choice)  # Convert to int
    while choice>=1 and choice<=4:
        if (choice == 1):
            new_saving()
        if (choice == 2):
            withdraw_savings()
        if (choice == 3):
            return
        if (choice == 4):
            exit()

        choice = input(
            "\n**** Main Menu --> Services --> Savings **** \n 1 - Open savings account \n 2 - Withdraw savings \n 3 - Go back \n 4 - Exit program \n ")
        while (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5'):  # input validation
            print("\n**Invalid input, please enter valid numbers!\n")
            choice = input(
                "\n**** Main Menu --> Services --> Savings **** \n 1 - Open savings account \n 2 - Withdraw savings \n 3 - Go back \n 4 - Exit program \n ")
        choice = int(choice)  # Convert to int

def loans_menu():  # loans menu
    # Print choice menu
    choice = input(
        "\n**** Main Menu --> Services --> Loans **** \n 1 - Add loan \n 2 - Delete loan \n 3 - Change loan details\n 4 - Go back \n 5 - Exit program \n ")
    while (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5'):  # input validation
        print("\n**Invalid input, please enter valid numbers!\n")
        choice = input(
            "\n**** Main Menu --> Services --> Loans **** \n 1 - Add loan \n 2 - Delete loan \n 3 - Change loan details\n 4 - Go back \n 5 - Exit program \n ")
    choice = int(choice)  # Convert to int
    while choice>=1 and choice<=5:
        if (choice == 1):
            new_loan()
        if (choice == 2):
            delete_loan()
        if (choice == 3):
            changeloan()
        if (choice == 4):
            return
        if (choice == 5):
            exit()

        choice = input(
            "\n**** Main Menu --> Services --> Loans **** \n 1 - Add loan \n 2 - Delete loan \n 3 - Change loan details\n 4 - Go back \n 5 - Exit program \n ")
        while (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5'):  # input validation
            print("\n**Invalid input, please enter valid numbers!\n")
            choice = input(
                "\n**** Main Menu --> Services --> Loans **** \n 1 - Add loan \n 2 - Delete loan \n 3 - Change loan details\n 4 - Go back \n 5 - Exit program \n ")
        choice = int(choice)  # Convert to int

def services_menu():  # sevices menu
    # Print choice menu
    choice = input(
        "\n**** Main Menu --> Services **** \n 1 - Loans \n 2 - Savings \n 3 - Go back \n 4 - Exit program \n ")
    while (choice != '1' and choice != '2' and choice != '3' and choice != '4'):  # input validation
        print("\n**Invalid input, please enter valid numbers!\n")
        choice = input(
            "\n**** Main Menu --> Services **** \n 1 - Loans \n 2 - Savings \n 3 - Go back \n 4 - Exit program \n ")
    choice = int(choice)  # Convert to int

    while choice>=1 and choice<=4:
        if (choice == 1):
            loans_menu()
        if (choice == 2):
            savings_menu()
        if (choice == 3):
            return
        if (choice == 4):
            exit()

        choice = input(
            "\n**** Main Menu --> Services **** \n 1 - Loans \n 2 - Savings \n 3 - Go back \n 4 - Exit program \n ")
        while (choice != '1' and choice != '2' and choice != '3' and choice != '4'):  # input validation
            print("\n**Invalid input, please enter valid numbers!\n")
            choice = input(
                "\n**** Main Menu --> Services **** \n 1 - Loans \n 2 - Savings \n 3 - Go back \n 4 - Exit program \n ")
        choice = int(choice)  # Convert to int

def customer_survey_score_graph():  # customer survey score average graph

    try:
        survey_file = open('customersurvey.dat', 'rb')  # Open the file.
        survey_dict = pickle.load(survey_file)  # load from file
        survey_file.close()
    except (EOFError, FileNotFoundError):  # in case no survey file is found, load past information
        survey_file = open('customersurvey.dat', 'wb')  # Open the file.
        survey_dict = {2016: {'Customer number':10, 'Score':50}, 2017: {'Customer number':50, 'Score':400}, 2018: {'Customer number':100, 'Score':200}, 2019: {'Customer number':100, 'Score':651}, 2020: {'Customer number':15, 'Score':92}}
        pickle.dump(survey_dict, survey_file)  # write to file
        survey_file.close()

    departures_file = open('customersurvey.dat', 'rb')  # Open the file.

    # customer score average
    customer_score = [(survey_dict[2016]['Score'])/(survey_dict[2016]['Customer number']), (survey_dict[2017]['Score'])/(survey_dict[2017]['Customer number']), (survey_dict[2018]['Score'])/(survey_dict[2018]['Customer number']), (survey_dict[2019]['Score'])/(survey_dict[2019]['Customer number']), (survey_dict[2020]['Score'])/(survey_dict[2020]['Customer number'])]

    # year names for plotting
    year = ["2016", "2017", "2018", "2019", "2020"]

    # define window size
    fig, ax = plt.subplots(figsize=(6.4, 4.8))

    # define x and y axes
    ax.plot(year,
            customer_score,
            marker='o')

    # set plot title and axes labels
    plt.title('Customer Survey Score Average (1-10)', fontsize=20)
    plt.xlabel('Year',fontsize=14)
    plt.ylabel('Average Score', fontsize=14)

    plt.show()

def divisions_revenue_graph():  # divisions revenue percentage

    revenue_sum()

    COLOR_VALUE1='#ff9999'
    COLOR_VALUE2='#66b3ff'
    COLOR_VALUE3='#99ff99'

    # plot window size
    plt.rcParams["figure.figsize"] = (6.4, 4.8)

    # Pie chart
    labels = ['Savings', 'Deposits', 'Loans']
    sizes = [sum_savings, sum_deposit, sum_loans]

    # colors
    colors = [COLOR_VALUE1, COLOR_VALUE2, COLOR_VALUE3]
    explode = (0.05, 0.05, 0.05)

    fig1, ax1 = plt.subplots()

    # draw circle
    ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85,
             explode=explode)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')

    # Add title
    plt.title('Divisions revenue percentage',fontsize=20)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)  # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()
    plt.show()

def customer_churn_graph():  # customer churn rate

    try:
        departures_file = open('customerdepartures.dat', 'rb')  # Open the file for reading.
        departures_dict = pickle.load(departures_file)  # load from file
        departures_file.close()
        #flag = 1
    except (EOFError, FileNotFoundError):  # in case no survey file is found, load past information
        departures_file = open('customerdepartures.dat', 'wb')  # Open the file for writing.
        departures_dict = {2016: 10, 2017: 50, 2018: 16, 2019: 100, 2020: 30}
        pickle.dump(departures_dict, departures_file)  # write to file
        departures_file.close()

    # plot window size
    plt.rcParams["figure.figsize"] = (6.4, 4.8)

    # y labels
    y = [departures_dict[2016], departures_dict[2017], departures_dict[2018], departures_dict[2019], departures_dict[2020]]
    # x labels
    x = ('2016', '2017', '2018', '2019', '2020')

    # Plot the bar graph
    plot = plt.bar(x, y,color=(0.2, 0.4, 0.6, 0.6))

    # Add the data value on head of the bar
    for value in plot:
        height = value.get_height()
        plt.text(value.get_x() + value.get_width() / 2.,
                 1.002 * height, '%d' % int(height), ha='center', va='bottom')

    # Add labels and title
    plt.title('Customer churn rate by year',fontsize=20)
    plt.ylabel('Number of departures')
    plt.xlabel('Year of departure')

    # Display the graph on the screen
    plt.show()

# KPI's taken from https://www.datapine.com/kpi-examples-and-templates/
# and https://www.clearpointstrategy.com/bank-kpis/
def kpis_menu():  # KPI's menu
   # Print choice menu
    choice = input(
        "\n**** Main Menu --> Key Performance Indicators and Metrics **** \n 1 - Customer churn rate \n 2 - Divisions revenue percentage  \n 3 - Client survey score \n 4 - Go back\n 5 - Exit program\n")
    while (
            choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5'):  # input validation
        print("\n**Invalid input, please enter valid numbers!\n")
        choice = input(
            "\n**** Main Menu --> Key Performance Indicators and Metrics **** \n 1 - Customer churn rate \n 2 - Divisions revenue percentage  \n 3 - Client survey score \n 4 - Go back\n 5 - Exit program\n")
    choice = int(choice)  # Convert to int
    while choice >= 1 and choice <= 5:
        if (choice == 1):
            customer_churn_graph()
        if (choice == 2):
            divisions_revenue_graph()
        if (choice == 3):
            customer_survey_score_graph()
        if (choice == 4):
            return
        if (choice == 5):
            exit()

        choice = input(
            "\n**** Main Menu --> Key Performance Indicators and Metrics **** \n 1 - Customer churn rate \n 2 - Divisions revenue percentage  \n 3 - Client survey score \n 4 - Go back\n 5 - Exit program\n")
        while (
                choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5'):  # input validation
            print("\n**Invalid input, please enter valid numbers!\n")
            choice = input(
                "\n**** Main Menu --> Key Performance Indicators and Metrics **** \n 1 - Customer churn rate \n 2 - Divisions revenue percentage  \n 3 - Client survey score \n 4 - Go back\n 5 - Exit program\n")
        choice = int(choice)  # Convert to int

def customer_details(): # display customer details
    validation_flag = 0  # variable to use as a flag

    # id to search
    while validation_flag == 0:  # input validation
        try:
            search = int(input('\nEnter ID number to search: '))  # ID to search for by user
            validation_flag = 1
        except ValueError: # checking ID validation
            print("\n**Error: please enter numbers only!\n")
    search = str(search)

    try:
        customers_file = open('customers.txt', 'r')  # Open the file.
    except FileNotFoundError:  # in case no file was found
        print("\nError: No customers file found. \nPlease make sure customers.txt is in the same library as the program, or add a customer to create a file, and try again.")
        return

    # Read the contents of the file into a list.
    customers_list = customers_file.readlines()

    # Close the file.
    customers_file.close()

    # Strip the \n from each element.
    index = 0
    while index < len(customers_list):
        customers_list[index] = customers_list[index].rstrip('\n')
        index += 1

    # search for id in list
    flag=0
    try:
        search_index = customers_list.index(search)
        flag=1
    except ValueError:
        print('\nNo customer with ID entered was found.')
        return

    if flag==1:  # in case customer was found
        print('\nName:', customers_list[search_index-1])
        print('ID:', customers_list[search_index])
        print('Phone number:', customers_list[search_index+1])
        print('Account number:', customers_list[search_index+2])
        print('Monthly income:', customers_list[search_index+3])
        print('Deposit money:', customers_list[search_index+4])

    try:
        savings_file = open('savings.txt', 'r')  # Open the file.

        # Read the contents of the file into a list.
        savings_list = savings_file.readlines()

        # Close the file.
        savings_file.close()

        # Strip the \n from each element.
        index = 0
        while index < len(savings_list):
            savings_list[index] = savings_list[index].rstrip('\n')
            index += 1

        # search for id in list
        flag = 0
        try:
            search_index = savings_list.index(search)
            flag = 1
        except ValueError:
            print('No customer savings were found.')

        if flag == 1:  # in case customer was found
            print('Savings amount:', savings_list[search_index+2])
    except FileNotFoundError:  # in case no file was found
        print ("No customer savings were found.")

    try:
        loans_file = open('loans.txt', 'r')  # Open the file.

        # Read the contents of the file into a list.
        loans_list = loans_file.readlines()

        # Close the file.
        loans_file.close()

        # Strip the \n from each element.
        index = 0
        while index < len(loans_list):
            loans_list[index] = loans_list[index].rstrip('\n')
            index += 1

        # search for id in list
        flag = 0
        try:
            search_index = loans_list.index(search)
            flag = 1
        except ValueError:
            print('No customer loans were found.')

        if flag == 1:  # in case customer was found
            print('Loans amount:', loans_list[search_index+2])
    except FileNotFoundError:  # in case no file was found
        print ("\nNo customer loans were found.")

def change_deposit():  # change customer deposit

    validation_flag = 0  # variable to use as a flag

    # ID to search
    while validation_flag == 0:  # input validation
        try:
            search = int(input('Enter customer ID: '))
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")
    search = str(search)

    #  add new deposit money
    validation_flag = 0
    while validation_flag == 0:  # input validation
        try:
            addeddeposit = int(input('Enter customer new deposit money amount: '))
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")

    try:
        customers_file = open('customers.txt', 'r')  # Open the file.
    except FileNotFoundError:  # in case no file is found
        print("\nError: No customers file found. \nPlease make sure customers.txt is in the same library as the program, or add a customer to create a file, and try again.")
        return

    # Read the contents of the file into a list.
    customers_list = customers_file.readlines()

    # Strip the \n from each element.
    index = 0
    while index < len(customers_list):
        customers_list[index] = customers_list[index].rstrip('\n')
        index += 1

    # search id in list
    flag=0
    try:
        search_index = customers_list.index(search)
        flag=1
    except ValueError:  # in case id was not found
        print('\nNo customer with ID entered was found.\n')

    if (flag==1):  # in case customer was found
        customers_list[search_index+4] = addeddeposit  # add new deposit money
        customers_file = open('customers.txt', 'w')  # Open the file.
        customers_file.seek(0)
        customers_file.truncate()  # delete file content

        # write into file
        for item in customers_list:
            customers_file.write(str(item) + '\n')

        print('\nThe file has been updated.')

    # Close the file.
    customers_file.close()

def change_income(): # change customer income

    validation_flag = 0  # variable to use as a flag

    while validation_flag == 0:  # input validation
        try:
            search = int(input('Enter customer ID: '))  # ID to search
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")
    search = str(search)

    validation_flag = 0
    while validation_flag == 0:  # checking phone validation
        try:
            newmonthlyincome = int(input('Enter customer new monthly income: '))
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")

    try:
        customers_file = open('customers.txt', 'r')  # Open the file.
    except FileNotFoundError:  # in case file was not found
        print("\nError: No customers file found. \nPlease make sure customers.txt is in the same library as the program, or add a customer to create a file, and try again.")
        return

    # Read the contents of the file into a list.
    customers_list = customers_file.readlines()

    # Strip the \n from each element.
    index = 0
    while index < len(customers_list):
        customers_list[index] = customers_list[index].rstrip('\n')
        index += 1

    # search id in list
    flag=0
    try:
        search_index = customers_list.index(search)
        flag=1
    except ValueError:  # in case id was not found
        print('\nNo customer with ID entered was found.\n')

    if (flag==1):  # in case customer was found
        customers_list[search_index+3] = newmonthlyincome  # update new income
        customers_file = open('customers.txt', 'w')  # Open the file.
        customers_file.seek(0)
        customers_file.truncate()  # delete file content

        # update file
        for item in customers_list:
            customers_file.write(str(item) + '\n')

        print('\nThe file has been updated.')

    # Close the file.
    customers_file.close()

def change_phone():  # change customer phone

    validation_flag = 0  # variable to use as a flag

    while validation_flag == 0:  # input validation
        try:
            search = int(input('Enter customer ID: '))  # ID to search
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")
    search = str(search)

    # new phone input
    validation_flag = 0
    while validation_flag == 0:  # input validation
        try:
            newphone = int(input('Enter customer new phone number: '))
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")

    try:
        customers_file = open('customers.txt', 'r')  # Open the file
    except FileNotFoundError:  # in case file was not found
        print("\nError: No customers file found. \nPlease make sure customers.txt is in the same library as the program, or add a customer to create a file, and try again.")
        return

    # Read the contents of the file into a list
    customers_list = customers_file.readlines()

    # Strip the \n from each element
    index = 0
    while index < len(customers_list):
        customers_list[index] = customers_list[index].rstrip('\n')
        index += 1

    # search id in list
    flag=0
    try:
        search_index = customers_list.index(search)
        flag=1
    except ValueError:  # in case id was not found
        print('\nNo customer with ID entered was found.\n')

    if (flag==1):  # in case id was found
        customers_list[search_index+1] = newphone  # update new phone in list
        customers_file = open('customers.txt', 'w')  # Open the file.
        customers_file.seek(0)
        customers_file.truncate()  # delete file content

        # update file
        for item in customers_list:
            customers_file.write(str(item) + '\n')

        print('\nThe file has been updated.')

    # Close the file.
    customers_file.close()

def customer_survey_score():  # insert customer survey score

    validation_flag = 0  # variable to use as a flag
    while validation_flag == 0:  # input validation
        try:
            search = int(input('\nEnter customer ID: '))  # account number to search
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")

    if search_ID(search) == 1:
        print("\nNo customer with ID entered was found.")
        return

    # year input
    validation_flag = 0  # variable as a flag
    while validation_flag == 0:  # input validation
        try:
            year = int(input('\nEnter current year: '))  # ID to search for by user
            if (year != 2016 and year != 2017 and year != 2018 and year != 2019 and year != 2020):
                raise ValueError
            validation_flag = 1
        except ValueError:
            print("\n**Invalid input: Year must be in the range of 2016-2020.")

    # load survey file
    try:
        survey_file = open('customersurvey.dat', 'rb')  # Open the file for reading
        survey_dict = pickle.load(survey_file)
    except (EOFError, FileNotFoundError):  # in case no survey file is found, load past information
        survey_file = open('customersurvey.dat', 'wb')  # Open the file for writing
        survey_dict = {2016: {'Customer number':10, 'Score':50}, 2017: {'Customer number':50, 'Score':400}, 2018: {'Customer number':100, 'Score':200}, 2019: {'Customer number':100, 'Score':651}, 2020: {'Customer number':15, 'Score':92}}
        pickle.dump(survey_dict, survey_file)
        survey_file.close()

    validation_flag = 0  # variable as a flag
    while validation_flag == 0:  # input validation
        try:
            score = int(input('\nEnter customer score, between 1-10: '))  # insert customer score
            if score < 1 or score > 10:
                raise ValueError
            validation_flag = 1
        except ValueError:
            print("\n**Invalid input: The number must be in the range of 1-10.")

    # update score in dictionary
    survey_dict[year]['Customer number']+=1
    survey_dict[year]['Score']+=score

    survey_file = open('customersurvey.dat', 'wb')  # Open the file

    # update file
    pickle.dump(survey_dict, survey_file)

    survey_file.close()  # Close the file

def update_customer_menu(): # update customer details menu

    choice = input(
        "\n**** Main Menu --> Customers --> Details Update **** \n 1 - Change phone number \n 2 - Change monthly income \n 3 - Change deposit money \n 4 - Insert customer survey score \n 5 - Go back\n 6 - Exit program\n")
    while (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6'):  # input validation
        print("\n**Invalid input, please enter valid numbers!\n")
        choice = input(
            "\n**** Main Menu --> Customers --> Details Update **** \n 1 - Change phone number \n 2 - Change monthly income \n 3 - Change deposit money \n 4 - Insert customer survey score \n 5 - Go back\n 6 - Exit program\n")
    choice = int(choice)  # Convert to int

    while choice>=1 and choice<=6:
        if (choice == 1):
            change_phone()
        if (choice == 2):
            change_income()
        if (choice == 3):
            change_deposit()
        if (choice == 4):
            customer_survey_score()
        if (choice == 5):
            return
        if (choice == 6):
            exit()

        choice = input(
            "\n**** Main Menu --> Customers --> Details Update **** \n 1 - Change phone number \n 2 - Change monthly income \n 3 - Change deposit money \n 4 - Insert customer survey score \n 5 - Go back\n 6 - Exit program\n")

        while (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6'):  # input validation
            print("\n**Invalid input, please enter valid numbers!\n")
            choice = input(
                "\n**** Main Menu --> Customers --> Details Update **** \n 1 - Change phone number \n 2 - Change monthly income \n 3 - Change deposit money \n 4 - Insert customer survey score \n 5 - Go back\n 6 - Exit program\n")
        choice = int(choice)  # Convert to int

def deletedcustomers_file():  # save deleted customers amount
    validation_flag=0
    while validation_flag == 0:  # input validation
        try:
            year = int(input('Enter year of departure: '))  # ID to search
            if (year != 2016 and year != 2017 and year != 2018 and year != 2019 and year != 2020):
                raise ValueError
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")

    try:
        departures_file = open('customerdepartures.dat', 'rb')  # Open the file for reading.
        departures_dict = pickle.load(departures_file)  # load from file
    except (EOFError, FileNotFoundError):  # in case file was not found, load deleted history
        departures_file = open('customerdepartures.dat', 'wb')  # Open the file for writing.
        departures_dict = {2016: 10, 2017: 50, 2018: 16, 2019: 100, 2020: 30}
        pickle.dump(departures_dict, departures_file)  # write into file
        departures_file.close()

    departures_file = open('customerdepartures.dat', 'wb')  # Open the file.

    departures_dict[year]+=1  # add 1 departure to year

    pickle.dump(departures_dict, departures_file)  # write into file

    departures_file.close()  # Close the file

def deletecustomer_byid():  # delete customer by ID

    validation_flag = 0  # variable to use as a flag
    while validation_flag == 0:  # input validation
        try:
            search = int(input('\nEnter customer ID to delete: '))  # ID to search
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")
    search = str(search)

    try:
        customers_file = open('customers.txt', 'r')  # Open the file.
    except FileNotFoundError:
        print("\nError: No customers file found. \nPlease make sure customers.txt is in the same library as the program, or add a customer to create a file, and try again.")
        return

    # Read the contents of the file into a list.
    customers_list = customers_file.readlines()

    # Strip the \n from each element.
    index = 0
    while index < len(customers_list):
        customers_list[index] = customers_list[index].rstrip('\n')
        index += 1

    flag=0
    try:
        search_index = customers_list.index(search)
        flag=1
    except ValueError:
        print('\nNo customer with ID entered was found.')

    if (flag==1):
        del customers_list[search_index-1:search_index+6] # delete customer
        customers_file = open('customers.txt', 'w')  # Open the file
        customers_file.seek(0)
        customers_file.truncate()

        # write list into file
        for item in customers_list:
            customers_file.write(str(item) + '\n')

        # keep deleted history
        deletedcustomers_file()

        delete_customer_services(search)  # delete customer loans and savings

        print('\nThe file has been updated.')

    # Close the file.
    customers_file.close()

def deletecustomer_byaccountnum():  # delete customer by account number
    validation_flag = 0  # variable to use as a flag
    while validation_flag == 0:  # input validation
        try:
            search = int(input('\nEnter customer account number to delete: '))  # account number to search
            validation_flag = 1
        except ValueError:
            print("\n**Error: please enter numbers only!\n")
    search = str(search)

    try:
        customers_file = open('customers.txt', 'r')  # Open the file.
    except FileNotFoundError:
        print("\nError: No customers file found. \nPlease make sure customers.txt is in the same library as the program, or add a customer to create a file, and try again.")
        return

    # Read the contents of the file into a list.
    customers_list = customers_file.readlines()

    # Strip the \n from each element.
    index = 0
    while index < len(customers_list):
        customers_list[index] = customers_list[index].rstrip('\n')
        index += 1

    # search account num in list
    flag=0
    try:
        search_index = customers_list.index(search)
        flag=1
    except ValueError:  # in case account num was not found
        print('\nNo customer with account number entered was found.\n')

    if (flag==1):  # if account num was found
        delete_customer_services(customers_list[search_index-2])  # delete customer loans and savings
        del customers_list[search_index-3:search_index+4]  # delete customer
        customers_file = open('customers.txt', 'w')  # Open the file.
        customers_file.seek(0)
        customers_file.truncate()

        # write list into file
        for item in customers_list:
            customers_file.write(str(item) + '\n')

        # keep deleted history
        deletedcustomers_file()

        print('\nThe file has been updated.')

    # Close the file.
    customers_file.close()

def deletecustomer_menu():  # delete menu

    # choice menu
    choice = input("\n**** Main Menu --> Customers --> Delete Customer **** \n 1 - Delete by ID \n 2 - Delete by account number \n 3 - Go back \n 4 - Exit program \n")

    while (choice != '1' and choice != '2' and choice != '3' and choice != '4'):  # input validation
        print("\n**Invalid input, please enter valid numbers!\n")
        choice = input("\n**** Main Menu --> Customers --> Delete Customer **** \n 1 - Delete by ID \n 2 - Delete by account number \n 3 - Go back \n 4 - Exit program \n")
    choice = int(choice)  # Convert to int

    if (choice == 1):
        deletecustomer_byid()
    if (choice == 2):
        deletecustomer_byaccountnum()
    if (choice == 3):
        return
    if (choice == 4):
        exit()

def search_ID(ID): #  search customer id in file

    try:
        customers_file = open('customers.txt', 'r')  # Open the file.
    except FileNotFoundError:
        return 1

    # Read the contents of the file into a list.
    customers_list = customers_file.readlines()

    # Close the file.
    customers_file.close()

    # Strip the \n from each element.
    index = 0
    while index < len(customers_list):
        customers_list[index] = customers_list[index].rstrip('\n')
        index += 1

    # search in list
    try:
        search_index = customers_list.index(str(ID))
        return 0
    except ValueError:
        return 1

def add_newcustomer():  # add a new customer

    # How many customers to add
    validation_flag=0
    while validation_flag == 0:  # input validation
      try:
         howmany = int(input("How many pepole would you like to add?\n"))
         if howmany <=0:
             raise ValueError
         validation_flag = 1
      except ValueError:
         print("\n**Error: please enter  valid numbers only!\n")

    validation_flag = 0
    for n in range(1, howmany + 1):  # Add "howmany" customers

        # name input
        validation_flag = 0 # variable to use as a flag
        while validation_flag == 0:  # input validation
            name = input('Enter customer fullname: ')
            if name.replace(" ", "").isalpha():
                validation_flag = 1
            else:
                print ("\nName is invalid. Please use alphabetic characters only.\n")

        # id input
        validation_flag = 0 # variable to use as a flag
        while validation_flag == 0:  # input validation
            try:
                id = int(input('Enter customer ID: '))
                validation_flag = 1
            except ValueError:
                print("\n**Error: please enter numbers only!\n")

        if search_ID(id)==0: # check if ID is already a customer
            print('\nThere is already a customer with that ID in file. You can update his details through the menu.')
            return

        # phone input
        validation_flag = 0
        while validation_flag == 0:  # input validation
            try:
                phone = int(input('Enter customer phone number: '))
                validation_flag = 1
            except ValueError:
                print("\n**Error: please enter numbers only!\n")

        # account number input
        validation_flag = 0
        while validation_flag == 0:  # input validation
            try:
                accountnum = int(input('Enter customer  account number: '))
                validation_flag = 1
            except ValueError:
                print("\n**Error: please enter numbers only!\n")

        # monthly income input
        validation_flag = 0
        while validation_flag == 0:  # input validation
            try:
                monthlyincome = int(input('Enter customer monthly income: '))
                validation_flag = 1
            except ValueError:
                print("\n**Error: please enter numbers only!\n")

        # deposit input
        validation_flag = 0
        while validation_flag == 0:  # input validation
            try:
                totalmoney = int(input('Enter customer deposit money: '))
                validation_flag = 1
            except ValueError:
                print("\n**Error: please enter numbers only!\n")

        # generating password
        random_num = random.randint(1000, 9999)
        password = int(str(id%1000) + str(random_num))
        print("\nPassword generatade for customer:", password)

        # creating customer tuple
        customers_tuple = (name,id,phone,accountnum,monthlyincome,totalmoney,password)

        customers_file = open('customers.txt', 'a')  # Open customers file

        # add to file
        for item in customers_tuple:
            customers_file.write(str(item) + '\n')

        print('\nThe file has been updated.')

    customers_file.close()  # Close the file

def customers_menu(): # Customers menu

    # Choice Menu
    choice = input(
        "\n**** Main Menu --> Customers **** \n 1 - Add customer \n 2 - Delete customer \n 3 - Update customer details \n 4 - Display customer details\n 5 - Go back\n 6 - Exit program\n")
    while (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6'):  # input validation
        print("\n**Invalid input, please enter valid numbers!\n")
        choice = input(
            "\n**** Main Menu --> Customers **** \n 1 - Add customer \n 2 - Delete customer \n 3 - Update customer details \n 4 - Display customer details\n 5 - Go back\n 6 - Exit program\n")
    choice = int(choice)  # Convert to int

    while choice>=1 and choice<=6:
        if (choice == 1):
            add_newcustomer()
        if (choice == 2):
            deletecustomer_menu()
        if (choice == 3):
            update_customer_menu()
        if (choice == 4):
            customer_details()
        if (choice == 5):
            return
        if (choice == 6):
            exit()

        # Choice Menu
        choice = input(
            "\n**** Main Menu --> Customers **** \n 1 - Add customer \n 2 - Delete customer \n 3 - Update customer details \n 4 - Display customer details\n 5 - Go back\n 6 - Exit program\n")
        while (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6'):  # input validation
            print("\n**Invalid input, please enter valid numbers!\n")
            choice = input(
                "\n**** Main Menu --> Customers **** \n 1 - Add customer \n 2 - Delete customer \n 3 - Update customer details \n 4 - Display customer details\n 5 - Go back\n 6 - Exit program\n")
        choice = int(choice)  # Convert to int

def main_menu():  # main menu
    print("Welcome to Bank Hapoalim!\n")

    print("Please choose option by number.\n")

    # Choice Menu
    choice = input(
        "****** Main Menu ****** \n 1 - Customers menu \n 2 - Services menu \n 3 - Key performance indicators and metrics \n 4 - Exit program \n")

    while (choice != '1' and choice != '2' and choice != '3' and choice != '4'):  # input validation
        print("\n**Invalid input, please enter valid numbers!\n")
        choice = input(
            "\n****** Main Menu ****** \n 1 - Customers menu \n 2 - Services menu \n 3 - Key performance indicators and metrics \n 4 - Exit program \n")

    choice = int(choice)  # Convert to int
    while choice>=1 and choice<=4:
        if (choice == 1):
            customers_menu()
        if (choice == 2):
            services_menu()
        if (choice == 3):
            kpis_menu()
        if (choice == 4):
            exit()

        # Choice Menu
        choice = input(
            "\n****** Main Menu ****** \n 1 - Customers menu \n 2 - Services menu \n 3 - Key performance indicators and metrics \n 4 - Exit program \n")
        while (choice != '1' and choice != '2' and choice != '3' and choice != '4'):  # input validation
            print("\n**Invalid input, please enter valid numbers!\n")
            choice = input(
                "\n****** Main Menu ****** \n 1 - Customers menu \n 2 - Services menu \n 3 - Key performance indicators and metrics \n 4 - Exit program \n")
        choice = int(choice)  # Convert to int

def main():
    main_menu()  # Call the choice menu
    input()

main()  # Call the main function.