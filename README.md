# 📈 Stock Portfolio Tracker

## Overview

Stock Portfolio Tracker is a simple Python application that allows users to manage a basic stock portfolio. Users can enter stock symbols and quantities, and the application calculates the total investment value using predefined stock prices. The project also provides an option to save the portfolio summary to a text file.

## Features

* User-friendly graphical interface using Tkinter
* Add multiple stocks and quantities
* Calculate individual stock investment values
* Display total portfolio value
* Save portfolio reports automatically
* Input validation and error handling

## Technologies Used

* Python 3
* Tkinter (GUI)
* Dictionaries
* File Handling

## Project Structure

```text
StockPortfolioTracker/
│
├── stock_portfolio_tracker.py
├── portfolio_report.txt
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/StockPortfolioTracker.git
```

2. Navigate to the project directory:

```bash
cd StockPortfolioTracker
```

3. Run the application:

```bash
python stock_portfolio_tracker.py
```

## Usage

1. Enter a valid stock symbol (AAPL, TSLA, GOOGL, MSFT, AMZN).
2. Enter the quantity of shares.
3. Click **Add Stock** to add it to your portfolio.
4. Repeat for additional stocks.
5. Click **Calculate Portfolio Value**.
6. View the portfolio summary and total investment value.
7. The report will be saved automatically as `portfolio_report.txt`.

## Example

### Input

* AAPL → 5 shares
* TSLA → 3 shares

### Output

```text
AAPL: 5 × $180 = $900
TSLA: 3 × $250 = $750

Total Portfolio Value = $1650
```

## Learning Outcomes

This project demonstrates:

* Dictionary operations in Python
* User input handling
* Conditional statements
* GUI development with Tkinter
* File handling and report generation

## Future Enhancements

* Real-time stock price integration using APIs
* Portfolio performance visualization
* CSV export functionality
* Database integration

## Author

Developed as part of the CodeAlpha Python Programming Internship.

## License

This project is open-source and available under the MIT License.
