'''This module handles the functionalities of purchasing a stock'''
# import statements sorted alphabetically
from datetime import datetime
from data_management import *
import fpdf
import pygal 
from utils import *
import yfinance as yf
import os
import errno



#A dictonary that holds the stocks purchased 
total_prices = {}

def app_title():
    """
    A function that Displays the Application title
       Parameters:None
       Returns:
           None:     
    """
    print("*" * 27)
    print(" Stock App")
    print("*" * 27)
def display_menu():
    """
    A function that prompt a user  with menu and returns selection
       Parameters:None
       Returns:
           int: response     
    """
    print("Press 1 to purchase stocks\n")
    print("\nPress 2 to visualize the total prices of selected stocks over the period of time imported from a json file\n")
    print("\nPress 0 to quit\n")
    try:
       response = int(input("\nwaiting for Input: "))
       if response < 0 or response > 2:
           return "Please input a value between 0 and 2"
    except:
        print("Please enter the numeric values specified in the menu")
    else:
        return response
def accept_name():
    """
    A function that prompt a user  to provide Full name returns selection
       Parameters:None
       Returns:
           String: welcome_message     
    """
    try:
       investor_name = input("Enter your Full Name: ")    
    except:
        print("Error when reciving investor name")
    else:
        if len(investor_name) == 0 or  isinstance(investor_name, int):
           print("Please Enter a valid name")
           accept_name()
        else:
           welcome_message =f'\n Greetings {investor_name.title()} Welcome to the Stocks App '
           print(welcome_message)
           return investor_name.title()
def purchase_Stock(investor_name):
    """
    A function that prompt a user  to provide name and number of stocks and
    Plots a summary of investment in  pie chart and generate a recipt in PDF format
       Parameters:None
       Returns:
           None:      
    """
    total_prices = {}
    while True:
        stock_symbol=input("\nEnter the Symbol of the stock you want to purchase: ")
        try:
           temp_stock_variable = yf.Ticker(stock_symbol)
           df = temp_stock_variable.history("today" )
        except Exception as e:
            print(f'purchase_stock function encountered {e} exception')
        else:          
            print(f'\nThe current Stock price for {temp_stock_variable.info ["shortName"]} is: {df.Close[0]}' )
            response = accept_to_proceed_or_quit()    
            if response == 'y' or response =='Y':
                no_share = accept_number_of_shares()
                total_prices[temp_stock_variable.info["symbol"]] = (df.Close[0] * int(no_share))
                                  
                while True:
                    response = proceed_to_payment_or_continue_purchase()
                    if response == 'c' or response =='C':
                        break
                    elif response == 'p' or response =='P':
                        generate_recipt(investor_name, total_prices)
                        generate_investment_summary(total_prices)
                        print("Thank you for using the Stock App.")
                        exit()   
                    elif response == 'n' or response =='N':
                            break
                    elif response == 'q' or response =='Q':
                            exit()
def generate_recipt(investor_name, total_prices):
    """
     A function that  generate a recipt in PDF format
    Parameters:investorn_name and total_price
    Returns:
            None:      
    """
      
    pdf = fpdf.FPDF(format='letter')                  
    total = 0.0
    pdf.add_page() 
    pdf.set_font("Arial", size=12)             
    pdf.cell(200, 10, txt='******************************************', ln=1, align="L")
    pdf.cell(200,10, txt='         Recipt                ',ln=2, align="L")
    pdf.cell(200, 10, txt='******************************************', ln=3, align="L")
    pdf.cell(200,10, txt=f'Date: {datetime.now().strftime("%B %d, %Y")}', ln=4, align="L")
    pdf.cell(200,10, txt=f'Investor Name: {investor_name.title()}', ln=5, align="L")
    pdf.cell(200, 10, txt='******************************************', ln=6, align="L")
    temp =6
    for symbol,individual_cost in total_prices.items():
         pdf.cell(200, 10, txt=f'{symbol}        {individual_cost:.2f}' ,ln=temp+1, align="L" )
    total = calculate_total_price(total_prices)
                                    
    pdf.cell(200,10, txt=f'Your Total excluding tax : {total:.2f}',ln= temp+1,align="L")
    pdf.cell(200, 10, txt='******************************************', ln=temp+1, align="L")
    try:
        os.makedirs("outputs")
    except OSError as exc: 
        if exc.errno != errno.EEXIST:
            raise
    try:
       pdf.output("outputs/recipt.pdf")
    except Exception as e:
        print(f'generate_recipt encountered {e} exception')
def generate_investment_summary(total_prices):
    """
    A function that  generate a summary of the investment in outputs folder with svg format
    Parameters: total_price
    Returns:
            None:      
    """
    pie_chart = pygal.Pie()
    pie_chart.title = 'Percentage of each investment (in %)'
    total = calculate_total_price(total_prices)
    for symbol,individual_cost in total_prices.items():
        pie_chart.add(symbol, individual_cost/total)
    try:                                                            
        pie_chart.render_to_file('outputs/investment_summary.svg')
    except Exception as e:
        print(f'generate_recipt encountered{e} exception')
def calculate_total_price(total_prices):
    """
                A function that  calculates the total using a total_price dictonary
                Parameters: total_price
                Returns:
                        float: total      
    """
    total = 0.0
    for symbol,individual_cost in total_prices.items():
         total += individual_cost
    return total
def accept_number_of_shares():
    try:
        no_share = int(input("\n Please Input the number of shares you want to purchase: "))
        if no_share < 0:
            print("Number of shares can not be negative")
            accept_number_of_shares()
    except Exception as e:
        print(f'accept_number_of_shares encounterd{e} exception')
    else:
        return no_share
def accept_to_proceed_or_quit():
     try:
         response = input(f'\nPress y if you want to purchase the stock and n  purchase another stock and q to exit from the App: ')
         print(response)
         if response == 'y' or response == 'Y' or response == 'n' or response == 'N' or response == 'q' or response == 'Q':
             return response
     except Exception as e:
             print(f'accept_to_proceddd_or_quit encounterd{e} exception')
     else:
         print("Please input y or n or q")
         accept_to_proceed_or_quit()
def proceed_to_payment_or_continue_purchase():
    try:
         response = input("Press c to continue purchasing another stock or P to proceed to payment ")
         if response == 'c' or response == 'C' or response == 'p' or response == 'P':
             return response
    except Exception as e:
             print(f'proceed_to_payment_or_continue_purchase encounterd{e} exception')
    else:
         print("Please input p or c")
         proceed_to_payment_or_continue_purchase()

