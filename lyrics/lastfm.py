import requests
from . import osx, lyrics
import os


class LastFM:
    def __init__(self):
        self.name, self.artist, self.album = self.get_last_track_name()
        self.hashed = self.hash_track()
        self.first = True

    def print_info(self, count):
        print('Name: ', self.name)
        print('Artist: ', self.artist)
        print('Album: ', self.album)
        print('Lyrics: ',
              lyrics.get_lyrics(self.name, self.artist, self.album))
        osx.send_message(self.name, self.artist)

    @staticmethod
    def get_last_track_name():
        params = {
            'format': 'json',
            'api_key': os.getenv('LASTFM_KEY', None),
            'user': os.getenv('LASTFM_USER', None),
            'limit': 1,
            'method': 'user.getrecenttracks',
        }
        response = requests.get('http://ws.audioscrobbler.com/2.0/', params)
        now_playing = response.json()['recenttracks']['track'][0]
        name = now_playing['name']
        artist = now_playing['artist']['#text']
        album = now_playing['album']['#text']
        return name, artist, album

    def hash_track(self):
        self.name, self.artist, self.album = self.get_last_track_name()
        import hashlib
        import json
        data = {'name': self.name, 'artist': self.artist, 'album': self.album}
        data_md5 = hashlib.md5(json.dumps(data, sort_keys=True)
                               .encode('utf-8')).hexdigest()
        return data_md5

    def song_has_changed(self):
        if self.hashed != self.hash_track() or self.first:
            self.first = False
            self.hashed = self.hash_track()
            return True
        return False
