-- Top 10 artists for each year
WITH artist_year_stats AS (
	SELECT
		strftime('%Y', ts) as year, 
		master_metadata_album_artist_name as artist, 
		COUNT(*) as play_count, 
		ROUND(SUM(ms_played) / 3600000.0, 2) as hours_listened, 
		row_number() OVER (
			PARTITION BY strftime('%Y', ts)
			ORDER BY COUNT(*) DESC
		) as rank 
	FROM streaming_history
	WHERE master_metadata_album_artist_name IS NOT NULL
	GROUP BY year, artist
)

SELECT 
	year, 
	rank, 
	artist, 
	play_count, 
	hours_listened
FROM artist_year_stats
WHERE rank <= 10
ORDER BY year DESC, rank
