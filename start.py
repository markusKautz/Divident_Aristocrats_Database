import stock_data
from stock_functions import add_stock, remove_stock, show_list, calculate_dividends, filter_data
from rich.console import Console

console = Console()
console.print("Dividend Aristocrats Database", style="yellow bold")
console.print("This Program will manage data about dividend stocks and allow filtering and calculating with the data", style="blue italic")
console.print("Press CTRL + C to exit.", style="bold")
console.print("Press ENTER to continue.", style="bold")
input()

while True:
    console.rule("[bold green]Main Menu[/bold green]")
    console.print(
        """
        [green]1.[/green] Add a stock
        [green]2.[/green] Remove a stock
        [green]3.[/green] Show List
        [green]4.[/green] Calculate dividends
        [green]5.[/green] Filter data
        [green]6.[/green] Exit
        """,
        style="bold", )
    select = int(console.input("[italic]Choose a function[1-6]: [/italic]"))
    match select:
        case 1:
            console.rule("[bold green]Add a Stock[/bold green]")
            add_stock()
        case 2:
            console.rule("[bold green]Remove a Stock[/bold green]")
            remove_stock()
        case 3:
            console.rule("[bold green]Show List[/bold green]")
            show_list()
        case 4:
            console.rule("[bold green]Calculate Dividends[/bold green]")
            calculate_dividends()
        case 5:
            console.rule("[bold green]Filter Data[/bold green]")
            filter_data()
        case 6:
            console.print("Exiting...", style="blue italic")
            break