from rich.console import Console
from rich.table import Table
from filtration import Expression

import stock_data
console=Console()

def add_stock():
    ticker=console.input("[italic]Enter a stock ticker: [/italic]")
    name=console.input("[italic]Enter a name for the stock: [/italic]")
    sector=console.input("[italic]Enter a sector for the stock: [/italic]")
    current_dividend=readFloat("[italic]Enter the current dividend: [/italic]")
    dividend_growth=readFloat("[italic]Enter the dividend growth rate for the last 5 years: [/italic]")
    payout_ratio=readFloat("[italic]Enter the current payout ratio for the stock: [/italic]")
    dividend_rate=readFloat("[italic]Enter the current dividend rate: [/italic]")
    stock_data.stocks[ticker]={'name': name, 'sector': sector, 'current_dividend': current_dividend, 'dividend_growth': dividend_growth, 'payout_ratio': payout_ratio, 'dividend_rate': dividend_rate }

def remove_stock():
    ticker = console.input("[italic]Enter a stock ticker: [/italic]")
    try:
        del stock_data.stocks[ticker]
    except KeyError:
        console.print("Stock not found.", style="bold red")

def show_list():
    print_table(stock_data.stocks)

def calculate_dividends():
    ticker = console.input("[italic]Enter a stock ticker: [/italic]")
    amount = readFloat("[italic]Enter the amount of shares: [/italic]")
    try:
        current_dividend=stock_data.stocks[ticker]['current_dividend']
    except KeyError:
        console.print("Stock not found.", style="bold red")
        return
    console.print(
        f"The total dividend for {amount} shares of {ticker} is {round(stock_data.stocks[ticker]['current_dividend'] * amount, 2)}€", style="bold green")

def filter_data():
    while True:
        expr=console.input("[italic]Enter a filter expression: [/italic]")
        if expr=="help":
            print("Filter expressions are based on the following tokens:")
            print("  name: The name of the stock")
            print("  sector: The sector of the stock")
            print("  current_dividend: The current dividend of the stock")
            print("  dividend_growth: The dividend growth rate for the last 5 years of the stock")
            print("  payout_ratio: The current payout ratio for the stock")
            print("  dividend_rate: The current dividend rate for the stock")
            print("Syntax: [token]operator[value] AND/OR [token]operator[value] ...")
            print("Example: sector=='Technology' AND current_dividend>1.0")
        else:
            break
    parsed=Expression.parseString(expr)
    filtered_stocks={}
    for ticker, data in stock_data.stocks.items():
        if parsed(data):
            filtered_stocks[ticker]=data
    print_table(filtered_stocks)


def readFloat(prompt):
    while True:
        try:
            return float(console.input(prompt))
        except ValueError:
            console.print("Invalid input, please try again.", style="bold red")

def print_table(stocks):
    table = Table(title="Stock Data")
    table.add_column("Ticker", no_wrap=True)
    table.add_column("Name")
    table.add_column("Sector")
    table.add_column("Current Dividend", style="green")
    table.add_column("Dividend Growth (5Y)", style="cyan")
    table.add_column("Payout Ratio")
    table.add_column("Dividend Rate", style="magenta")
    console.print(
        "[bold]Current Stock Data[/bold]", style="bold blue"
    )
    for ticker, data in stocks.items():
        table.add_row(ticker, data['name'], data['sector'], str(data['current_dividend'])+"€", str(data['dividend_growth'])+"%", str(data['payout_ratio'])+"%", str(data['dividend_rate'])+"%")
    console.print(table)