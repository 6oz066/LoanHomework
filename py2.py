"""
Date:2024/11/28
Author: ZHANG CHENBING, CHEN WEIQUAN, LI CHENGLONG
Version:1.0
"""
import matplotlib.pyplot as plt
import numpy as np

# Definition of the loan method
def french_loan(amount,rate,month):
    month_payment = (amount * rate *(1+rate)**month)/((1+rate)**month-1)
    month_payment_list = []
    for current_month in range(1,month+1):
        month_payment_list.append(month_payment)
    return  month_payment_list


def american_loan(amount,rate,month):
    month_payment = amount * rate
    month_payment_list=[]
    for current_month in range(1,month):
        month_payment_list.append(month_payment)
    month_payment_list.append(month_payment+amount)
    return month_payment_list


def italian_loan(amount,rate,month):
    month_principal = amount/month
    month_payment_list = []
    for current_month in range(1,month+1):
        month_payment=month_principal+(amount-current_month*month_principal)*rate
        month_payment_list.append(month_payment)
    return month_payment_list


def geometric_loan(amount,rate,month):
    geometric_rate= 0.5 # Here you can change the rate but carefully
    month_principal_initial =(amount * (1-geometric_rate))  / (1-(geometric_rate**month))
    month_payment_list = [month_principal_initial]
    for current_month in range(2,month+1):
        front_amount = amount * (1 + rate) ** (current_month - 1) - month_principal_initial * (1 - geometric_rate) ** (current_month - 1) / (1 - geometric_rate)
        remain_amount = front_amount*(1+rate)- month_principal_initial * geometric_rate**(current_month - 1)
        month_payment = abs(front_amount - remain_amount)
        month_payment_list.append(month_payment)
    return month_payment_list


def chinese_loan(amount,rate,month):
    month_payment = (amount * rate *(1+rate)**month)/((1+rate)**month-1)
    month_payment_list = []
    for current_month in range(1,month+1):
        month_payment_list.append(month_payment)
    return  month_payment_list

def one_graph(month,month_payment_list):
    x_space = np.linspace(1, month, month)
    plt.title("Monthly Loan from the first month")
    plt.plot(x_space,month_payment_list,label="Monthly Payment",marker='o')
    plt.legend()
    plt.show()
    print("The total payment including interest you need to pay is:",sum(month_payment_list))

# Insert the information
method = int(input("Please choose the method and input the number:\n 1.French \n 2.American \n 3.Italian \n 4.Geometric \n 5.Chinese \n 6.ALL\n Please enter:"))
amount = float(input("Please input your amount to borrow:"))
rate = float(input("Please input your monthly interest rate in decimal:"))
month = int(input("Please input your borrowing period (in month):"))
# Method Decision
if method == 1:
    result=french_loan(amount,rate,month)
    one_graph(month, result)
elif method == 2:
    result=american_loan(amount,rate,month)
    one_graph(month,result)
elif method == 3:
    result=italian_loan(amount,rate,month)
    one_graph(month,result)
elif method == 4:
    result=geometric_loan(amount,rate,month)
    one_graph(month, result)
elif method == 5:
    result=chinese_loan(amount,rate,month)
    one_graph(month, result)
elif method == 6:
    french_result = french_loan(amount,rate,month)
    american_result = american_loan(amount,rate,month)
    italian_result = italian_loan(amount,rate,month)
    geometric_result = geometric_loan(amount,rate,month)
    chinese_result = chinese_loan(amount,rate,month)
    # Draw the graph for all methods
    x_space = np.linspace(1, month, month)
    plt.title("Monthly Loan from the first month for all methods")
    plt.plot(x_space,french_result,label="French Loan",marker='o')
    plt.plot(x_space,american_result,label="American Loan",marker='x')
    plt.plot(x_space,italian_result,label="Italian Loan",marker='*')
    plt.plot(x_space,geometric_result,label="Geometric Loan",marker='+')
    plt.plot(x_space,chinese_result,label="Chinese Loan",marker='.')
    print("The total payment including interest you need to pay for French Loan is:", sum(french_result))
    print("The total payment including interest you need to pay for American Loan is:", sum(american_result))
    print("The total payment including interest you need to pay for Italian Loan is:", sum(italian_result))
    print("The total payment including interest you need to pay for Geometric Loan is:", sum(geometric_result))
    print("The total payment including interest you need to pay for Chinese Loan is:", sum(chinese_result))
    plt.legend()
    plt.show()
