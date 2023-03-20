-- En cok is olan sehirler
select lower(company), count(*)
from
	(select * from alldata 
	union all
	select * from daily) t1
group by 1
order by 2 DESC;

-- En cok is olan sehirler
select t1.city, count(*) 
from
	(select * from alldata 
	union all
	select * from daily) t1
group by 1
order by 2 DESC;

-- En ok is basligi
select replace(replace(replace(lower(t1.job_title), ' (m/w/d)', ''), ' (all genders)', ''), ' (w/m/d)', ''), count(*)
from
	(select * from alldata 
	union all
	select * from daily) t1
group by 1
order by 2 DESC;

-- drop duplicate rows
select link, count(*)
from 	
	(select * from alldata 
	union all
	select * from daily) t1
group by 1
having count(*) >1
order by 2 DESC;



select *
from alldata
where lower(job_title) LIKE '%data engineer%';


