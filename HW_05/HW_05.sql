SELECT TrackId, SUM(UnitPrice), COUNT(*)
FROM invoice_items as current_tbl
GROUP BY TrackId
ORDER BY TrackId ASC;