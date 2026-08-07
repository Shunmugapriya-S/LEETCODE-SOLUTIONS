-- # Write your MySQL query statement below
-- select patient_id,patient_name,conditions
-- from Patients
-- WHERE instr(concat('',conditions,''),'DIAB1')>0;
# Write your MySQL query statement below
select patient_id,patient_name,conditions
from Patients
WHERE conditions like 'DIAB1%' or conditions like '% DIAB1%';