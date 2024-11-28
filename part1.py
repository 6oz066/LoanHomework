"""
Date:
Author: <NAME>
Version:
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the amortization methods
def italian_amortization(C, i, n):
#     A = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
    O=C/n    
#     A=C*i/(1-(1-i)**n)
    am = []
    x=[]
    for s in range(1,n+1):
        A=O+(C-s*O)*i
        am.append(A)
        x.append(s)
    return x,am

def french_amortization(C, i, n):
    A = C * i * (1 + i) ** n / ((1 + i) ** n - 1)
    am = []
    x=[]
    for s in range(1,n+1):
        am.append(A)
        x.append(s)
    return x,am

def american_amortization(C, i, n):
    A = C *i
    am = []
    x=[]
    for s in range(1,n):
        am.append(A)
        x.append(s)
    am.append(C*i+C)
    x.append(n)
    return x,am

def geometric_amortization(C, i, n):
    numerator = C * (1 + i) * (1 - q**n)
    denominator = sum((1 + i)**k * q**(n-1-k) for k in range(n))
    a = numerator / denominator
    
    am = []
    x = []
    
    for s in range(1, n + 1):
        am.append(a * q**(s-1))
        x.append(s)
    
    return x, am
#     A = C * (1-i) / (1 - i ** (n))
#     am = []
#     x=[]
#     for s in range(1,n+1):
#         am.append(A)
#         x.append(s)
#     return x,am

# Function to calculate the amortization schedule
def calculate_schedule(method, P, r, n):
    if method == 'Italian':
        return italian_amortization(P, r, n)
    elif method == 'French':
        return french_amortization(P, r, n)
    elif method == 'American':
        return american_amortization(P, r, n)
    elif method == 'Geometric':
        return geometric_amortization(P, r, n)
    else:
        raise ValueError("Method not recognized")

# Function to visualize the comparison across methods
def visualize_amortization(methods, P, r, n):
    plt.figure(figsize=(10, 6))
    for method in methods:
        x,payments = calculate_schedule(method, P, r, n)
        plt.plot(x,payments, label=method)
    print(x,payments)
    plt.xlabel('Period')
    plt.ylabel('Payment')
    plt.title('Amortization Method Comparison')
    plt.legend()
    plt.show()

# Function to save results to an Excel file
def save_to_excel(methods, P, r, n, filename):
    with pd.ExcelWriter(filename) as writer:
        for i, method in enumerate(methods):
            df = pd.DataFrame(calculate_schedule(method, P, r, n), columns=['Payment'])
            df.to_excel(writer, sheet_name=method)

# User input for method selection
print("Select the amortization methods to include (type the names separated by commas):")
user_input = input("Italian, French, American, Geometric: ")
methods = [method.strip() for method in user_input.split(',')]

# Loan parameters
principal = float(input("Enter the principal amount (P): "))
rate = float(input("Enter the annual interest rate (r) as a decimal: "))
periods = int(input("Enter the number of periods (n): "))

# Calculate and visualize
visualize_amortization(methods, principal, rate, periods)