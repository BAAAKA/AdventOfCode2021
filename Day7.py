
with open('inputDay7.txt','r') as f:
    lines = f.readlines()

lines = lines[0].split(',')
for i, l in enumerate(lines):
    print(l)
    lines[i] = int(l)

minCrab = min(lines)
maxCrab = max(lines)

fuelSpend = [0]*abs(maxCrab-minCrab)


for height in range(maxCrab-minCrab):
    print("{} out of {}".format(height, (maxCrab-minCrab)))
    for crabHeight in lines:
        goalHeight = minCrab+height
        difference = 0
        for nr in range(abs(goalHeight - crabHeight)):
            difference+=nr+1
        fuelSpend[height] += (difference)


print(fuelSpend)
print("The min amount of Fuel spend is: {}".format(min(fuelSpend)))