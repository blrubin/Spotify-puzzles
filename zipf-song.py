import sys

def getSongQuality(numSongs):
    songs = []
    for i in range(numSongs):
        song = sys.stdin.readline().split()
        title = song[1].rstrip()
        trackNumber = i + 1
        playCount = int(song[0])
        
        # zipfs law predicts frequency should be 1 / track number
        # quality = play count / predicted frequency
        # therefore quality = track number * play count

        quality = playCount * trackNumber
        songs.append([title, quality, trackNumber])
    return songs

def getSelectedSongs(songs):
    return sorted(songs, key=lambda x: x[1], reverse=True)

def main():
    firstLine = sys.stdin.readline()
    numSongs = int(firstLine.split()[0])
    numSelected = int(firstLine.split()[1])

    songs = getSongQuality(numSongs)
    selections = getSelectedSongs(songs)

    for song in selections[:numSelected]:
        print song[0]   

if __name__ == '__main__':
    main()
