# Sales Data Analysis

This project involves analyzing sales data to extract valuable insights and visualize key metrics.

## Project Overview

This project processes and analyzes sales data to generate a comprehensive sales report. The data includes information on orders, products, quantities, prices, dates, sales amounts, and cities.

## Data Overview

The dataset contains the following columns:
- **Order ID**
- **Product**
- **Quantity Ordered**
- **Prices Each (in $)**
- **Order Date**
- **Sales Amount (in $)**
- **City**

## Key Insights

### Overview
- **Total Orders:** 178,437
- **Unique Products:** 19
- **Unique Cities:** 9

### Products Sold
1. **USB-C Charging Cable:** 21,903 sales
2. **Lightning Charging Cable:** 21,658 sales
3. **AAA Batteries (4-pack):** 20,641 sales
4. **AA Batteries (4-pack):** 20,577 sales
5. **Wired Headphones:** 18,882 sales
6. **Apple Airpods Headphones:** 15,549 sales
7. **Bose SoundSport Headphones:** 13,325 sales
8. **27in FHD Monitor:** 7,507 sales
9. **iPhone:** 6,842 sales
10. **27in 4K Gaming Monitor:** 6,230 sales
11. **34in Ultrawide Monitor:** 6,181 sales
12. **Google Phone:** 5,525 sales
13. **Flatscreen TV:** 4,800 sales
14. **Macbook Pro Laptop:** 4,724 sales
...

### Sales by City
- **New York City:** 8 transactions
- **San Francisco:** 9 transactions
- **Atlanta:** 1 transaction
- **Dallas:** 6 transactions
- **Portland:** 4 transactions
- **Boston:** 6 transactions
- **Los Angeles:** 2 transactions
- **Austin:** 1 transaction
- **Seattle:** 1 transaction

### Sales Analysis
- **Total Sales Amount:** $6,306.59
- **Highest Sales Amount:** Order ID 295665 - $1,700.00 (Macbook Pro Laptop)
- **Lowest Sales Amount:** Order ID 295670 - $3.84 (AA Batteries (4-pack))
- **Most Frequent Product:** USB-C Charging Cable (11 sales)
- **Most Expensive Product:** Macbook Pro Laptop ($1,700.00)
- **Least Expensive Product:** AA Batteries (4-pack) ($2.99 per pack)

## Graphical Insights

1. **Histogram of Quantity Ordered:** Most quantities ordered are 1, indicating single item purchases.
2. **Bar Chart of Sales Amount by Product:** USB-C Charging Cable is the most sold product by number of transactions, but Macbook Pro Laptop contributes the highest total sales amount.
3. **Pie Chart of Sales Amount Distribution by City:** San Francisco and New York City dominate in terms of sales amount.
4. **Line Chart of Sales Amount Over Time:** Sales were highest towards the end of the month, indicating possible holiday-related sales spikes.
5. **Scatter Plot of Prices Each vs Sales Amount:** Higher prices tend to correlate with higher sales amounts, but most products are sold at lower price points.
6. **Box Plot of Sales Amount by Product:** Macbook Pro Laptop and Apple Airpods Headphones show higher sales amounts compared to other products.
7. **Heatmap of Correlation:** Sales amount correlates positively with the prices each product is sold at.
8. **Count Plot of Each Product:** USB-C Charging Cable is the most frequently sold item.
9. **Bar Chart of Total Quantity Ordered by City:** San Francisco and New York City have the highest quantities ordered.
10. **Sales Amount by Month:** Sales spike towards the end of the month, with the majority of high-value transactions occurring in the final days of December.

## Running the Analysis

To run the analysis and generate the report, execute the following steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sanath-tejas474/Projects/Projects/Sales_data_analysis.git
