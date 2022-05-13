from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

scope = "playlist-modify-public"
scope_read = 'playlist-read-collaborative'

playlist_id = '4OT5npqGnPNYBXWWf1Ja5R'
wish_you_were_here = '6mFkJmJqdDVQ1REhVfGgd1'
tnt='7LRMbd3LEoV5wZJvXT1Lwb'
glass='spotify:track:5OHbgQbHzTjolHzWffSrvn'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret= client_secret, redirect_uri='http://localhost:8080', scope=scope))
sp_read = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret= client_secret, redirect_uri='http://localhost:8080', scope=scope_read))


track_lists=[]

with open ('songs.txt','r') as f:
    for line in f:
        line=line.split()
        track_lists.append(line) 
# print(track_lists)
print ('Song | Tempo | Loudness')
for track in track_lists:
    analysis = sp.audio_analysis(track[0])
    print(' '.join(track[2:]),'|', analysis['track']['tempo'],'|',analysis['track']['loudness'])