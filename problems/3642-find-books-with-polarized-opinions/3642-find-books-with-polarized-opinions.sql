# Write your MySQL query statement below
select
    book_id,
    title,
    author,
    genre,
    pages,
    max(session_rating) - min(session_rating) as rating_spread,
    round(sum(case when session_rating> 3 or session_rating < 3 then 1 else 0 end) * 1.0 / count(*), 2) as polarization_score
from books join reading_sessions 
using(book_id)
group by 1, 2, 3, 4, 5
having
    count(*) > 4
    and sum(case when session_rating > 3 then 1 else 0 end) > 0
    and sum(case when session_rating < 3 then 1 else 0 end) > 0
    and polarization_score >= 0.6
order by polarization_score desc, title desc