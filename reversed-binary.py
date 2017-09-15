import sys

num = sys.stdin.readline()
binary =  bin(int(num))[2::]
reversedBin = binary[::-1]
print int(reversedBin, 2)
