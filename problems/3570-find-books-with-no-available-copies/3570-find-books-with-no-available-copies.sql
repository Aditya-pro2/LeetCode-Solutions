# Write your MySQL query statement below
with cte as (
    select book_id, count(record_id) as current_borrowers
    from borrowing_records
    where return_date is null
    group by book_id
)
select l.book_id, title, author, genre, publication_year, current_borrowers
from cte c, library_books l
where c.book_id = l.book_id and c.current_borrowers = l.total_copies
order by current_borrowers desc, title;