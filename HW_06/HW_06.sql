SELECT *
FROM customers as current_tbl
WHERE (FirstName = 'Mark' AND LastName = 'Taylor') OR (FirstName = 'Frank' AND LastName = 'Harris')
ORDER BY CustomerId ASC;