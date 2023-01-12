SELECT year,
		month,
       sum(close) AS sum_close
FROM hacktiv8.aapl_historical_stock_price
WHERE high>200 and year in (2007,2013)
GROUP BY year,month
HAVING avg(close) > 100
ORDER by month,year;

SELECT date,
       volume,
       close,
       CASE WHEN close > 500 THEN 'yes'
            WHEN close > 300 THEN 'maybe'
            ELSE 'no' END AS big_number
  FROM hacktiv8.aapl_historical_stock_price;

SELECT COUNT(DISTINCT month) AS unique_months
  FROM hacktiv8.aapl_historical_stock_price;

SELECT *
FROM (SELECT year,AVG(close) as mean_close
FROM hacktiv8.aapl_historical_stock_price
GROUP BY year) as sub
WHERE year=2014;

SELECT * FROM hacktiv8.aapl_historical_stock_price
WHERE close > (SELECT AVG(mean_close)
FROM (SELECT year, AVG(CLOSE) AS mean_close
FROM hacktiv8.aapl_historical_stock_price
GROUP BY year) as sub);


SELECT *,sum(close) over() as sum
FROM hacktiv8.aapl_historical_stock_price;

SELECT *,max(close) over(partition by year) as max
FROM hacktiv8.aapl_historical_stock_price;

SELECT *,max(close) over(partition by year order by month) as max
FROM hacktiv8.aapl_historical_stock_price;

USE hacktiv8;
create table employee
( emp_ID int
, emp_NAME varchar(50)
, DEPT_NAME varchar(50)
, SALARY int);
insert into employee values(101, 'Mohan', 'Admin', 4000);
insert into employee values(102, 'Rajkumar', 'HR', 3000);
insert into employee values(103, 'Akbar', 'IT', 4000);
insert into employee values(104, 'Dorvin', 'Finance', 6500);
insert into employee values(105, 'Rohit', 'HR', 3000);
insert into employee values(106, 'Rajesh',  'Finance', 5000);
insert into employee values(107, 'Preet', 'HR', 7000);
insert into employee values(108, 'Maryam', 'Admin', 4000);
insert into employee values(109, 'Sanjay', 'IT', 6500);
insert into employee values(110, 'Vasudha', 'IT', 7000);
insert into employee values(111, 'Melinda', 'IT', 8000);
insert into employee values(112, 'Komal', 'IT', 10000);
insert into employee values(113, 'Gautham', 'Admin', 2000);
insert into employee values(114, 'Manisha', 'HR', 3000);
insert into employee values(115, 'Chandni', 'IT', 4500);
insert into employee values(116, 'Satya', 'Finance', 6500);
insert into employee values(117, 'Adarsh', 'HR', 3500);
insert into employee values(118, 'Tejaswi', 'Finance', 5500);
insert into employee values(119, 'Cory', 'HR', 8000);
insert into employee values(120, 'Monica', 'Admin', 5000);
insert into employee values(121, 'Rosalin', 'IT', 6000);
insert into employee values(122, 'Ibrahim', 'IT', 8000);
insert into employee values(123, 'Vikram', 'IT', 8000);
insert into employee values(124, 'Dheeraj', 'IT', 11000);

select * from hacktiv8.employee;

select * ,
max(salary) over(partition by dept_name order by emp_ID desc) as max_salary,
min(salary) over(partition by dept_name order by emp_ID desc) as min_salary,
avg(salary) over(partition by dept_name order by emp_ID desc) as avg_salary
from hacktiv8.employee;

-- ROW_NUMBER()
select *,
row_number() over(partition by year) as rn
from hacktiv8.aapl_historical_stock_price;

select *,
row_number() over(partition by year order by month) as rn
from hacktiv8.aapl_historical_stock_price;

select *
from(select *,
row_number() over(partition by year order by month) as rn
from hacktiv8.aapl_historical_stock_price) as data
where mod(rn,2)=1;

select *
from(select *,
row_number() over(partition by year order by month) as rn
from hacktiv8.aapl_historical_stock_price) as data
where rn in (25,30);

-- RANK()
select *,
rank() over(partition by dept_name order by salary desc) as rank_salary
from hacktiv8.employee;

-- DENSE_RANK()
select *,
dense_rank() over(partition by dept_name order by salary desc) as rank_salary
from hacktiv8.employee;

-- NTILE()
select *,
ntile(4) over(partition by month) as bucket
from hacktiv8.aapl_historical_stock_price;

select *,
ntile(4) over(partition by month) as bucket
from hacktiv8.aapl_historical_stock_price
order by close desc;

-- LAG() LEAD()
select *,
lag(close,2) over() as diff_atas,
lead(close,2) over() as diff_bawah
from hacktiv8.aapl_historical_stock_price;

select *, case when selisih > 0 then 'untung'
else 'rugi' end as hasil_trading
from
(select *,
lag(close,2) over() as diff_atas,
lead(close,2) over() as diff_bawah,
close - lag(close,2) over() as selisih
from hacktiv8.aapl_historical_stock_price) as data;

select *,
ntile(4) over(partition by year)
from (select 
distinct year,
max(close)
from hacktiv8.aapl_historical_stock_price
group by year) as impostor;
