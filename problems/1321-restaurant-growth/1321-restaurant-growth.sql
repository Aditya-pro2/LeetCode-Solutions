# Write your MySQL query statement below
select visited_on, amount, round(amount / 7, 2) as average_amount
from
(select distinct visited_on, sum(amount) over(order by visited_on range between interval 6 day preceding and current row) as amount, min(visited_on) over() as date
from Customer) as T
where visited_on >= date + 6;