# Stock-Program
The Stock program enables an investor to buy a stock or visualize stock data stored in a JSON file. 
When purchasing a stock the program uses the current price accessed from yfinance library. Additionally, 
the program requests the user to provide the number of shares.
After purchasing one or more shares the program requests the user to proceed to payment and print out a summary
of the investment and receipt in PDF format in the output’s directory.
The second functionality requests the user for a JSON file and plots a line graph of the total stocks for the specified period. 
The program uses yfinance to access the latest stock price sqlite3  as a database, pandas to process data, and matplotlib and pygal for visualization.

#To run the program
Excecute the app module.
