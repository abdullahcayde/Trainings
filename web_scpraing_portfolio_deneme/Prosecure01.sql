BEGIN PROSECURE ;

-- 01. Find Daily datas 
CREATE TABLE sildaily as 
SELECT * FROM silall
WHERE (Date_Part('day', date) = Extract(Day from Now())) AND (Date_Part('month', date) = Extract(MONTH from Now()))

-- 02. Add new datas to dailyhours
INSERT INTO dailyhours
SELECT * FROM dailyhours
WHERE lower(publish) LIKE '%stunde%'; 

-- 02. Add new datas to dailyhours
INSERT INTO dailynew
SELECT * FROM dailyshours
WHERE lower(publish) LIKE '%stunde%';

-- 03. Clean 'daily' table
TRUNCATE daily, dailyhours;

CREATE TABLE dailyclean


-- 01. Find Daily datas 
CREATE TABLE sildaily as 
SELECT * FROM silall
WHERE (Date_Part('day', date) = Extract(Day from Now())) AND (Date_Part('month', date) = Extract(MONTH from Now()))

INSERT INTO silhours
SELECT * FROM silall
WHERE lower(publish) LIKE '%stunde%';

CREATE TABLE silhours as
SELECT * FROM sildaily
WHERE lower(publish) LIKE '%stunde%'; 

CREATE TABLE silhoursnoduplicate as
SELECT * FROM silhours;

DELETE FROM silhoursnoduplicate s
    using
    (
        SELECT link,max(ctid) as max_ctid
        FROM silhoursnoduplicate
        GROUP BY link) t
Where s.ctid <> t.max_ctid and s.link = t.link;
----------------------------------
With CTE as
(
	Select *, Row_Number() OVER (Partition by link ) as RN
	from silhoursnoduplicate
)
Delete from CTE Where rn >1 ;

SELECT * FROM silhoursnoduplicate

SELECT * FROM silhours

select id,job_title,publish,city,company,date,link from silhoursnoduplicate order by id
