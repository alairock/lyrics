import requests
import os


def get_lyrics(track, artist, album):
    api_key = os.getenv('MM_KEY', None)
    params = {
        'apikey': api_key,
        'q_track': track,
        'q_artist': artist,
        'format': 'json',
    }

    url = 'http://api.musixmatch.com/ws/1.1/matcher.lyrics.get'
    results = requests.get(url, params)
    if results.json()['message']['header']['status_code'] != 404:
        return '\n\n' + str(results.json()['message']['body']
                          ['lyrics']['lyrics_body'])
    return "No Lyrics Found"
