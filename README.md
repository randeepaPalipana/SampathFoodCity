# 🛒 Sampath Food City — Sales Analysis System

A Python CLI application for analyzing sales data of Sampath Food City (PVT) Ltd across multiple branches. Generates tabular reports and matplotlib charts from a CSV dataset.

## Features

- **Admin login** — single admin account, credential-protected access
- **Branch-Based Sales** — total quantity sold per branch (bar chart)
- **Weekly Sales Summary** — quantity trends by week number (line chart)
- **Product Price Overview** — average price per product (bar chart)
- **Product Popularity** — most sold items by quantity (pie chart)
- **Sales Revenue Distribution** — total revenue per branch (bar chart)
- **Strategy Pattern** — each report type is a separate interchangeable class
- **Unit Tests** — pytest test suite covering branch quantity, product quantity, and branch revenue

## Tech Stack

- Python 3.x
- pandas
- matplotlib
- tabulate
- pytest
- ABC (abstract base class)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/randeepaPalipana/Sampath-food-city.git
cd Sampath-food-city
```

2. Install dependencies:

```bash
pip install pandas matplotlib tabulate pytest
```

## Running the App

```bash
python main.py
```

You will be prompted to log in:

```
Enter username: Sampath
Enter password: 12345
```

Then choose a report from the menu:

```
Choose the Sales Report You Want:
1 - Branch-Based Sales
2 - Weekly Sales Summary
3 - Product Price Overview
4 - Product Popularity
5 - Sales Revenue Distribution
6 - Exit
```

## Running Tests

```bash
# Run all tests
pytest test.py -v

# Run only the data folder tests
pytest data/test_sales_analysis.py -v
```

### Test Coverage

| Test | Type | Description |
|------|------|-------------|
| `test_branch_quantity_positive` | ✅ Positive | Validates correct branch-wise quantity totals |
| `test_branch_quantity_negative` | ❌ Negative | Confirms wrong values raise AssertionError |
| `test_product_quantity_positive` | ✅ Positive | Validates correct product-wise quantity totals |
| `test_product_quantity_negative` | ❌ Negative | Confirms wrong values raise AssertionError |
| `test_branch_revenue_positive` | ✅ Positive | Validates correct branch revenue (Price × Quantity) |
| `test_branch_revenue_negative` | ❌ Negative | Confirms wrong revenue values raise AssertionError |
| `test_discount` | ✅ Positive | Validates 5% discount applied for purchases ≥ LKR 10,000 |

## Project Structure

```
Sampath-food-city/
├── main.py                          # Entry point — Admin login
├── services.py                      # All report strategy classes + MenuHandler
├── test.py                          # Main pytest test suite
├── data/
│   ├── Sampath Food City (PVT) Ltd.csv   # Sales dataset (50 transactions)
│   └── test_sales_analysis.py            # Additional unit tests
```

## Dataset

The CSV contains 50 transactions across 4 branches:

| Column | Description |
|--------|-------------|
| `Transaction_ID` | Unique transaction identifier |
| `Branch` | Colombo, Kandy, Gampaha, or Badulla |
| `Item` | Product name |
| `Price (LKR)` | Unit price in Sri Lankan Rupees |
| `Quantity` | Units sold |
| `Year` / `Month` / `Date` | Transaction date components |

## Design Patterns Used

- **Strategy Pattern** — `SalesAnalysis` is an abstract base class; each report type (`BranchSales`, `WeeklySales`, etc.) implements `analyzeData()` independently
- **Singleton-like Pattern** — `Admin.admin_created` flag prevents multiple admin accounts

## Known Limitations

- Admin credentials are hardcoded (`Sampath` / `12345`)
- Only one admin account is supported
- Dataset is a single static CSV — no database integration
- `test.py` contains extensive commented-out test drafts (earlier versions)