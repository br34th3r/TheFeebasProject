import random

fishingTileAmount = 19
spawnTileAmount = 433
feebasTileAmount = 6

fishingTiles = []
shuffleList = []

startingTile = random.randint(0, spawnTileAmount - fishingTileAmount)

for i in range(18):
    fishingTiles.append(startingTile + i)

for i in range(100000):
    shuffles = 0
    feebasFound = False
    while feebasFound != True:
        feebasTiles = []
        feebasStartingTile = random.randint(0, spawnTileAmount - feebasTileAmount)
        for i in range(feebasTileAmount):
            feebasTiles.append(feebasStartingTile + i)
            if feebasTiles[i] in fishingTiles:
                feebasFound = True
                break
        if feebasFound:
            break
        else:
            shuffles += 1
    shuffleList.append(shuffles)

total = 0

for val in shuffleList:
    total += val

print(total/len(shuffleList))
