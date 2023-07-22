# task-1,Categories jadval barcha ustun ma’lumotlarini bilan qaytaring.

javob:

```sql
SELECT *
FROM categories
```

![img.png](img.png)

# task-2,Categories jadval category_name va description ustun ma’lumotlarini qaytaring.

javob:

```sql
SELECT category_name, description
from categories
```

![img_1.png](img_1.png)

# task-3,Categories jadval barcha ustun ma’lumotlari olishda ustun nomlarini o’zbekcha tarjimada qaytaring. M-n: category_name=Nomi

javob:

```sql
SELECT category_id AS kategoriya_id, category_name AS kategoriya_nomi, description AS Tavsifi, picture AS Rasm
FROM categories
```

![img_2.png](img_2.png)

# task-4 Categories jadvaldan kategoriya nomi ’Confections’ ga teng bo’lgan ma’lumotlarni qaytaring.

javob:

```sql
SELECT *
FROM categories
WHERE category_name = 'Confections'
```

![img_3.png](img_3.png)

# task-5 Categories jadvaldan kategoriya nomi ‘Produce’ yoki ‘Seafood’ bo’lgan ma’lumotlarni qaytaring.

javob:

```sql
SELECT *
FROM categories
WHERE category_name = 'Produce'
   OR category_name = 'Seafood'
```

![img_4.png](img_4.png)

# TASK-6

![img_5.png](img_5.png)
javob:

```sql
SELECT *
FROM categories
WHERE category_id BETWEEN 6 AND 8
```

![img_6.png](img_6.png)

# TASK-7,Categories jadvaldan ma’lumotlarni description alifbo bo’yicha Z-A tartibida chiqaring.

javob:

```sql
SELECT *
from categories
order by description desc
```

![img_7.png](img_7.png)

# TASK-8, Customers jadvalidan barcha ma’lumotlarni oling

javob:

```sql
SELECT *
from customers
```

![img_8.png](img_8.png)

# TASK-9,Customers jadvalida ustun nomlarini o’zbekcha holatda oling

javob:

```sql
SELECT customer_id   AS mijoz_id,
       company_name  AS kompanina_nomi,
       contact_name  AS mijoz_nomi,
       contact_title as mijoz_unvon,
       address       as manzil,
       city          as shahar,
       region        as viloyat,
       postal_code   as poshta_kodi,
       country       as mamlakat_nomi,
       phone         as telefon_raqami,
       fax           as faks
from customers
```

![img_9.png](img_9.png)

# TASK-10, Customers jadvalidan contact_title ‘Owner’ bo’lgan ma’lumotlarni qaytaring.

javob:

```sql
SELECT *
FROM customers
WHERE contact_title = 'Owner'
```

![img_10.png](img_10.png)

# TASK-11,Customers jadvalidan city ‘London’ bo’lgan ma’lumotlarni qaytaring.

javob:

```sql

SELECT *
FROM customers
WHERE city = 'London'
```

![img_11.png](img_11.png)

# TASK-12,Customers jadvalidan region ustun NULL bo’lgan ma’lumotlarni qaytaring

javob:

```sql
SELECT *
FROM customers
WHERE region is null
```

![img_12.png](img_12.png)

# TASK-13,Customers jadvalidan region ustun NULL bo’lmagan ma’lumotlarni qaytaring.

javob:

```sql
SELECT *
FROM customers
WHERE region is not null
```

![img_13.png](img_13.png)

# TASK-14,Customers jadvalidan country ustun Germany bo’lgan ma’lumotlarni qaytaring.

javob:

```sql
SELECT *
FROM customers
WHERE country = 'Germany'
```

![img_14.png](img_14.png)

# TASK-15,Customers jadvalidan country ustun Germany bo’lgan qatorlar sonini qaytaring.

javob:

```sql
SELECT count(*)
FROM customers
WHERE country = 'Germany'
```

![img_15.png](img_15.png)

# Task-16, Customers jadvalidan fax ustun NULL bo’lmalgan ma’lumotlarni contact_name ustun alifbo tartiba tartiblab qaytaring.

javob:

```sql
SELECT *
FROM customers
WHERE (fax is not null)
order by contact_name
```

![img_16.png](img_16.png)

# Task-17,Employees jadvaldan barcha ma’lumotlarni qaytaring.

javob:

```sql
SELECT *
FROM employees
```

![img_17.png](img_17.png)

#Task-18,Employees jadval ustun nomlarini o’zbekcha qaytaring.
javob:

```sql
SELECT employee_id       as xodim_id,
       last_name         as familya,
       first_name        as ism,
       title             as unvon,
       title_of_courtesy as unvon_boyicha_hurmati,
       birth_date        as tugilgan_malumotlar,
       hire_date         as ish_boshlagan_kun,
       address           as manzil,
       city              as shahar,
       region            as viloyat,
       postal_code       as pochta_kodi,
       country           as mamlakati,
       home_phone        as uy_telefon_raqami,
       extension         as kengaytma,
       photo             as rasm,
       notes             as malumot
FROM employees
```

![img_18.png](img_18.png)

# TAsk-19,Employess jadvaldan title_of_courtest ‘Mr’ bo’lgan xodimlarni firts_name alifbo tartibida qaytaring.

javob:

```sql
SELECT *
FROM employees
WHERE title_of_courtesy = 'Mr.'
order by first_name
```

![img_19.png](img_19.png)

# Task-20,Employes jadvalda title ‘Sales Representative’ bo’lgan xodimlar sonini qaytaring

javob:

```sql
SELECT *
FROM employees
where title = 'Sales Representative'
```

![img_20.png](img_20.png)

# Task-21,Employees jadvalda hire_date 1994-yilda bo’lgan ma’lumotlarni qaytaring.

javob:

```sql
SELECT *
FROM employees
where hire_date between '1994-01-01' and '1994-12-31'
```

![img_21.png](img_21.png)

# Task-22,Employees jadvaldan region NULL bo’lmagan xodimlarni first_name, last_name, title, city,

home_phone ma’lumotlarini first_name Z-A alifbo tartibida qaytaring.
javob:

```sql
SELECT first_name, last_name, title, city, home_phone
FROM employees
WHERE region IS not NULL
order by first_name
```

![img_22.png](img_22.png)

# Task-23,Orders jadvaldan customer_id ‘VINET’ bo’lgan buyurtmalarni qaytaring

javob:

```sql
SELECT *
FROM orders
WHERE customer_id = 'VINET'
```

![img_23.png](img_23.png)

# Task-24,Orders jadvaldan order_date ustuni orqali 1996-yildagi ma’lumotlarni qaytaring

javob:

```sql
SELECT *
FROM orders
WHERE order_date between '1996-01-01' and '1996-12-31'
```

![img_24.png](img_24.png)

# Task-25,Orders jadvaldan ship_region ustun NULL bo’lmagan ma’lumotlarni qaytaring.

javob:

```sql
SELECT *
FROM orders
WHERE ship_region is not null
```

![img_25.png](img_25.png)
javob:

# Task-26,Orders jadvaldan order_id 10300 va 10400 orasida bo’lgan ma’lumotlarni qaytaring

```sql
SELECT *
FROM orders
WHERE order_id between '10300' and '10400'
```

![img_26.png](img_26.png)
![img_27.png](img_27.png)
javob:

# Task-27, Order Details jadvaldan unit_price ustun umumiy qiymatini qaytaring.

```sql
javob
:
SELECT sum(unit_price)
FROM order_details
```

![img_28.png](img_28.png)


