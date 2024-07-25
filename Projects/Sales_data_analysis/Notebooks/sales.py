# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv(r"C:\Users\yuria\Desktop\projects\Projects\Sales_data_analysis\data\Data_trannsformed.csv")

# Total Orders
total_orders = data['Order ID'].nunique()

# Unique Products
unique_products = data['Product'].nunique()

# Unique Cities
unique_cities = data['City'].nunique()

# Products Sold
products_sold = data['Product'].value_counts()

# Sales by City
sales_by_city = data['City'].value_counts()

# Total Sales Amount
total_sales_amount = data['Sales Amount in $'].sum()

# Highest Sales Amount
highest_sales_amount = data[data['Sales Amount in $'] == data['Sales Amount in $'].max()]

# Lowest Sales Amount
lowest_sales_amount = data[data['Sales Amount in $'] == data['Sales Amount in $'].min()]

# Most Frequent Product
most_frequent_product = data['Product'].mode()[0]

# Most Expensive Product
most_expensive_product = data[data['Prices Each in $'] == data['Prices Each in $'].max()]

# Least Expensive Product
least_expensive_product = data[data['Prices Each in $'] == data['Prices Each in $'].min()]

# Create visualizations

# 1. Histogram of Quantity Ordered
plt.figure(figsize=(10, 6))
sns.histplot(data['Quantity Ordered'], bins=20, kde=True)
plt.title('Histogram of Quantity Ordered')
plt.xlabel('Quantity Ordered')
plt.ylabel('Frequency')
plt.savefig(r'C:\Users\yuria\Desktop\projects\Projects\Sales_data_analysis\Analytical_pics/histogram_quantity_ordered.png')
plt.show()

# 2. Bar Chart of Sales Amount by Product
plt.figure(figsize=(12, 8))
product_sales = data.groupby('Product')['Sales Amount in $'].sum().sort_values(ascending=False)
product_sales.plot(kind='bar')
plt.title('Sales Amount by Product')
plt.xlabel('Product')
plt.ylabel('Sales Amount in $')
plt.savefig(r'C:\Users\yuria\Desktop\projects\Projects\Sales_data_analysis\Analytical_pics/bar_sales_amount_by_product.png')
plt.show()

# 3. Pie Chart of Sales Amount Distribution by City
plt.figure(figsize=(10, 8))
city_sales = data.groupby('City')['Sales Amount in $'].sum()
city_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales Amount Distribution by City')
plt.ylabel('')
plt.savefig(r'C:\Users\yuria\Desktop\projects\Projects\Sales_data_analysis\Analytical_pics/pie_sales_amount_by_city.png')
plt.show()

# 4. Line Chart of Sales Amount Over Time
data['Order Date'] = pd.to_datetime(data['Order Date'])
data.set_index('Order Date', inplace=True)
monthly_sales = data.resample('M')['Sales Amount in $'].sum()
plt.figure(figsize=(12, 6))
monthly_sales.plot()
plt.title('Sales Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Amount in $')
plt.savefig(r'C:\Users\yuria\Desktop\projects\Projects\Sales_data_analysis\Analytical_pics/line_sales_amount_over_time.png')
plt.show()

# 5. Scatter Plot of Prices Each vs Sales Amount
plt.figure(figsize=(10, 6))
plt.scatter(data['Prices Each in $'], data['Sales Amount in $'])
plt.title('Prices Each vs Sales Amount')
plt.xlabel('Prices Each in $')
plt.ylabel('Sales Amount in $')
plt.savefig(r'C:\Users\yuria\Desktop\projects\Projects\Sales_data_analysis\Analytical_pics/scatter_prices_each_vs_sales_amount.png')
plt.show()

# 6. Box Plot of Sales Amount by Product
plt.figure(figsize=(12, 8))
sns.boxplot(x='Product', y='Sales Amount in $', data=data)
plt.title('Sales Amount by Product')
plt.xticks(rotation=90)
plt.savefig(r'C:\Users\yuria\Desktop\projects\Projects\Sales_data_analysis\Analytical_pics/box_sales_amount_by_product.png')
plt.show()

# 7. Heatmap of Correlation
plt.figure(figsize=(10, 8))
correlation = data[['Quantity Ordered', 'Prices Each in $', 'Sales Amount in $']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig(r'C:\Users\yuria\Desktop\projects\Projects\Sales_data_analysis\Analytical_pics/heatmap_correlation.png')
plt.show()

# 8. Count Plot of Each Product
plt.figure(figsize=(12, 8))
sns.countplot(y='Product', data=data, order=data['Product'].value_counts().index)
plt.title('Count of Each Product')
plt.xlabel('Count')
plt.ylabel('Product')
plt.savefig(r'C:\Users\yuria\Desktop\projects\Projects\Sales_data_analysis\Analytical_pics/countplot_each_product.png')
plt.show()

# 9. Bar Chart of Total Quantity Ordered by City
plt.figure(figsize=(12, 8))
city_quantity = data.groupby('City')['Quantity Ordered'].sum().sort_values(ascending=False)
city_quantity.plot(kind='bar')
plt.title('Total Quantity Ordered by City')
plt.xlabel('City')
plt.ylabel('Total Quantity Ordered')
plt.savefig(r'C:\Users\yuria\Desktop\projects\Projects\Sales_data_analysis\Analytical_pics/bar_quantity_ordered_by_city.png')
plt.show()

# 10. Sales Amount by Month
monthly_sales = data.resample('M')['Sales Amount in $'].sum()
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='bar')
plt.title('Sales Amount by Month')
plt.xlabel('Month')
plt.ylabel('Sales Amount in $')
plt.savefig(r'C:\Users\yuria\Desktop\projects\Projects\Sales_data_analysis\Analytical_pics/bar_sales_amount_by_month.png')
plt.show()

# Report
report = f"""
===============================
         Sales Data Report
===============================

Overview:
- Total Orders: {total_orders}
- Unique Products: {unique_products}
- Unique Cities: {unique_cities}

Products Sold:
"""

for i, (product, count) in enumerate(products_sold.items(), 1):
    report += f"{i}. {product}: {count} sale{'s' if count > 1 else ''}\n"

report += f"""

Sales by City:
"""

for city, count in sales_by_city.items():
    report += f"- {city}: {count} transaction{'s' if count > 1 else ''}\n"

report += f"""

Sales Analysis:
- Total Sales Amount: ${total_sales_amount:.2f}
- Highest Sales Amount: Order ID {highest_sales_amount['Order ID'].values[0]} - ${highest_sales_amount['Sales Amount in $'].values[0]:.2f} ({highest_sales_amount['Product'].values[0]})
- Lowest Sales Amount: Order ID {lowest_sales_amount['Order ID'].values[0]} - ${lowest_sales_amount['Sales Amount in $'].values[0]:.2f} ({lowest_sales_amount['Product'].values[0]})
- Most Frequent Product: {most_frequent_product} ({products_sold[most_frequent_product]} sales)
- Most Expensive Product: {most_expensive_product['Product'].values[0]} (${most_expensive_product['Prices Each in $'].values[0]:.2f})
- Least Expensive Product: {least_expensive_product['Product'].values[0]} (${least_expensive_product['Prices Each in $'].values[0]:.2f})

Graphical Insights:
1. Histogram of Quantity Ordered: Most quantities ordered are 1, indicating single item purchases.
2. Bar Chart of Sales Amount by Product: USB-C Charging Cable is the most sold product by number of transactions, but Macbook Pro Laptop contributes the highest total sales amount.
3. Pie Chart of Sales Amount Distribution by City: San Francisco and New York City dominate in terms of sales amount.
4. Line Chart of Sales Amount Over Time: Sales were highest towards the end of the month, indicating possible holiday-related sales spikes.
5. Scatter Plot of Prices Each vs Sales Amount: Higher prices tend to correlate with higher sales amounts, but most products are sold at lower price points.
6. Box Plot of Sales Amount by Product: Macbook Pro Laptop and Apple Airpods Headphones show higher sales amounts compared to other products.
7. Heatmap of Correlation: Sales amount correlates positively with the prices each product is sold at.
8. Count Plot of Each Product: USB-C Charging Cable is the most frequently sold item.
9. Bar Chart of Total Quantity Ordered by City: San Francisco and New York City have the highest quantities ordered.
10. Sales Amount by Month: Sales spike towards the end of the month, with the majority of high-value transactions occurring in the final days of December.

Conclusions:
- San Francisco and New York City are the top cities contributing to the overall sales.
- USB-C Charging Cable is the most frequently purchased product, while the Macbook Pro Laptop generates the highest revenue.
- The data shows a significant increase in sales towards the end of the month, possibly driven by holiday shopping.

===============================
"""

print(report)


# %%



