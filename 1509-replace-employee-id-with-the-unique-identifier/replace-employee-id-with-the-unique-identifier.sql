# Write your MySQL query statement below
select e.name, u.unique_id
from EmployeeUNI u
right join Employees e
on e.id=u.id; 