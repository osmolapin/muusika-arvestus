from pygame import *
import vlc, choose, os, check
from difflib import SequenceMatcher

def check_similarity(a, b):
    threshold = 0.6
    similarity = SequenceMatcher(None, a, b).ratio()
    print("\nSarnasus:\t", similarity)
    if similarity > threshold: 
        return True
    else:
        return False

path = check.isFile()

learned_songs = []

while True:
    songName = choose.randomFile(path)
    cleanName = os.path.splitext(songName)[0]

    if check.isLearned(songName, learned_songs):
        continue

    #laulu valimine ja playeri valmistamine
    media_player = vlc.MediaPlayer()
    media = vlc.Media(path + "/" + songName)
    media_player.set_media(media)


    timestamp = choose.randomTimestamp()

    #laulu käima panemine
    media_player.play()
    #positsiooni panemine
    media_player.set_position(timestamp)

    guessName = input("\nKirjuta laulu nimi:")

    print("\nSinu arvamus:\t", guessName)
    print("Päris nimi:\t", cleanName)

    while True:
        guess = check_similarity(guessName, cleanName)

        if guess == True:
            print("\nTulemus:\tHea töö!")
            learned_songs.append(songName)
            break

        elif guess == False:
            print("\nTulemus:\tJäta laul meelde!")
            break

    media_player.stop()