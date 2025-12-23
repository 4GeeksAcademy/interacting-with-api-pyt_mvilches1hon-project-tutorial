import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import seaborn as sns
import spotipy
import spotipy as spotify


# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
print(f'El ID es: {client_id}')


# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

id_artista = '5YGY8feqx7naU7z4HrwZM6'

results = spotify.Spotify.artist_top_tracks(spotify.Spotify, artist_id=id_artista)
canciones = []

for track in results['tracks']:
    canciones.append(
        {'name':track['name'],
        'popularity' : track['popularity']}
    )



print(track)