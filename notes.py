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

start = time.time() 
data = load_song('example')
while True: 
    beat = get_beat(time.time() - start, data["tempo"])
    print(get_buttons(beat, data))
