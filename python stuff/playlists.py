from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

scope = "playlist-modify-public"

playlist_id = '4OT5npqGnPNYBXWWf1Ja5R'
track_id = '6mFkJmJqdDVQ1REhVfGgd1'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret= client_secret, redirect_uri='http://localhost:8080', scope=scope))
play = sp.playlist_add_items(playlist_id=playlist_id,items=[track_id])

