'''

X city opened a new cinema, many people would like to go to this cinema. 
The cinema also gives out a poster indicating the movies’ ratings and descriptions.
Please write a SQL query to output movies with an odd numbered ID and 
a description that is not 'boring'. Order the result by rating.

'''

# Write your MySQL query statement below

SELECT *
FROM cinema
WHERE id%2 <> 0
AND description NOT LIKE '%boring%'
ORDER BY rating DESC;

# Runtime: 374 ms, faster than 5.02%
# Memory Usage: 0B, less than 100.00%

/*
select *
from cinema
where id % 2 = 1 and description != 'boring'
order by rating desc
*/