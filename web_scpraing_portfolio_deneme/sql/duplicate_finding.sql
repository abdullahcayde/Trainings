SELECT *
    FROM daily
    WHERE ID NOT IN
    (
        SELECT MAX(ID)
        FROM daily
        GROUP BY job_title, 
                 city, 
                 description
    );
	
SELECT *
    FROM daily
    WHERE ID NOT IN
    (
        SELECT MAX(ID)
        FROM daily
        GROUP BY link
    );