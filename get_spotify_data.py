import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from datetime import datetime
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

# Set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope='user-read-recently-played user-top-read'
))

# Get recently played tracks (last 50)
results = sp.current_user_recently_played(limit=50)

# Format the data similar to Spotify's download format
listening_history = []
for item in results['items']:
    track = item['track']
    listening_history.append({
        'endTime': item['played_at'],
        'artistName': track['artists'][0]['name'],
        'trackName': track['name'],
        'msPlayed': track['duration_ms']
    })

# Save to JSON file
with open('spotify_recent.json', 'w', encoding='utf-8') as f:
    json.dump(listening_history, f, indent=2, ensure_ascii=False)

print(f"Successfully retrieved {len(listening_history)} tracks!")
print("Saved to spotify_recent.json")