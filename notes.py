import json
import time

def load_song(song_id):
    with open('songs/'+song_id+'.json') as file:
        data = json.load(file)
    return data

def get_beat(seconds, tempo):
    return int(seconds // (60 / tempo))

def get_buttons(beat, song_data):
    return [song_data["tracks"][track][beat] for track in range(4)]

print(get_buttons(0, load_song('example')))