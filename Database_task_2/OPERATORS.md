# TASK 1
```sql
select * from customer where grade > 100;
```
![Снимки экрана](/home/asus/Изображения/Снимки экрана/Снимок экрана от 2023-02-26 16-36-13.png)

# TASK 2 
```sql
select * from customer where city = 'New York' and grade > 100
```
![Снимки экрана](/home/asus/Изображения/Снимки экрана/Снимок экрана от 2023-02-26 16-39-27.png)

# TASK 3
```sql
select * from customer where city = 'New York' or grade > 100
```
![Снимки экрана](/home/asus/Изображения/Снимки экрана/Снимок экрана от 2023-02-26 16-41-27.png)


# TASK 4
```sql
select * from customer where city = 'New York' or not grade > 100
```
![Снимки экрана](/home/asus/Изображения/Снимки экрана/Снимок экрана от 2023-02-26 16-46-38.png)

# TASK 5 
```sql
select * from customer where city <> 'New York' and not grade > 100
```
![Снимки экрана](/home/asus/Изображения/Снимки экрана/Снимок экрана от 2023-02-26 17-17-34.png)

# TASK 6
```sql
select *
from orders
where not (ord_date = '2012-09-10' and salesman_id > 5005 or purch_amt > 1000)
```
![Снимки экрана](/home/asus/Изображения/Снимки экрана/Снимок экрана от 2023-02-26 17-31-00.png)

# TASK 7 
```sql
select *
from salesman
where (commission between 0.10 and 0.12)and commission <> 0.12 
```
![Снимки экрана](/home/asus/Изображения/Снимки экрана/Снимок экрана от 2023-02-26 17-54-03.png)

# TASK 8
```sql
select * from orders where purch_amt 
< 200 or not  ord_date >='2012-02-10'and customer_id < 3009
```
![Снимки экрана](/home/asus/Изображения/Снимки экрана/Снимок экрана от 2023-02-26 18-37-27.png)

# TASK 9
```sql
select * from orders where ord_date = 
'2012-08-17' or not customer_id >3005 and purch_amt < 1000
```
![Снимки экрана](/home/asus/Изображения/Снимки экрана/Снимок экрана от 2023-02-26 18-47-18.png)

# TASK 11
```sql
select * from emp_details where emp_lname in ('Dosni','Mardy')
```
![Снимки экрана](/home/asus/Изображения/Снимки экрана/Снимок экрана от 2023-02-26 18-54-35.png)


# TASK 12
```sql
select * from emp_details where  EMP_DEPT = 47 or EMP_DEPT = 63
```
![Снимки экрана](/home/asus/Изображения/Снимки экрана/Снимок экрана от 2023-02-26 19-01-41.png)































