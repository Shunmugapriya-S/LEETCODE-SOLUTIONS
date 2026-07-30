-- -- user higly queried
(select name as results from Users U join MovieRating M on U.user_id=M.user_id group by U.user_id,U.name order by count(*)desc, u.name asc limit 1)
union all
#movie query
(select  title as results from Movies MV join MovieRating M on MV.movie_id =M.movie_id where M.created_at>='2020-02-01' AND M.created_at<'2020-03-01' group by MV.movie_id ,MV.title order by avg(M.rating)  desc, MV.title asc limit 1);