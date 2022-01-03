
with open('inputDay8.txt','r') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    lines[i] = l.replace("\n","")
    print(lines[i])

lowpoints = 0

for rowNr, row in enumerate(lines):
    print('')
    for digitNr, digit in enumerate(row):
        print('')
        print('the digit {} with {}- '.format(digit,digitNr), end ="")
        lowPoint = True
        if rowNr > 0:
            nr = lines[rowNr-1][digitNr]
            print(nr, end ="")
            if(nr <= digit):
                lowPoint = False
        if rowNr+1 < len(lines):
            nr = lines[rowNr+1][digitNr]
            print(nr, end ="")
            if(nr <= digit):
                lowPoint = False
        if int(digitNr)+1 < len(row):
            nr = lines[rowNr][digitNr+1]
            print(nr, end ="")
            if(nr <= digit):
                lowPoint = False
        if int(digitNr) > 0:
            nr = lines[rowNr][digitNr-1]
            print(nr, end ="")
            if(nr <= digit):
                lowPoint = False
        if(lowPoint):
            print('')
            print("{} is a lowpoint!".format(digit))
            lowpoints+=int(digit)+1
print("")
print("total lowpoint is {}".format(lowpoints))