import time
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from phue import Bridge
from PIL import Image
from io import BytesIO
import colorsys

# Set up Philips Hue Bridge
b = Bridge('172.17.187.253', 'fAoQajpSocxzpkNodgpZ8u8LCji1epSCYSarbeXq')
b.connect()
b.get_api()

# Set up Spotify API
scope = "user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id='f6023b464d11474bb51c9e9528e4a934',client_secret='6889568353ca4f0f8f6a21ae7ae82682',redirect_uri='http://localhost:8000/callback'))
user_info = sp.current_user()

# Main loop
while True:
    print('test')
    # Get current Spotify playback information
    playback = sp.current_playback(additional_types=['track'], market='from_token')
    if playback and playback['is_playing']:
        # Get the track information
        track_name = playback['item']['name']
        artist_name = playback['item']['artists'][0]['name']

        # Get the average RGB color of the album cover
        album_cover_url = playback['item']['album']['images'][0]['url']
        response = requests.get(album_cover_url)
        print(type(response.content))
        # Open the image from bytes
        img = Image.open(BytesIO(response.content))

        # Get the pixel data as a list of tuples (R, G, B)
        pixels = list(img.getdata())

        # Calculate the average RGB color
        avg_rgb = tuple(round(sum(channel) / len(pixels)) for channel in zip(*pixels))     
        print(avg_rgb) 
        h, s, v = colorsys.rgb_to_hsv(avg_rgb[0] / 255.0, avg_rgb[1] / 255.0, avg_rgb[2] / 255.0)
        print(b.lights)
        light = b.lights[3]
        # Set light to the HSB color
        light.on = True
        light.hue = int(h * 65535)
        light.saturation = int(s * 254)
        light.brightness = int(v * 254)
        # Add color loop effect
        light.effect= 'channelchange'

    time.sleep(1)
