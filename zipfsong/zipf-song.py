import sys
import heapq

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
        heapq.heappush(songs, (-quality, trackNumber, title))
    return songs

def main():
    firstLine = sys.stdin.readline()
    numSongs = int(firstLine.split()[0])
    numSelected = int(firstLine.split()[1])

    songs = getSongQuality(numSongs)
    selections = getSelectedSongs(songs)

    for i in range(numSelected):
        print heapq.heappop(songs)[2]

if __name__ == '__main__':
    main()
