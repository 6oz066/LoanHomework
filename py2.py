"""
Date:2024/11/28
Author:
Version:1.0
"""
import matplotlib.pyplot as plt
import numpy as np

# Definition of the loan method
def french_loan(amount,rate,month):
    pass
    month_payment = (amount * ((1+rate)**month))
    for current_month in range(month):
        current_month_amount = amount * (1 + rate)


def american_loan(amount,rate,month):
    month_payment = amount * rate
    month_payment_list=[]
    month_remain_amount=[]
    for current_month in range(month-1):
        month_payment_list.append(month_payment)
        month_remain_amount.append(amount)
    month_payment_list.append(month_payment+amount)
    month_remain_amount.append(0)
    return month_payment_list,month_remain_amount

def italian_loan():
    pass

def geometric_loan():
    pass

def chinese_loan():

    pass

def one_graph(month):
    x_space = np.linspace(0, month, month)

def all_graph(month):
    x_space = np.linspace(0, month, month)


# Insert the information
print("Please choose the method and input the number:\n 1.French \n 2.American \n 3.Italian \n 4.Geometric \n 5.ALL \n ")
method = int(input())
print("Please input your amount to lend")
amount = float(input())
print("Please input your monthly interest rate")
rate = float(input())
print("Please input your month period")
month = int(input())

# Method Decision