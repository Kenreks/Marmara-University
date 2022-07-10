/*
Craete a trigger for OrderItem, so that whenever we insert a new OrderItem along with
the attributes ProductID,OrderID,UnitPrice,Quantity etc. it will update the TotalAmount
attribute of the Order having that OrderItem.
You can assume each insertion to order item would be valid.
*/



/*
Create a stored procedure listing number of orders each customer ordered.
Little not that a customer may not have ordered anything. You have to print zero in this case.

sp_printNumOfOrdersCustomers()
It is to list info about all the customers so there must be total of 91 customers.
*/



/*
This time, find the total number of products EACH customer ordered.
He or she may have ordered these products in different orders.
So, please consider all the products he or she ordered in all his or her order(s).
(HINT: You have to consider Quantity attribute in OrderItem table.)

sp_printNumOfProductsCustomers()
It is to list info about all the customers so there must be total of 91 customers.
*/




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




/*
We want to get the top 10 Suppliers sold maximum number of products.
Consider all the orders bought by all customers.
You should also print out the total amount of money earned by these sells.
It is not a stored procedure. Just writing the query is enough.
*/


/*
Find out how many UNIQUE customers each Supplier has.
For example, if there are two customers bought a product supplied by the supplier 'Pavlova, Ltd.'
then, you should print two along with the company name 'Pavlova, Ltd.'.
You have to join many tables in this question.
It is not a stored procedure. You can just write the query.
*/



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

