/*
Craete a trigger for OrderItem, so that whenever we insert a new OrderItem along with
the attributes ProductID,OrderID,UnitPrice,Quantity etc. it will update the TotalAmount
attribute of the Order having that OrderItem.
You can assume each insertion to order item would be valid.
*/

CREATE TRIGGER trg_updateTotalAmount
ON OrderItem
AFTER INSERT
AS
BEGIN
    DECLARE @addition decimal(12,2)
    SET @addition = (SELECT (ot.UnitPrice*ot.Quantity) FROM Inserted ot)

    UPDATE o
    SET o.TotalAmount = o.TotalAmount + @addition
    FROM [Order] o INNER JOIN Inserted ot ON ot.OrderId=o.Id
END

/*
Create a stored procedure listing number of orders each customer ordered.
Little not that a customer may not have ordered anything. You have to print zero in this case.

sp_printNumOfOrdersCustomers()
It is to list info about all the customers so there must be total of 91 customers.
*/


CREATE PROCEDURE sp_printNumOfOrdersCustomers
AS
BEGIN
    SELECT c.FirstName, c.LastName, c.City, c.Country, c.Phone, COUNT(o.Id) AS NumberOfOrders
    FROM Customer c LEFT OUTER JOIN [Order] o ON o.CustomerId=c.Id
    GROUP BY c.Id, c.FirstName, c.LastName, c.City, c.Country, c.Phone
END


/*
This time, find the total number of products EACH customer ordered.
He or she may have ordered these products in different orders.
So, please consider all the products he or she ordered in all his or her order(s).
(HINT: You have to consider Quantity attribute in OrderItem table.)

sp_printNumOfProductsCustomers()
It is to list info about all the customers so there must be total of 91 customers.
*/


CREATE PROCEDURE sp_printNumOfProductsCustomers
AS
BEGIN
    SELECT c.Id, c.FirstName, c.LastName, c.City, c.Country, c.Phone, SUM(CASE WHEN (ot.Id IS NULL) THEN 0 ELSE ot.Quantity END) AS NumberOfTotProducts
    FROM Customer c LEFT OUTER JOIN ([Order] o INNER JOIN OrderItem ot ON o.Id=ot.OrderId) ON o.CustomerId=c.Id
    GROUP BY c.Id, c.FirstName, c.LastName, c.City, c.Country, c.Phone
END


/*
Given @startdate and @enddate,
Create a stored procedure listing top 10 customers who spend their money most.
You have to consider all the orders of the customers between these dates when 
calculating total money spent.

Print; c.Id, c.FirstName, c.LastName, c.City, c.Country, c.Phone of the customer and
the total money spent of the customers.

sp_getTop10Customers()
@startdate datetime,
@enddate datetime
*/


CREATE PROCEDURE sp_getTop10Customers
@startdate datetime,
@enddate datetime
AS
BEGIN
    SELECT TOP(10) c.Id, c.FirstName, c.LastName, c.City, c.Country, c.Phone, SUM(CASE WHEN (o.Id IS NULL) THEN 0 ELSE o.TotalAmount END) AS TotalSpent
    FROM Customer c LEFT OUTER JOIN [Order] o ON c.Id=o.CustomerId
    WHERE o.OrderDate<=@enddate AND o.OrderDate>=@startdate
    GROUP BY c.Id, c.FirstName, c.LastName, c.City, c.Country, c.Phone
    ORDER BY TotalSpent DESC
END


/*
We want to get the top 10 Suppliers sold maximum number of products.
Consider all the orders bought by all customers.
You should also print out the total amount of money earned by these sells.
It is not a stored procedure. Just writing the query is enough.
*/

SELECT TOP(10) s.CompanyName, s.ContactName, SUM(ot.Quantity) AS NumOfProductsSold, SUM(ot.UnitPrice*ot.Quantity) AS TotalMoneyEearned
FROM Supplier s INNER JOIN (Product p INNER JOIN OrderItem ot ON p.Id=ot.ProductId) ON s.Id=p.SupplierId
GROUP BY s.Id, s.CompanyName, s.ContactName
ORDER BY NumOfProductsSold DESC

/*
Find out how many UNIQUE customers each Supplier has.
For example, if there are two customers bought a product supplied by the supplier 'Pavlova, Ltd.'
then, you should print two along with the company name 'Pavlova, Ltd.'.
You have to join many tables in this question.
It is not a stored procedure. You can just write the query.
*/

SELECT s.CompanyName, COUNT(DISTINCT c.Id) AS NumOfUniqueCustomers
FROM Supplier s INNER JOIN Product p ON s.Id=p.SupplierId
                INNER JOIN OrderItem ot ON ot.ProductId=p.Id
                INNER JOIN [Order] o ON o.Id=ot.OrderId
                INNER JOIN Customer c ON c.Id=o.CustomerId
GROUP BY s.Id, s.CompanyName

/*
[MUSTAFA HOCA STYLE - FAMILIAR TO MIDTERM LAST QUESTION]

List the names of the customers and total number of products they bought, for the customers
that ordered multiple times within a month.
The orders must have TotalAmount greater than 1000.

[Hint1]:
Use (DATEDIFF(day,date1,date2) < 30) condition.

[Hint2]:
For example, if Ali ordered in the dates 2012-07-08 and 2012-07-12, then he woud have multiple orderds
within a month. So, his name should be listed along with the total number of products he bought all the time.
*/

SELECT c.Id, c.FirstName, c.LastName, SUM(ot.Quantity) AS TotalNumOfProducts
FROM Customer c INNER JOIN [Order] o ON c.Id=o.CustomerId INNER JOIN OrderItem ot ON ot.OrderId=o.Id
WHERE c.Id IN (
    SELECT c2.Id
    FROM Customer c2 INNER JOIN [Order] o2 ON c2.Id=o2.CustomerId
    WHERE o2.TotalAmount>1000 AND EXISTS(
        SELECT *
        FROM Customer c3 INNER JOIN [Order] o3 ON c3.Id=o3.CustomerId
        WHERE o2.Id!=o3.Id AND c3.Id=c2.Id AND o3.TotalAmount>1000 AND DATEDIFF(day,o3.OrderDate,o2.OrderDate)<30
    )
)
GROUP BY c.Id, c.FirstName, c.LastName
