SELECT employee.id,employee.name,department.emp_id,department.name as department name
FROM employee as e, department as d
INNER JOIN d WHERE e.id = d.emp_id;
