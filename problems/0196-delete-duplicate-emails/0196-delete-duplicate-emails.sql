# Write your MySQL query statement below
delete A from Person A, Person B
where A.email = B.email and A.id > B.id;