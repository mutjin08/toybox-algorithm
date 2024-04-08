select ID, 
case ntile(4) over (order by size_of_colony desc)
    when 1 then 'CRITICAL'
    when 2 then 'HIGH'
    when 3 then 'MEDIUM'
    when 4 then 'LOW'
end as 'COLONY_NAME'
from ecoli_data
order by ID
