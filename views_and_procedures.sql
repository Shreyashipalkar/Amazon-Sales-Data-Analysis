CREATE VIEW category_sales AS

SELECT Category,

SUM(Sales) AS TotalSales

FROM sales

GROUP BY Category;
