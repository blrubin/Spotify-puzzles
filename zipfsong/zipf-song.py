import sys

def getSongQuality(numSongs):
    songs = []
    for i in range(numSongs):
        song = sys.stdin.readline().split()
        title = song[1].rstrip()
        zi = 1/float(i+1)
        fi = int(song[0])
        qi = fi/zi
        songs.append([title, qi, i])
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
