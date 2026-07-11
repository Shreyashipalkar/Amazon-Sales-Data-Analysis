-- Total Sales
SELECT SUM(Sales) FROM sales;

-- Total Profit
SELECT SUM(Profit) FROM sales;

-- Total Orders
SELECT COUNT(*) FROM sales;

-- Average Sales
SELECT AVG(Sales) FROM sales;

-- Top 10 Products
SELECT Product_Name,SUM(Sales)
FROM sales
GROUP BY Product_Name
ORDER BY SUM(Sales) DESC
LIMIT 10;

-- Category Wise Sales
SELECT Category,SUM(Sales)
FROM sales
GROUP BY Category;

-- Region Wise Profit
SELECT Region,SUM(Profit)
FROM sales
GROUP BY Region;

-- Monthly Sales
SELECT MONTH(Order_Date),SUM(Sales)
FROM sales
GROUP BY MONTH(Order_Date);

-- Top Customers
SELECT Customer_Name,SUM(Sales)
FROM sales
GROUP BY Customer_Name
ORDER BY SUM(Sales) DESC
LIMIT 10;

-- Highest Discount
SELECT *
FROM sales
ORDER BY Discount DESC;
