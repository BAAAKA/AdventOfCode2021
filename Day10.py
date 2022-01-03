
with open('inputDay10.txt','r') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    lines[i] = l.replace("\n","")
    #print(lines[i])

openers = ["[","(","{","<"]
closers = ["]",")","}",">"]

values = {
    "]": 2,
    ")": 1,
    "}": 3,
    ">": 4
}
def calcScore(lineAra):
    totalScore = 0
    for sym in lineAra:
        totalScore*=5
        totalScore += values[sym]
    print("Returning Score of {}".format(totalScore))
    return totalScore

totalScores = []

lineAra = []
for line in lines:
    lineAra = []
    for sym in line:
        if sym in openers:
            #print("{} is an opener".format(sym))
            lineAra.append(sym)
        elif sym in closers:
            #print("{} is a closer".format(sym))
            if closers.index(sym) == openers.index(lineAra[-1]):
                #print("{} correct closure".format(openers[closers.index(sym)]))
                lineAra.pop(-1)
            else:
                #print("Wrong Closure! {}, expected {}".format(sym, lineAra[-1]))
                lineAra = []
                break

    if not lineAra == []:
        lineAra = lineAra[::-1]
        temp = []
        for sym in lineAra:
            temp.append(closers[openers.index(sym)])
        lineAra = temp
        print(lineAra)
        totalScores.append(calcScore(lineAra))


print(totalScores)

totalScore = sorted(totalScores)[int(len(totalScores)/2)]
print("remain: {}".format(lineAra))
print("TotalScore: {}".format(totalScore))


