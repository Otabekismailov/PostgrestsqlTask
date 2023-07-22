# TASK 1

```sql
select *
from salesman
where city in ('Paris', 'Rome');
```

<img src="pictures/Снимок экрана от 2023-02-26 19-13-43.png">


# TASK 3

```sql
select *
from salesman
where city not in ('Paris', 'Rome');
```

<img src="pictures/Снимок экрана от 2023-02-26 19-17-17.png">

# TASK 4

```sql
select *
from customer
where customer_id between 3007 and 3009
```

<img src="pictures/Снимок экрана от 2023-02-26 19-22-08.png">

# TASK 5

```sql
select *
from salesman
where commission between 0.12 and 0.14
```

<img src="pictures/Снимок экрана от 2023-02-26 19-24-56.png">

# TASK 6

```sql
select *
from orders
where purch_amt between 500 and 4000
  and not purch_amt between 948.50 and 1983.43
```

<img src="pictures/Снимок экрана от 2023-02-26 19-34-09.png">

# TASK 7

```sql
select *
from salesman
where name between 'A' and 'L'
```

<img src="pictures/Снимок экрана от 2023-02-26 19-49-31.png">

# TASK 8

```sql
select *
from salesman
where name not between 'A' and 'L'
```

<img src="pictures/Снимок экрана от 2023-02-26 19-51-05.png">

# TASK 9

```sql
select * from customer where cust_name like('B%')
```

<img src="pictures/Снимок экрана от 2023-02-26 19-55-04.png">

# TASK 10
```sql
select * from customer where cust_name like('%n')
```
<img src="pictures/Снимок экрана от 2023-02-26 19-57-53.png">

# TASK 11 
```sql
select * from salesman where name like('N__l%')
```
<img src="pictures/Снимок экрана от 2023-02-26 20-06-35.png">

# TASK 12
```sql
select col1 from testtable where col1 like '%/_%'ESCAPE '/' 
```
<img src="pictures/Снимок экрана от 2023-02-27 12-55-23.png">

# TASK 13
```sql
select col1 from testtable where col1 not like '%/_%'ESCAPE '/'  
```
<img src="pictures/Снимок экрана от 2023-02-27 12-58-05.png">

# TASK 14 
```sql
select * from testtable where col1 like '%//%' escape '/';
```
<img src="pictures/Снимок экрана от 2023-02-27 15-17-21.png">

# TASK 15
```sql
select * from testtable where col1 not like '%//%' escape '/'
```
<img src="pictures/Снимок экрана от 2023-02-27 15-18-44.png">

# TASK 16
```sql
select * from testtable where col1  like '%/_//%' escape '/'
```
<img src="pictures/Снимок экрана от 2023-02-27 15-26-41.png">

# TASK 17
```sql
select * from testtable where col1 not like '%/_//%' escape '/'
```
<img src="pictures/Снимок экрана от 2023-02-27 15-27-50.png">

# TASK 18
```sql
select * from testtable where col1 like '%/%%' escape '/'
```
<img src="pictures/Снимок экрана от 2023-02-27 15-33-05.png">

# TASK 20
```sql
select * from testtable where col1 not like '%/%%' escape '/'
```
<img src="pictures/Снимок экрана от 2023-02-27 15-35-07.png">


# TASK 21
```sql
select * from customer where grade is null
```
<img src="pictures/Снимок экрана от 2023-02-27 15-43-54.png">


# TASK 22
```sql
select * from emp_details where EMP_LNAME like 'D%'
```
<img src="pictures/Снимок экрана от 2023-02-27 15-46-53.png">














