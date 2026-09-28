# Blinkit Grocery Sales Analysis

A step-by-step data analysis project using Blinkit grocery sales data. The project cleans inconsistent fat-content labels, calculates business KPIs, answers seven analytical questions, and creates visual dashboards with Python.

## Project Questions and Answers

### Step 1: What are the main business KPIs?

The script calculates:

- **Total Sales:** Overall revenue generated from all items sold.
- **Average Sales:** Average revenue per sale.
- **Number of Items:** Number of unique items based on `Item Identifier`.
- **Average Rating:** Average customer rating.

### Step 2: How does fat content affect sales?

The analysis groups the data by `Item Fat Content` and compares:

- Total Sales
- Average Sales
- Number of Items
- Average Rating

Before analysis, the labels are standardized:

- `LF` becomes `Low Fat`
- `low fat` becomes `Low Fat`
- `reg` becomes `Regular`

### Step 3: Which item types perform best?

The analysis groups sales by `Item Type` and `Item Fat Content`. This identifies the strongest item categories and shows how the four KPIs vary between fat-content groups.

### Step 4: How do outlets perform by fat content?

The analysis compares every `Outlet Identifier` by `Item Fat Content`. This shows which outlets generate the most sales for Low Fat and Regular products.

### Step 5: How are sales distributed by outlet establishment year?

The analysis groups sales by `Outlet Establishment Year` to evaluate how outlet age relates to sales performance.

### Step 6: What percentage of sales comes from each outlet size?

For each `Outlet Size`, the script calculates:

```text
Sales Percentage = Outlet Size Sales / Total Sales * 100
```

This makes it easy to compare the contribution of Small, Medium, and High outlets.

### Step 7: How do location and outlet type affect performance?

The analysis provides:

- Sales and KPIs by `Outlet Location Type`
- Total Sales, Average Sales, Number of Items, and Average Rating by `Outlet Type`

## Visual Results

The Python script creates two dashboard images in the `Images` folder.

### Main Sales Dashboard

[Open the main dashboard](Images/Blinkit_Sales_Analysis.png)

This dashboard contains:

1. Total Sales by Fat Content
2. Total Sales by Item Type and Fat Content
3. Total Sales by Outlet and Fat Content
4. Total Sales by Outlet Establishment Year

### Additional Outlet Dashboard

[Open the additional outlet dashboard](Images/Blinkit_Additional_Analysis.png)

This dashboard contains:

1. Percentage of Sales by Outlet Size
2. Sales by Outlet Location
3. Total Sales by Outlet Type

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV data analysis

## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd "Blinkit Project"
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the analysis

```bash
python Main.py
```

The script prints the KPI tables in the terminal and saves the visual dashboards to the `Images` folder.

## Project Structure

```text
Blinkit Project/
|-- BlinkIT Grocery Data.csv
|-- Main.py
|-- requirements.txt
|-- README.md
|-- Images/
|   |-- Blinkit_Sales_Analysis.png
|   |-- Blinkit_Additional_Analysis.png
|-- SQLQuery_of_Blinkit.sql
```

## Notes

- The CSV file must remain in the same folder as `Main.py`.
- The script uses a path relative to `Main.py`, so it can be run from another working directory.
- The SQL file contains equivalent analysis queries for a database version of the project.
