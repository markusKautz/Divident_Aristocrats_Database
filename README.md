# Dividend Aristocrats Database

A Python-based command-line application for managing and analyzing dividend stocks. This tool helps investors track and analyze dividend-paying stocks, calculate potential dividend income, and filter stocks based on various criteria.
This is just a simplified version to learn data structures and algorithms.
The initial stocks are hardcoded and not read data and input data is not stored anywhere after the program is closed.

## Features

- **Stock Management**: Add and remove stocks from your portfolio
- **Dividend Calculation**: Calculate potential dividend income based on number of shares
- **Data Visualization**: View stock data in a well-formatted table
- **Filtering**: Filter stocks by various criteria (sector, growth rate, etc.)
- **Rich Interface**: Beautiful console interface with colors and formatting

## Requirements

- Python 3.6+
- Required packages (install via `pip install -r requirements.txt`):
  - rich

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Divident_Aristocrats_Database
   ```

2. Install the required packages:
   ```bash
   pip install rich
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
5. **Filter data**: Filter stocks based on various criteria
6. **Exit**: Close the application

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
