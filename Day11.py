
with open('inputDay11.txt','r') as f:
    lines = f.readlines()

def outOctopuses(lines, x):
    print("")
    print("  ############ {} #############".format(x))
    for l in lines:
        print("")
        for d in l:
            if(d == 0):
                print("  " + '\x1b[1;30;50m' +"0"+ '\x1b[0m', end='')
            elif len(str(d)) == 1:
                print("  " + str(d), end='')
            else:
                print(" " + str(d), end='')
    print("")



for i, l in enumerate(lines):
    l = l.replace("\n","")
    temp = []
    for d in l:
        temp.append(int(d))
    lines[i] = temp
outOctopuses(lines, 0)

def addOne(lines):
    global explosions
    for iLine, line in enumerate(lines):
        for iDigit, digit in enumerate(line):
            digit+=1
            if(digit > 9):
                explosions+=1
                digit = 0

            lines[iLine][iDigit] = digit
    return lines

def adjacent(lines):
    done = False
    while not done:
        linesBefore = [row[:] for row in lines]
        done = True
        for iLine, line in enumerate(lines):
            for iDigit, digit in enumerate(line):
                if digit == 0:
                    lineAmount = len(lines)-1
                    digitAmount = len(line)-1

                    if iLine != 0:
                        lines[iLine-1][iDigit] = increaseDigit(lines[iLine-1][iDigit])
                    if iLine != lineAmount:
                        lines[iLine+1][iDigit] = increaseDigit(lines[iLine+1][iDigit])
                    if iDigit != 0:
                        lines[iLine][iDigit-1] = increaseDigit(lines[iLine][iDigit-1])
                    if iDigit != digitAmount:
                        lines[iLine][iDigit+1] = increaseDigit(lines[iLine][iDigit+1])

                    if iDigit != 0 and iLine != 0:
                        lines[iLine-1][iDigit-1] = increaseDigit(lines[iLine-1][iDigit-1])
                    if iDigit != digitAmount and iLine != 0:
                        lines[iLine-1][iDigit+1] = increaseDigit(lines[iLine-1][iDigit+1])
                    if iDigit != 0 and iLine != lineAmount:
                        lines[iLine+1][iDigit-1] = increaseDigit(lines[iLine+1][iDigit-1])
                    if iDigit != digitAmount and iLine != lineAmount:
                        lines[iLine+1][iDigit+1] = increaseDigit(lines[iLine+1][iDigit+1])
                    lines[iLine][iDigit] = 'X'
        if linesBefore == lines:
            outOctopuses(lines, x + 1)
            print('Done')
            lines = [[_el if _el != "X" else 0 for _el in _ar] for _ar in lines]
            return lines
        else:
            done = False
            outOctopuses(lines, x + 1)
            print('NotDone')

def flashSync(lines, x):
    for line in lines:
        for d in line:
            if d == 0:
                continue
            else:
                print("{} not synced".format(x))
                return
    print("{} synced!".format(x))
    exit()


def increaseDigit(d):
    global explosions
    if d == "X":
        return "X"
    elif d == 0:
        return 0
    elif d == 9:
        explosions+=1
        return 0
    else:
        return d+1

print('')
explosions = 0
for x in range(1000):
    lines = addOne(lines)
    outOctopuses(lines, x+1)
    lines = adjacent(lines)
    outOctopuses(lines, x+1)
    flashSync(lines, x+1)







print('')
print("Total Explosions: {}".format(explosions))