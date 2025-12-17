--  Top 10 most played artists
SELECT artist_name, COUNT(*) as play_count, 
	ROUND(SUM(ms_played) / 60000.0, 2) as minutes_played
FROM streaming_history
GROUP BY artist_name
ORDER BY play_count DESC
LIMIT 10;

-- Top 10 most played songs 
SELECT track_name, artist_name, COUNT(*) as play_count
FROM streaming_history
-- Track name can be used my multiple artists and vice versa, so have to group by both 
GROUP BY track_name, artist_name
ORDER BY play_count
LIMIT 10;

-- Total listening time 
SELECT ROUND(SUM(ms_played) / 3600000.0 / 2) as total_hours
FROM streaming_history;

-- Listening by hour of day
SELECT strftime('%H', end_time) as hour, 
	COUNT(*) as plays, 
	ROUND(SUM(ms_played) / 60000.0 , 2) as minutes
FROM streaming_history
GROUP BY hour
ORDER BY hour;
