import json
import sqlite3

# Connect to your database (replace with your actual .db filename)
conn = sqlite3.connect('spotifyDatabase.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS streaming_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        end_time TEXT,
        artist_name TEXT,
        track_name TEXT,
        ms_played INTEGER
    )
''')

# Read the JSON file
with open('spotify_recent.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Insert each record
for item in data:
    cursor.execute('''
        INSERT INTO streaming_history (end_time, artist_name, track_name, ms_played)
        VALUES (?, ?, ?, ?)
    ''', (item['endTime'], item['artistName'], item['trackName'], item['msPlayed']))

conn.commit()
conn.close()

print(f"Successfully imported {len(data)} tracks into the database!")