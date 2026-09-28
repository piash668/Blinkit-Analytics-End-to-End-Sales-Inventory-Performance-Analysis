from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_FILE = Path(__file__).parent / "BlinkIT Grocery Data.csv"
df = pd.read_csv(DATA_FILE)
df["Item Fat Content"] = df["Item Fat Content"].replace(
	{"LF": "Low Fat", "low fat": "Low Fat", "reg": "Regular"}
)

print(f"Loaded {len(df):,} rows and {len(df.columns)} columns from {DATA_FILE.name}")
print("Item Fat Content values:", sorted(df["Item Fat Content"].dropna().unique()))
print(df.head())

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
number_of_items = df["Item Identifier"].nunique()
average_rating = df["Rating"].mean()

print(f"Total Sales: {total_sales:,.2f}")
print(f"Average Sales: {average_sales:,.2f}")
print(f"Number of Items: {number_of_items:,}")
print(f"Average Rating: {average_rating:.2f}")

# 1. ANSWER: This table shows how total sales and the other KPIs vary by fat content.
sales_by_fat_content = (
	df.groupby("Item Fat Content", as_index=False)
	.agg(
		Total_Sales=("Sales", "sum"),
		Average_Sales=("Sales", "mean"),
		Number_of_Items=("Item Identifier", "nunique"),
		Average_Rating=("Rating", "mean"),
	)
	.sort_values("Total_Sales", ascending=False)
)
print("\n1. Total Sales and KPIs by Fat Content")
print(sales_by_fat_content.to_string(index=False))

# 2. ANSWER: This table identifies the best-performing item types, split by fat content.
sales_by_item_type = (
	df.groupby(["Item Type", "Item Fat Content"], as_index=False)
	.agg(
		Total_Sales=("Sales", "sum"),
		Average_Sales=("Sales", "mean"),
		Number_of_Items=("Item Identifier", "nunique"),
		Average_Rating=("Rating", "mean"),
	)
	.sort_values("Total_Sales", ascending=False)
)
print("\n2. Total Sales and KPIs by Item Type and Fat Content")
print(sales_by_item_type.to_string(index=False))

# 3. ANSWER: This table compares outlet sales and KPIs for each fat-content segment.
sales_by_outlet_fat_content = (
	df.groupby(["Outlet Identifier", "Item Fat Content"], as_index=False)
	.agg(
		Total_Sales=("Sales", "sum"),
		Average_Sales=("Sales", "mean"),
		Number_of_Items=("Item Identifier", "nunique"),
		Average_Rating=("Rating", "mean"),
	)
	.sort_values("Total_Sales", ascending=False)
)
print("\n3. Total Sales and KPIs by Outlet and Fat Content")
print(sales_by_outlet_fat_content.to_string(index=False))

# 4. ANSWER: This table shows how total sales change by outlet establishment year.
sales_by_establishment = (
	df.groupby("Outlet Establishment Year", as_index=False)
	.agg(
		Total_Sales=("Sales", "sum"),
		Average_Sales=("Sales", "mean"),
		Number_of_Items=("Item Identifier", "nunique"),
		Average_Rating=("Rating", "mean"),
	)
	.sort_values("Outlet Establishment Year")
)
print("\n4. Total Sales and KPIs by Outlet Establishment Year")
print(sales_by_establishment.to_string(index=False))

# 5. ANSWER: This table shows each outlet-size group's share of overall sales.
sales_by_outlet_size = (
	df.groupby("Outlet Size", as_index=False)
	.agg(Total_Sales=("Sales", "sum"))
)
sales_by_outlet_size["Sales_Percentage"] = (
	sales_by_outlet_size["Total_Sales"] / total_sales * 100
)
sales_by_outlet_size = sales_by_outlet_size.sort_values(
	"Sales_Percentage", ascending=False
)
print("\n5. Percentage of Sales by Outlet Size")
print(sales_by_outlet_size.to_string(index=False, formatters={
	"Total_Sales": "{:,.2f}".format,
	"Sales_Percentage": "{:.2f}%".format,
}))

# 6. ANSWER: This table compares the geographic sales distribution by location tier.
sales_by_location = (
	df.groupby("Outlet Location Type", as_index=False)
	.agg(
		Total_Sales=("Sales", "sum"),
		Average_Sales=("Sales", "mean"),
		Number_of_Items=("Item Identifier", "nunique"),
		Average_Rating=("Rating", "mean"),
	)
	.sort_values("Total_Sales", ascending=False)
)
print("\n6. Sales and KPIs by Outlet Location")
print(sales_by_location.to_string(index=False))

# 7. ANSWER: This table provides all key metrics for every outlet type.
metrics_by_outlet_type = (
	df.groupby("Outlet Type", as_index=False)
	.agg(
		Total_Sales=("Sales", "sum"),
		Average_Sales=("Sales", "mean"),
		Number_of_Items=("Item Identifier", "nunique"),
		Average_Rating=("Rating", "mean"),
	)
	.sort_values("Total_Sales", ascending=False)
)
print("\n7. All Metrics by Outlet Type")
print(metrics_by_outlet_type.to_string(index=False))

# VISUAL DASHBOARD: This displays steps 1-4 visually.
figure, axes = plt.subplots(2, 2, figsize=(16, 11))
figure.suptitle("Blinkit Sales Analysis Dashboard", fontsize=18, fontweight="bold")

# Visual answer 1: total sales comparison between fat-content categories.
axes[0, 0].bar(
	sales_by_fat_content["Item Fat Content"],
	sales_by_fat_content["Total_Sales"],
	color=["#2a9d8f", "#e76f51"],
)
axes[0, 0].set_title("Total Sales by Fat Content")
axes[0, 0].set_ylabel("Total Sales")

# Visual answer 2: item-type sales, with fat content shown as stacked segments.
item_type_chart = sales_by_item_type.pivot(
	index="Item Type", columns="Item Fat Content", values="Total_Sales"
).fillna(0)
item_type_chart.sort_values("Low Fat").plot.barh(
	stacked=True, ax=axes[0, 1], color=["#2a9d8f", "#e76f51"]
)
axes[0, 1].set_title("Total Sales by Item Type and Fat Content")
axes[0, 1].set_xlabel("Total Sales")
axes[0, 1].set_ylabel("")
axes[0, 1].legend(title="Fat Content")

# Visual answer 3: outlet sales, with fat content shown as stacked segments.
outlet_chart = sales_by_outlet_fat_content.pivot(
	index="Outlet Identifier", columns="Item Fat Content", values="Total_Sales"
).fillna(0)
outlet_chart.plot.bar(
	stacked=True, ax=axes[1, 0], color=["#2a9d8f", "#e76f51"]
)
axes[1, 0].set_title("Total Sales by Outlet and Fat Content")
axes[1, 0].set_ylabel("Total Sales")
axes[1, 0].set_xlabel("Outlet")
axes[1, 0].tick_params(axis="x", rotation=45)
axes[1, 0].legend(title="Fat Content")

# Visual answer 4: sales trend by outlet establishment year.
axes[1, 1].plot(
	sales_by_establishment["Outlet Establishment Year"],
	sales_by_establishment["Total_Sales"],
	marker="o",
	color="#264653",
)
axes[1, 1].set_title("Total Sales by Outlet Establishment Year")
axes[1, 1].set_xlabel("Establishment Year")
axes[1, 1].set_ylabel("Total Sales")
axes[1, 1].grid(axis="y", alpha=0.3)

figure.tight_layout()
figure_path = Path(__file__).parent / "Images" / "Blinkit_Sales_Analysis.png"
figure_path.parent.mkdir(exist_ok=True)
figure.savefig(figure_path, dpi=150, bbox_inches="tight")
print(f"\nVisual dashboard saved to: {figure_path}")

# Visual answers 5-7: additional charts for outlet size, location, and type.
additional_figure, additional_axes = plt.subplots(1, 3, figsize=(18, 6))
additional_figure.suptitle(
	"Blinkit Additional Outlet Analysis", fontsize=18, fontweight="bold"
)

additional_axes[0].bar(
	sales_by_outlet_size["Outlet Size"],
	sales_by_outlet_size["Sales_Percentage"],
	color="#2a9d8f",
)
additional_axes[0].set_title("Percentage of Sales by Outlet Size")
additional_axes[0].set_ylabel("Sales Percentage (%)")

additional_axes[1].bar(
	sales_by_location["Outlet Location Type"],
	sales_by_location["Total_Sales"],
	color="#e76f51",
)
additional_axes[1].set_title("Sales by Outlet Location")
additional_axes[1].set_ylabel("Total Sales")

additional_axes[2].bar(
	metrics_by_outlet_type["Outlet Type"],
	metrics_by_outlet_type["Total_Sales"],
	color="#264653",
)
additional_axes[2].set_title("Total Sales by Outlet Type")
additional_axes[2].set_ylabel("Total Sales")
additional_axes[2].tick_params(axis="x", rotation=45)

additional_figure.tight_layout()
additional_figure_path = (
	Path(__file__).parent / "Images" / "Blinkit_Additional_Analysis.png"
)
additional_figure.savefig(additional_figure_path, dpi=150, bbox_inches="tight")
print(f"Additional visual dashboard saved to: {additional_figure_path}")
plt.show()


