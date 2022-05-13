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


analysis1 = sp.audio_analysis(track_id=wish_you_were_here)
# analysis2 = sp.audio_analysis(track_id=tnt)
# analysis3 = sp.audio_analysis(track_id=glass)

# for k,v in enumerate(analysis):
#     print (k,v)


with open('analysis.txt','a')as f:
    for param in analysis1['track'].keys():
        f.write(param+'\n')

# print('Wish you were here tempo:', analysis1['track']['tempo'])
# print('T.N.T. tempo:',analysis2['track']['tempo'])
# print('Glass in the park tempo:',analysis3['track']['tempo'])
# print('Wish you were here loudness: ', analysis1['track']['loudness'])
# print('T.N.T. loudness:',analysis2['track']['loudness'])
# print('Glass in the park loudness:',analysis3['track']['loudness'])

# songs = sp_read.playlist_tracks(playlist_id)
# # print(songs['items'][1])
# for song in (songs['items']):
#     print(song['track']['uri'])
#     print(song['track']['name'])
#     print('******')
#     break

# with open ('songs.txt','a') as f:
#     for song in (songs['items']):
#         f.write(song['track']['uri']+' : ')
#         f.write(song['track']['name']+'\n')