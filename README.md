# Lyrics
Get an alert of the song you are currently playing (specifically
scrobbling to last.fm)

Show the name, artist, album and lyrics of currently playing track
printed in your console where this is running


## Prereqs.
This was written for Python 3.5. Mileage may vary in other versions 

This uses the following modules:
 - pyobjc-core
 - pyobjc


## Installation and Usage
A binary will be provided someday, but for now: 
1 - `$ git clone git@github.com:alairock/lyrics.git`
2 - `$ cp runner.sh.example runner.sh`
3 - Modify the `runner.sh` file, change vars to your specific values
4 - `$ ./runner.sh`


## Limitations
This uses MusixMatch API. You will need to provide a key, and because
of their *stupid* limitations, you can only display a portion of the
songs lyrics
