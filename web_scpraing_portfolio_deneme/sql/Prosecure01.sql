BEGIN PROSECURE ;

-- 01. Add new datas to dailyhours
INSERT INTO dailyhours
SELECT * FROM alldata
WHERE Date_Trunc('day', date) = CURRENT_DATE
      AND lower(publish) LIKE '%stunde%'; 

-- 02. Links to go (Data Engineer, Cloud Engineer)

INSERT INTO linkstogo
SELECT id,CURRENT_DATE, job_title,company,link
FROM 
	(Select *, 
		Row_Number() Over (Partition BY job_title,company ) as RN
		From dailyhours) t1
Where RN < 2 AND (lower(job_title) LIKE '%data engineer%' or lower(job_title) LIKE '%cloud%')
             AND Date_Trunc('day', date) = CURRENT_DATE
Order by 4,2




