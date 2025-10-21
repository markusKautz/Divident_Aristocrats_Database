# Dividend Aristocrats Database

A Python-based command-line application for managing and analyzing dividend stocks. This tool helps investors track and analyze dividend-paying stocks, calculate potential dividend income, and filter stocks based on various criteria.

## ⚠️ Important Note
This is purely an educational project focused on:
- Python data structures
- Basic financial calculations
- Command-line interfaces using Rich
- Input validation

**Data is stored in memory only and will be lost when the program closes.**

## Features

- **Stock Management**: Add and remove stocks from your portfolio
- **Dividend Calculation**: Calculate potential dividend income based on number of shares
- **Data Visualization**: View stock data in a well-formatted table
- **Advanced Filtering**: Filter stocks using flexible expressions with multiple criteria (sector, dividend yield, growth rate, etc.)
- **Rich Interface**: Beautiful console interface with colors and formatting

## Requirements

- Python 3.6+
- Required packages (install via `pip install -r requirements.txt`):
  - requirement.txt

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/markusKautz/Divident_Aristocrats_Database
   cd Divident_Aristocrats_Database
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python start.py
```

### Main Menu Options

1. **Add a stock**: Add a new stock to the database
2. **Remove a stock**: Remove a stock from the database
3. **Show List**: Display all stocks in a formatted table
4. **Calculate dividends**: Calculate potential dividend income for a stock
5. **Filter Data**: Filter stocks using flexible expressions with multiple criteria
6. **Exit**: Close the application

## Filtering Stocks

The application provides a powerful filtering system that allows you to find stocks based on specific criteria using logical expressions.

### Available Filter Fields
- `name`: The name of the stock (case-insensitive)
- `sector`: The sector the stock belongs to (e.g., 'Technology', 'Healthcare')
- `current_dividend`: The current dividend amount (numeric value)
- `dividend_growth`: The 5-year dividend growth rate (percentage)
- `payout_ratio`: The company's payout ratio (percentage)
- `dividend_rate`: The current dividend rate

### Filter Operators
- Comparison: `==`, `>`, `<`, `>=`, `<=`, `!=`
- Logical: `and`, `or`, `not`
- String matching: `contains` (for partial name or sector matching)

### Examples

Filter for stocks in the Technology sector:
```
sector == 'Technology'
```

Find stocks with dividend growth rate above 5% and payout ratio below 60%:
```
dividend_growth > 5 and payout_ratio < 60
```

Search for stocks with 'Corp' in their name:
```
name contains 'Corp'
```

### Usage Tips
- Type `help` in the filter prompt to see available filter fields
- String values must be enclosed in single quotes ('')
- Multiple conditions can be combined using `and`/`or`
- Use parentheses `()` to group conditions when needed

## Data Structure

Each stock in the database contains the following information:
- Ticker symbol
- Company name
- Sector
- Current dividend
- Dividend growth rate (5-year)
- Payout ratio
- Dividend rate

## Example

### Filtering Example
```
╭─────────────────────────────── Filter Data ──────────────────────────────╮
                                                                          
Enter a filter expression: sector = 'Technology' and dividend_growth > 5

╭─────────┬───────────────┬──────────────┬───────────────────┬───────────────────┬───────────────┬────────────────╮
│ Ticker  │ Name          │ Sector       │ Current Dividend  │ Dividend Growth % │ Payout Ratio  │ Dividend Rate  │
├─────────┼───────────────┼──────────────┼───────────────────┼───────────────────┼───────────────┼────────────────┤
│ MSFT    │ Microsoft     │ Technology   │ 2.72              │ 10.2%             │ 28.5%         │ 0.68           │
│ AAPL    │ Apple Inc.    │ Technology   │ 0.92              │ 5.8%              │ 15.3%         │ 0.23           │
╰─────────┴───────────────┴──────────────┴───────────────────┴───────────────────┴───────────────┴────────────────╯

╭─────────────────────────────────────────────────────────────────────────╮
                                                                         
Press ENTER to continue...
                                                                         
╰─────────────────────────────────────────────────────────────────────────╯
```

### Main Menu
```
Dividend Aristocrats Database
This Program will manage data about dividend stocks and allow filtering and calculating with the data

╭─────────────────────────────── Main Menu ───────────────────────────────╮
                                                                          
        1. Add a stock
        2. Remove a stock
        3. Show List
        4. Calculate dividends
        5. Filter data
        6. Exit
                                                                          
╰─────────────────────────────────────────────────────────────────────────╯
```

## License

This project is open source and available under the [MIT License](LICENSE).
