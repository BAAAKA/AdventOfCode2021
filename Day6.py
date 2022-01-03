
with open('inputDay6.txt','r') as f:
    lines = f.readlines()


lines = lines[0].split(',')
days = 80


araDays = [0]*11

for l in lines:
    l = int(l)
    araDays[l]+=1




for day in range(days):
    print(araDays)
    temp = araDays
    araDays[7] += araDays[0]
    araDays[9] += araDays[0]
    for m in range(10):
        araDays[m] = temp[m + 1]

    print(araDays)

    totalfish = 0
    for f in araDays:
        totalfish += f

    print('Today is Day {}'.format(day))
    print('There are {} FISH'.format(totalfish))


    #print(lines)
totalfish = 0
for f in araDays:
    totalfish += f

print('Today is Day {}'.format(day))
print('There are {} FISH'.format(totalfish))