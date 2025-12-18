DROP TABLE IF EXISTS streaming_history;

CREATE TABLE streaming_history (
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	ts TEXT, 
	username TEXT,
	platform TEXT, 
	ms_played INTEGER, 
	conn_country TEXT, 
	ip_addr_decrypted TEXT, 
	user_agent_decrypted TEXT, 
	master_metadata_track_name TEXT, 
	master_metadata_album_artist_name TEXT, 
	master_metadata_album_album_name TEXT, 
	spotify_track_uri TEXT, 
	episode_name TEXT, 
	episode_show_name TEXT, 
	reason_start TEXT,
    reason_end TEXT,
    shuffle INTEGER,
    skipped INTEGER,
    offline INTEGER,
    offline_timestamp INTEGER,
    incognito_mode INTEGER
);