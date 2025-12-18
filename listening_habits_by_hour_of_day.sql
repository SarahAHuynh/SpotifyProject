-- Listening habits by hour of day
SELECT
	CAST(strftime('%H', ts) AS INTEGER) as hour, 
	COUNT(*) as plays, 
	ROUND(SUM(ms_played) / 3600000.0, 2) as hours
FROM streaming_history
WHERE master_metadata_track_name IS NOT NULL
GROUP BY hour
ORDER BY hour;
