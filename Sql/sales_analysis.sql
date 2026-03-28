CREATE TABLE sales (
    OrderDate TEXT,
    Product TEXT,
    Region TEXT,
    Sales REAL,
    Profit REAL
);

SELECT 
    SUM(Sales) AS TotalSales
FROM sales;

SELECT 
    SUM(Profit) AS TotalProfit
FROM sales;

SELECT 
    Product,
    SUM(Sales) AS TotalSales
FROM sales
GROUP BY Product
ORDER BY TotalSales DESC;

SELECT 
    Product,
    SUM(Profit) AS TotalProfit
FROM sales
GROUP BY Product
ORDER BY TotalProfit DESC;

SELECT 
    Region,
    SUM(Sales) AS TotalSales
FROM sales
GROUP BY Region
ORDER BY TotalSales DESC;

SELECT 
    AVG(Sales) AS AvgOrderValue
FROM sales;