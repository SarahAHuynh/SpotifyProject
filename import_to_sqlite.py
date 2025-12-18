import json
import sqlite3
import os
import glob

# Connect to your database (replace with your actual .db filename)
conn = sqlite3.connect('spotifyDatabase.db')
cursor = conn.cursor()

# Find all JSON files (adjust the pattern if your files are named differently)
json_files = glob.glob('Streaming_History*.json')  # or 'StreamingHistory*.json'

total_records = 0

for json_file in json_files:
    print(f"Processing {json_file}...")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        cursor.execute('''
            INSERT INTO streaming_history (
                ts, username, platform, ms_played, conn_country,
                ip_addr_decrypted, user_agent_decrypted,
                master_metadata_track_name, master_metadata_album_artist_name,
                master_metadata_album_album_name, spotify_track_uri,
                episode_name, episode_show_name, spotify_episode_uri,
                reason_start, reason_end, shuffle, skipped, offline,
                offline_timestamp, incognito_mode)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            item.get('ts'),
             item.get('username'),
            item.get('platform'),
            item.get('ms_played'),
            item.get('conn_country'),
            item.get('ip_addr_decrypted'),
            item.get('user_agent_decrypted'),
            item.get('master_metadata_track_name'),
            item.get('master_metadata_album_artist_name'),
            item.get('master_metadata_album_album_name'),
            item.get('spotify_track_uri'),
            item.get('episode_name'),
            item.get('episode_show_name'),
            item.get('spotify_episode_uri'),
            item.get('reason_start'),
            item.get('reason_end'),
            1 if item.get('shuffle') == True else 0 if item.get('shuffle') == False else None,
            1 if item.get('skipped') == True else 0 if item.get('skipped') == False else None,
            1 if item.get('offline') == True else 0 if item.get('offline') == False else None,
            item.get('offline_timestamp'),
            1 if item.get('incognito_mode') == True else 0 if item.get('incognito_mode') == False else None
        ))
    total_records += len(data)
    print(f"    Imported {len(data)} records from {json_file}")

conn.commit()
conn.close()

print(f"Successfully imported {total_records} tracks into the database!")