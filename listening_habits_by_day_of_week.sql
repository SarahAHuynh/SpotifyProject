-- Listening habits by day of week (0=Sunday, 6=Saturday)
SELECT 
    CASE CAST(strftime('%w', ts) AS INTEGER)
        WHEN 0 THEN 'Sunday'
        WHEN 1 THEN 'Monday'
        WHEN 2 THEN 'Tuesday'
        WHEN 3 THEN 'Wednesday'
        WHEN 4 THEN 'Thursday'
        WHEN 5 THEN 'Friday'
        WHEN 6 THEN 'Saturday'
    END as day_of_week,
    COUNT(*) as plays,
    ROUND(SUM(ms_played) / 3600000.0, 2) as hours
FROM streaming_history
WHERE master_metadata_track_name IS NOT NULL
GROUP BY strftime('%w', ts)
ORDER BY CAST(strftime('%w', ts) AS INTEGER);