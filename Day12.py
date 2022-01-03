
with open('inputDay12.txt','r') as f:
    lines = f.readlines()

caves = {}

for i, l in enumerate(lines):
    l = l.replace("\n","")
    l = l.split("-")
    for cave in l:
        if not cave in caves:
            caves.update({cave:[]})
    caves[l[0]].append(l[1])
    caves[l[1]].append(l[0])
print(caves)

def printCave(pathTillNow, ending):
    print(pathTillNow, end='')
    print(ending)

def canContinue(pathTillNow, cave):
    pathTillNow = pathTillNow.split("-")
    pathTillNow = sorted(pathTillNow)
    if pathTillNow.count(cave) == 0:
        return True
    elif pathTillNow.count(cave) == 1:
        for i, l in enumerate(pathTillNow):
            if i < (len(pathTillNow) - 1) and l == pathTillNow[i + 1] and l.islower():
                print("DUPLICATE {}".format(l))
                return False
        return True
    else:
        return False
def searchCave(sCave, pathTillNow):
    global paths
    for cave in caves[sCave]:
        if cave == 'end':
            printCave("{}-{}".format(pathTillNow, cave), "-END")
            paths+=1
            pass
        elif cave == 'start':
            pass
        elif cave.isupper():
            searchCave(cave, "{}-{}".format(pathTillNow, cave))
        elif canContinue(pathTillNow, cave):
            searchCave(cave, "{}-{}".format(pathTillNow, cave))
        else:
            printCave("{}-{}".format(pathTillNow, cave), "...")
            pass

paths = 0

for cave in caves["start"]:
    searchCave(cave, 'start-{}'.format(cave))

print("There are {} paths from start to finish!".format(paths))