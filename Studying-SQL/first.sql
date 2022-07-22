SELECT NAME,DATETIME from ANIMAL_INS order by ANIMAL_ID desc;

SELECT NAME,DATETIME from ANIMAL_INS order by ANIMAL_ID asc;

SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) AS count 
from ANIMAL_INS 
where ANIMAL_TYPE in ('Cat','Dog')
group by ANIMAL_TYPE
order by animal_type asc;